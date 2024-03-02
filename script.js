// script.js
document.addEventListener("DOMContentLoaded", function () {
  const contentArea = document.getElementById("content-area");
  const dropdown = document.getElementById("content-dropdown");
  const buttons = document.querySelectorAll(".right-boxes button");

  // Create or update hidden state input
  function updateHiddenState(value) {
    let hiddenState = contentArea.querySelector(".hidden-state");
    if (!hiddenState) {
      hiddenState = document.createElement("input");
      hiddenState.type = "hidden";
      hiddenState.className = "hidden-state";
      contentArea.appendChild(hiddenState);
    }
    hiddenState.value = value;
  }

  // Function to check and display buttons
  function checkButtons() {
    buttons.forEach((button) => {
      const targetId = button.id.replace("show", "");
      if (document.getElementById(targetId)) {
        button.style.display = "block";
      } else {
        button.style.display = "none";
      }
    });
  }

  // Load content based on dropdown selection
  function loadContent(value) {
    // Check if the selected content is already loaded
    let alreadyLoaded =
      contentArea.querySelector(".hidden-state") &&
      contentArea.querySelector(".hidden-state").value === value;
    if (!alreadyLoaded) {
      // Simulate loading HTML content (e.g., AJAX request could be used here)
      contentArea.innerHTML = `<div id="${value}">Content for ${value}.html loaded</div>`;
      // Update hidden state
      updateHiddenState(value);
      // Update the URL to reflect the current state
      window.history.pushState(
        { page: value },
        `${value} - Page`,
        `?page=${value}`
      );
    }

    checkButtons();
  }

  // Show specific content and hide others
  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      const targetId = this.id.replace("show", "");
      contentArea.querySelectorAll("div").forEach((div) => {
        if (div.id === targetId) {
          div.style.display = "block";
          // Update URL to reflect button state
          const selectedValue = dropdown.value;
          window.history.pushState(
            { page: selectedValue, button: targetId },
            `${selectedValue} - ${targetId} - Page`,
            `?page=${selectedValue}&button=${targetId}`
          );
        } else {
          div.style.display = "none";
        }
      });
    });
  });

  // Dropdown onchange handler
  dropdown.addEventListener("change", function () {
    loadContent(this.value);
  });

  // Check buttons on load
  checkButtons();

  // Function to parse URL and set the correct state
  function parseUrl() {
    const params = new URLSearchParams(window.location.search);
    const page = params.get("page");
    const button = params.get("button");

    if (page) {
      dropdown.value = page;
      loadContent(page);
    }

    if (button) {
      const buttonElement = document.getElementById(`show${button}`);
      if (buttonElement) {
        buttonElement.click();
      }
    }
  }

  // Call parseUrl on load to check URL and set the correct state
  parseUrl();
});
