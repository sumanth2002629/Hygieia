$(document).ready(function(){
 
  
    //Dynamic Next
   $(".btn-next").on("click", function(){
     nextStep = $("#" + $(this).parents(".slider-step").data("nextStep"));
     $(this).parents(".slider-step").attr("data-anim","hide-to--left");
     nextStep.attr("data-anim","show-from--right");
   });
   
   //Dynamic Back
   $(".btn-back").on("click", function(){
     backTo = $("#" + $(this).parents(".slider-step").data("backTo"));
     $(this).parents(".slider-step").attr("data-anim","hide-to--right");
     backTo.attr("data-anim","show-from--left");
   });
 });