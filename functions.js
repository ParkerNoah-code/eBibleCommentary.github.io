// Function to play the audio and show the custom controls
function playAudioWithControls() {
    const audio = document.getElementById('audio-element');
    audio.controls = true;
    audio.play();
  }