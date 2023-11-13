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

function mandelbrotSet(canvas, ctx, zoom, offsetX, offsetY) {
  let width = canvas.width;
  let height = canvas.height;

  for (let x = 0; x < width; x++) {
    for (let y = 0; y < height; y++) {
      // Scale and translate the coordinates
      let a = ((x - width / 2) * (4 / width)) / zoom + offsetX;
      let b = ((y - height / 2) * (4 / width)) / zoom + offsetY;

      let ca = a;
      let cb = b;
      let n = 0;
      let maxIterations = 100;

      while (n < maxIterations) {
        let aa = a * a;
        let bb = b * b;
        let twoab = 2 * a * b;
        a = aa - bb + ca;
        b = twoab + cb;

        // Break if the point is not in the Mandelbrot set
        if (aa + bb > 16) {
          break;
        }

        n++;
      }

      // Use a simple coloring algorithm based on the number of iterations
      let brightness = map(n, 0, maxIterations, 0, 255);
      if (n === maxIterations) {
        brightness = 0; // Make it black if it's in the set
      }

      let color = `rgb(${brightness}, ${brightness}, ${brightness})`;
      ctx.fillStyle = color;
      ctx.fillRect(x, y, 1, 1);
    }
  }
}

// Helper function to map a value from one range to another
function map(value, in_min, in_max, out_min, out_max) {
  return ((value - in_min) * (out_max - out_min)) / (in_max - in_min) + out_min;
}

function findBrightestPixel(ctx, width, height) {
  let imageData = ctx.getImageData(0, 0, width, height);
  let data = imageData.data;
  let maxBrightness = 0;
  let targetX = 0;
  let targetY = 0;
  let centerX = width / 2;
  let centerY = height / 2;
  let minDist = Infinity;

  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      let index = (y * width + x) * 4;
      let brightness = data[index]; // Assuming black & white, so only need one channel

      if (brightness > maxBrightness) {
        let dist = Math.hypot(centerX - x, centerY - y);
        if (dist < minDist) {
          maxBrightness = brightness;
          targetX = x;
          targetY = y;
          minDist = dist;
        }
      }
    }
  }

  return { x: targetX, y: targetY };
}
