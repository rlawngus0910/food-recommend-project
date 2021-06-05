function thirdQuestion(){
    var thirdQuestionTemplate = document.querySelector("#question3").innerHTML;
    document.querySelector("div.bg").innerHTML = "";
    document.querySelector("div.bg").innerHTML = thirdQuestionTemplate;

    /*for(var i = 0;firstQuestionBtnList.length;i++){
        firstQuestionBtnList[i].addEventListener("click",function () {
            secondQuestion();
        });
    }*/
}

function secondQuestion(){
    var secondQuestionTemplate = document.querySelector("#question2").innerHTML;
    document.querySelector("div.bg").innerHTML = "";
    document.querySelector("div.bg").innerHTML = secondQuestionTemplate;
    window.onload = function() {
        var secondQuestionBtnList = document.querySelectorAll("#secondQuestion");

        console.log(secondQuestionBtnList);
        for(var i = 0;secondQuestionBtnList.length;i++){
            secondQuestionBtnList[i].addEventListener("click",function () {
                thirdQuestion();
            });
        }
    }
}

function init(){
    var firstQuestionBtnList = document.querySelectorAll("#firstQuestion");
    var secondQuestionBtnList = document.querySelectorAll("#secondQuestion");
    var thirdQuestionBtnList = document.querySelectorAll("#thirdQuestion");
    var fourthQuestionBtnList = document.querySelectorAll("#fourthQuestion");

    var price;
    var who;
    var time;
    var size;

    console.log(firstQuestionBtnList);
    console.log(secondQuestionBtnList);


    for(var i = 0;i < firstQuestionBtnList.length;i++){
        firstQuestionBtnList[i].addEventListener("click",function (evt) {
            console.log(evt.target.value)
            price = evt.target.value;
            document.querySelector("#firstQuestionContainer").style = "display:none";
            document.querySelector("#secondQuestionContainer").style = "";
        });
    }

    for(var i = 0;i < secondQuestionBtnList.length;i++){
        secondQuestionBtnList[i].addEventListener("click",function (evt) {
            console.log(evt.target.value)
            who = evt.target.value;
            document.querySelector("#secondQuestionContainer").style = "display:none";
            document.querySelector("#thirdQuestionContainer").style = "";
        });
    }

    for(var i = 0;i < thirdQuestionBtnList.length;i++){
        thirdQuestionBtnList[i].addEventListener("click",function (evt) {
            console.log(evt.target.value)
            time = evt.target.value;
            document.querySelector("#thirdQuestionContainer").style = "display:none";
            document.querySelector("#fourthQuestionContainer").style = "";
        });
    }

    for(var i = 0;i < fourthQuestionBtnList.length;i++){
        fourthQuestionBtnList[i].addEventListener("click",function (evt) {
            console.log(evt.target.value)
            size = evt.target.value;
            var url = "result/?price=" + price + "&who=" + who + "&time=" + time;
            location.href = url
        });
    }


}


document.addEventListener("DOMContentLoaded", function(){
	console.log("DOMContentLoaded");
    init();
});