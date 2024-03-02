function loadContent(contentName) {
  if (!contentName) return; // Do nothing if no content is selected

  // Fetch the HTML file based on contentName
  fetch(`Bible/${contentName}.html`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((html) => {
      // Inject the fetched HTML into the content area
      document.getElementById("content-area").innerHTML = html;
    })
    .catch((error) => {
      console.error("Failed to load content:", error);
    });
}

document.addEventListener("DOMContentLoaded", (event) => {
  // Function to show the selected content div
  function show(id) {
    // Hide all content divs
    const contentDivs = document.querySelectorAll("#content-area > div");
    contentDivs.forEach((div) => {
      div.style.display = "none"; // Hide each div
    });

    // Show the selected content div
    const selectedContent = document.getElementById(id);
    if (selectedContent) {
      selectedContent.style.display = "block"; // Show the div with the matching id

      // Execute scripts within the selected content, if any
      const scripts = selectedContent.getElementsByTagName("script");
      for (let script of scripts) {
        // Create a new script element
        const newScript = document.createElement("script");

        // Copy the script code or src from the original script
        if (script.src) {
          newScript.src = script.src;
        } else {
          newScript.textContent = script.textContent;
        }

        // Append the new script to the document head to execute it
        document.head.appendChild(newScript);

        // Remove the new script element after execution as a cleanup step
        document.head.removeChild(newScript);
      }
    }
  }

  // Check and update button visibility based on the existence of their respective content divs
  function updateButtonVisibility() {
    const ids = ["I", "T", "C", "H"];

    ids.forEach((id) => {
      const contentExists = document.getElementById(id) !== null;
      const button = document.getElementById(`show${id}`);
      if (button) {
        // Ensure the button element was successfully selected
        if (contentExists) {
          // Show button and attach event listener if content exists
          button.style.display = "inline-block";
          button.onclick = () => show(id); // Using onclick for better compatibility
        } else {
          // Hide button if content does not exist
          button.style.display = "none";
        }
      }
    });
  }

  // Initial check to update button visibility
  updateButtonVisibility();
});
