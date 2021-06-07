function init(){
    var firstQuestionBtnList = document.querySelectorAll("#firstQuestion");
    var secondQuestionBtnList = document.querySelectorAll("#secondQuestion");
    var thirdQuestionBtnList = document.querySelectorAll("#thirdQuestion");
    var fourthQuestionBtnList = document.querySelectorAll("#fourthQuestion");

    var price;
    var who;
    var time;
    var size;

    for(var i = 0;i < firstQuestionBtnList.length;i++){
        firstQuestionBtnList[i].addEventListener("click",function (evt) {
            price = evt.target.value;
            document.querySelector("#firstQuestionContainer").style = "display:none";
            document.querySelector("#secondQuestionContainer").style = "";
        });
    }

    for(var i = 0;i < secondQuestionBtnList.length;i++){
        secondQuestionBtnList[i].addEventListener("click",function (evt) {
            who = evt.target.value;
            document.querySelector("#secondQuestionContainer").style = "display:none";
            document.querySelector("#thirdQuestionContainer").style = "";
        });
    }

    for(var i = 0;i < thirdQuestionBtnList.length;i++){
        thirdQuestionBtnList[i].addEventListener("click",function (evt) {
            time = evt.target.value;
            document.querySelector("#thirdQuestionContainer").style = "display:none";
            document.querySelector("#fourthQuestionContainer").style = "";
        });
    }

    for(var i = 0;i < fourthQuestionBtnList.length;i++){
        fourthQuestionBtnList[i].addEventListener("click",function (evt) {
            size = evt.target.value;
            var url = "result/?price=" + price + "&who=" + who + "&time=" + time + "&size=" + size;
            location.href = url
        });
    }
}


document.addEventListener("DOMContentLoaded", function(){
    init();
});