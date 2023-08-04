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

document.addEventListener("DOMContentLoaded", function () {
  // Get references to the button and the content
  const revealButton = document.getElementById("text-button");
  const content = document.getElementById("content");

  // Add an event listener to the button
  revealButton.addEventListener("click", function () {
    // Toggle the 'hidden' class on the content div
    content.classList.toggle("hidden");
  });
});
