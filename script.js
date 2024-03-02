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

  // IDs to check for in the content-area div
  const ids = ["I", "T", "C", "H", "B"];

  // Check each id and set the display of the corresponding button
  ids.forEach((id) => {
    const contentExists = document.getElementById(id) !== null;
    const button = document.getElementById(`show${id}`);
    if (contentExists && button) {
      // If the content div exists, show the button and add click event listener
      button.style.display = "inline-block"; // Show button
      button.addEventListener("click", () => show(id));
    } else if (button) {
      // If the content div does not exist, hide the button
      button.style.display = "none"; // Hide button
    }
  });
});
