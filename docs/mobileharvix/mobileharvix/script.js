function uppermenu() {
	document.getElementById('menu').style.top = "0px";
}


document.ontouchstart = function(e){
  if(e.target.type == 'text' || e.target.type == 'submit'){

  }
  else {
    e.preventDefault();
  }
}

function unuppermenu() {
	document.getElementById('menu').style.top = "-402px";
}