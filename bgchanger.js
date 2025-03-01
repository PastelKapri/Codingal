function clickfunc(){

    var bg = document.getElementById("background");
    var colors = ["red", "orange", "yellow", "green", "blue", "purple"];
    var colorindex =Math.floor(Math.random()*colors.length);
    bg.style.backgroundColor = colors[colorindex];
}