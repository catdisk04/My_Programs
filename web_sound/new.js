const body = document.body

//To check
var div = document.createElement("p");
div.innerHTML="Hello";
body.append(div);

var aud = document.createElement("audio");
aud.setAttribute("src", "audiocheck.net_sin_1000Hz_-10dBFS_3s.wav");
aud.setAttribute("controls", "controls");
body.append(aud);

let correctTimes=[];

const arr=[
`<audio controls src=\"audiocheck.net_sin_2000Hz_-10dBFS_3s.wav\"></audio>
<button>1000 Hz</button>
<button onclick=\"correctTimes.push(Date.now());\">2000 Hz</button>`, 

`<audio controls src=\"audiocheck.net_sin_1000Hz_-10dBFS_3s.wav\"></audio>
<button onclick=\"correctTimes.push(Date.now());\">1000 Hz</button>
<button>2000 Hz</button>`
]

function initChoices(){
startTime=Date.now();
document.getElementById("list_div").innerHTML='<ol><li id="li1"></li><li id="li2"></li><li id="li3"></li><li id="li4"></li><li id="li5"></li></ol><button onclick="endChoices();">Finish</button>';

for (let i=1; i<=5; i++){
	document.getElementById("li"+i).innerHTML = arr[Math.floor(Math.random()*2 )];
}
document.getElementById("end_div").innerHTML="";
}


function endChoices(){
	let s = "";
	for (let i = 0; i< correctTimes.length; i++){
		s +=Math.floor((correctTimes[i]-startTime)/100)/10;
		s+="sec<br>"
		console.log(correctTimes[i]);
	}
	console.log(startTime);
	document.getElementById("end_div").innerHTML="<p>You answered correctly ("+correctTimes.length+")times</p><br>";
	document.getElementById("end_div").innerHTML+="<p>Times for correct answers:<br> " + s + "</p>";
	console.log(correctTimes);
}
