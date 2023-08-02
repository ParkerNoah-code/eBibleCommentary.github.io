// Function to play the audio and show the custom controls
function playAudioWithControls() {
  const audio = document.getElementById("audio-element");
  if (audio.controls) {
    audio.controls = false;
    audio.pause();
  } else {
    audio.controls = true;
    audio.play();
  }
}
