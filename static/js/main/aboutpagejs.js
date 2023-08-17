var x = document.getElementById("aboutpanel");
var y = document.getElementById("register");
var z = document.getElementById("btn");

function cv() {
  x.style.left = "-100%";/* chilo 400px*/
  y.style.left = "0px";
  z.style.left = "120px";
}

function about() {
  x.style.left = "0px";
  y.style.left = "100%"; /* chilo 450px*/
  z.style.left = "0px";
}
