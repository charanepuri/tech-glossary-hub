const topBtn=document.getElementById("topBtn");

window.onscroll=function(){

    topBtn.style.display=
    window.scrollY>300?"block":"none";

}

topBtn.onclick=function(){

    window.scrollTo({

        top:0,

        behavior:"smooth"

    });

}