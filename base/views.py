from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt

from base.api_class import PriaidDiagnosisClientMine
import base.PriaidDiagnosisClient as PriaidDiagnosisClient

flag = 0
bodySublocations = []
symptoms = []


# Create your views here.
def home(request):
    return render(request, 'base/home.html')


def lobby(request):
    return render(request, 'base/lobby.html', {'title': 'Lobby'})


def room(request):
    return render(request, 'base/room.html', {'title': 'Room'})


def getToken(request):
    appId = "c13e8d2ddedb4901bf4bbc56c5d90d86"
    appCertificate = "1c3a7ebbf4f64bfd9de6488ce6d84808"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name': data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name': member.name}, safe=False)


@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)


def symptom_checker(request):
    api = PriaidDiagnosisClientMine()
    global flag
    locid = 0
    sublocid = 0
    symptom_id = 0
    global bodySublocations
    global symptoms
    if flag == 0:

        flag = 1
        return render(request, "base/symptom_checker.html", {"flag": 0})

    elif flag == 1:
        bodyLocations = api._diagnosisClient.loadBodyLocations()
        if ("body_locations" not in request.GET):
            flag = 0
            return render(request, "base/symptom_checker.html", {"flag": 0})

        body_loc = request.GET["body_locations"]
        flag = 2
        for i in bodyLocations:
            if i["Name"] == body_loc:
                locid = i["ID"]

        bodySublocations = api._diagnosisClient.loadBodySubLocations(locid)
        to_html = [i["Name"] for i in bodySublocations]
        flag = 2
        return render(request, "base/symptom_checker.html", {"flag": 1, "sublocations": to_html})

    elif flag == 2:
        body_subloc = request.GET["body_sublocations"]
        print(body_subloc)
        # bodySubLocations = api._diagnosisClient.loadBodySubLocations(locid)
        for i in bodySublocations:
            if i["Name"] == body_subloc:
                sublocid = i["ID"]

        print(sublocid)

        symptoms = api._diagnosisClient.loadSublocationSymptoms(sublocid, PriaidDiagnosisClient.SelectorStatus.Man)
        flag = 3
        to_html = [i["Name"] for i in symptoms]
        return render(request, "base/symptom_checker.html", {"flag": 2, "symptoms": to_html})

    elif flag == 3:
        if "symptoms" not in request.GET:
            return render(request, "base/symptom_checker.html", {"flag": 3, "diagnosis": []})
        selected_symp = request.GET["symptoms"]
        flag = 0
        for i in symptoms:
            if i["Name"] == selected_symp:
                symptom_id = i["ID"]

        selectedSymptomsIds = [symptom_id]
        # change this based on gender and birth year of patient
        diagnosis = api._diagnosisClient.loadDiagnosis(selectedSymptomsIds, PriaidDiagnosisClient.Gender.Male, 1988)

        to_html = []
        for d in diagnosis:
            specialisations = []
            for specialisation in d["Specialisation"]:
                specialisations.append(specialisation["Name"])
            print("{0} - {1}% \nSpecialisations : {2}\n".format(d["Issue"]["Name"], d["Issue"]["Accuracy"],
                                                                ",".join(x for x in specialisations)))

            to_html.append([d["Issue"]["Name"], d["Issue"]["Accuracy"], ",".join(x for x in specialisations)])

            # print(to_html[0])
        return render(request, "base/symptom_checker.html", {"flag": 3, "diagnosis": to_html})

    flag = 0
    return render(request, "base/symptom_checker.html", {"flag": 0})
