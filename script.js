function loadContent(contentName) {
  if (!contentName) return; // Do nothing if no content is selected

  // Fetch the HTML file based on contentName
  fetch(`${contentName}.html`)
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
