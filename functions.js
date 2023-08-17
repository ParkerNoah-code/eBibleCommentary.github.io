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

function playMusicWithControls() {
  const audio = document.getElementById("music-element");
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
  const revealButton = document.getElementById("music-button");
  const content = document.getElementById("music");

  // Add an event listener to the button
  revealButton.addEventListener("click", function () {
    // Toggle the 'hidden' class on the content div
    content.classList.toggle("hidden");
  });
});

function visibility(elementId) {
  const contentElements = document.getElementsByClassName("commentary");
  for (const element of contentElements) {
    if (element.id === elementId) {
      element.style.display = "block";
    } else {
      element.style.display = "none";
    }
  }
}
