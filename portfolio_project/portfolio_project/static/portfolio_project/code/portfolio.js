//For Demo only
var links = document.getElementsByClassName('link')
for(var i = 0; i <= links.length; i++)
   addClass(i)


function addClass(id){
   setTimeout(function(){
      if(id > 0) links[id-1].classList.remove('hover')
      links[id].classList.add('hover')
   }, id*750) 
}

function sidebar_open() {
   document.getElementById("id_body_content").style.marginLeft = "25%";
   document.getElementById("sidebar").style.width = "25%";
   document.getElementById("sidebar").style.display = "block";
   document.getElementById("cat-button").style.display = 'none';
 }

 function sidebar_close() {
   document.getElementById("id_body_content").style.marginLeft = "25%";
   document.getElementById("sidebar").style.width = "25%";
   document.getElementById("sidebar").style.display = "block";
   document.getElementById("cat-button").style.display = 'none';
 }