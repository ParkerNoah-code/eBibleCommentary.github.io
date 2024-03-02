function loadContent(contentName) {
  if (!contentName) return; // Do nothing if no content is selected

  // Fetch the HTML file based on contentName
  fetch(`Bible\\${contentName}.html`)
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

function showContent(contentId) {
  // Hide all content first
  document.querySelectorAll("#content-area > div").forEach(function (content) {
    content.style.display = "none";
  });

  // Show the selected content
  document.getElementById(contentId).style.display = "block";
}
