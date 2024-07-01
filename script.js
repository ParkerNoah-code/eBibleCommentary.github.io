function updateURLParameter(param, value) {
  const url = new URL(window.location);
  if (value === null || value === undefined) {
    url.searchParams.delete(param);
  } else {
    value = value.replace(/\//g, ".");
    url.searchParams.set(param, value);
  }
  window.history.pushState({}, "", url);
}

function loadContentFromURL() {
  const urlParams = new URLSearchParams(window.location.search);
  let content = urlParams.get("content") || "about";

  content = content.replace(/\//g, ".");

  loadContent(content);
}

function loadContent(value) {
  value = value.replace(/\//g, ".");

  const fileName = value + ".html";
  updateURLParameter("content", value);

  fetch(fileName)
    .then((response) => {
      if (!response.ok) throw new Error("Network response was not ok");
      return response.text();
    })
    .then((html) => {
      document.getElementById("content-area").innerHTML = html;
      populateSectionDropdown();
      checkForNavTargets();
    })
    .catch((error) => {
      console.error("There was a problem with your fetch operation:", error);
      document.getElementById(
        "content-area"
      ).innerHTML = `<section><p>Error loading content. Please try again.</p></section>`;
    });
}

function checkForNavTargets() {
  const navButton = document.getElementById("back-button");
  const contentArea = document.getElementById("content-area");
  const nav = contentArea.querySelector(".nav");

  if (nav) {
    let targetContent = nav.getAttribute("data-content");
    targetContent = targetContent.replace(/\//g, ".");

    if (targetContent) {
      navButton.style.display = "inline-block";
      navButton.onclick = () => {
        loadContent(targetContent);
      };
    } else {
      navButton.style.display = "none";
    }
  } else {
    navButton.style.display = "none";
  }
}

function populateSectionDropdown() {
  const sections = document.querySelectorAll("#content-area > div");
  const sectionDropdown = document.getElementById("section-dropdown");
  sectionDropdown.innerHTML = "";

  sections.forEach((section) => {
    const option = document.createElement("option");
    option.value = section.id;
    option.textContent = section.getAttribute("dropdownName");
    sectionDropdown.appendChild(option);
  });

  const urlParams = new URLSearchParams(window.location.search);
  const section = urlParams.get("section");

  if (sections.length > 0) {
    sectionDropdown.style.display = "";
    if (section) {
      document.getElementById("section-dropdown").value = section;
      filterSection(section);
    }
  } else {
    sectionDropdown.style.display = "none";
  }
}

function filterSection(sectionId) {
  updateURLParameter("section", sectionId);

  const sections = document.querySelectorAll("#content-area > div");

  sections.forEach((section) => {
    section.style.display = section.id === sectionId ? "" : "none";
  });

  window.scrollTo(0, 0);
}

function updateNavDataAttributes() {
  const navElements = document.querySelectorAll(".nav[data-content]");
  navElements.forEach((el) => {
    let contentAttr = el.getAttribute("data-content");
    if (contentAttr.includes("/")) {
      contentAttr = contentAttr.replace(/\//g, ".");
      el.setAttribute("data-content", contentAttr);
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  updateNavDataAttributes();
  loadContentFromURL();
});
