const collapsibles = document.querySelectorAll(".collapsible");
collapsibles.forEach((collapsible) => {
  collapsible.addEventListener("click", function () {
    this.classList.toggle("active");
    const content = this.nextElementSibling;

    if (content.style.display === "block") {
      content.style.maxHeight = null; // Collapse
      content.style.display = "none"; // Hide content
    } else {
      content.style.display = "block"; // Show content
      content.style.maxHeight = content.scrollHeight + "px"; // Expand with animation
    }
  });
});
