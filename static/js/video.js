	var vid = document.getElementById("bgvid");
	var pauseButton = document.querySelector("#polina button");

	function vidFade() {
	  vid.classList.add("stopfade");
	}

	vid.addEventListener('ended', function() {
	// only functional if "loop" is removed 
	vid.pause();
	// to capture IE10
	vidFade();
	}); 
	// TODO: I don't think this was tested. It doesn't work.
	// Seems like copy pasted code from somewhere
	// pauseButton.addEventListener("click", function() {
	//   vid.classList.toggle("stopfade");
	//   if (vid.paused) {
	//     vid.play();
	//     pauseButton.innerHTML = "<i class='lni-pause'></i>";
	//   } else {
	//     vid.pause();
	//     pauseButton.innerHTML = "<i class='lni-play'></i>";
	//   }
	// })