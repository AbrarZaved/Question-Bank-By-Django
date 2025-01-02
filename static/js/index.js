document.addEventListener("DOMContentLoaded", function () {
  // Global variables
  let faculty = "",
    department = "",
    semester = "",
    exam_type = "",
    course_name = "",
    year = 2024;

  // Helper function to replace placeholder options
  function replacePlaceholder(selectElement, placeholderText) {
    const options = Array.from(selectElement.options);
    options.forEach((option) => {
      if (option.value === "" && option.textContent.trim() === "---------") {
        selectElement.removeChild(option);
      }
    });

    const placeholderOption = document.createElement("option");
    placeholderOption.value = "";
    placeholderOption.textContent = placeholderText;
    placeholderOption.disabled = true;
    placeholderOption.selected = true;
    selectElement.insertBefore(placeholderOption, selectElement.firstChild);
  }

  // Update placeholders for semester and exam type
  const semesterField = document.querySelector("[name=semester]");
  const examTypeField = document.querySelector("[name=exam_type]");
  replacePlaceholder(semesterField, "Select Semester");
  replacePlaceholder(examTypeField, "Select Exam Type");

  // Function to update the department choices based on selected faculty
  const facultyField = document.querySelector('[name="faculty"]');
  const departmentField = document.querySelector('[name="department"]');
  facultyField.addEventListener("change", function () {
    faculty = this.value;

    fetch(`get_departments`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ faculty }),
    })
      .then((response) => response.json())
      .then((data) => {
        departmentField.innerHTML = ""; // Clear existing options

        // Add placeholder option
        const placeholderOption = document.createElement("option");
        placeholderOption.value = "";
        placeholderOption.textContent = "Select Department";
        placeholderOption.disabled = true;
        placeholderOption.selected = true;
        departmentField.appendChild(placeholderOption);

        // Add new department options
        data.departments.forEach(([value, text]) => {
          const option = document.createElement("option");
          option.value = value;
          option.textContent = text;
          departmentField.appendChild(option);
        });
      })
      .catch((error) => console.error("Error fetching departments:", error));
  });

  // Update global variables on input change
  const fields = {
    '[name="department"]': (value) => (department = value),
    '[name="semester"]': (value) => (semester = value),
    '[name="exam_type"]': (value) => (exam_type = value),
    "#id_course_name": (value) => (course_name = value),
    "#id_year": (value) => (year = value),
  };

  Object.entries(fields).forEach(([selector, updateFn]) => {
    document.querySelector(selector).addEventListener("input", function () {
      updateFn(this.value);
    });
  });
  const csrfToken = document
    .querySelector('meta[name="csrf-token"]')
    .getAttribute("content");
  var search = document.getElementById("search");
  setInterval(() => {
    if (
      faculty === "" ||
      department === "" ||
      semester === "" ||
      exam_type === "" ||
      course_name === ""
    ) {
      search.disabled = true;
    } else {
      search.disabled = false;
    }
  }, 100);

  search.addEventListener("click", function (e) {
    e.preventDefault();
    fetch("question_results", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify({
        faculty,
        department,
        semester,
        exam_type,
        course_name,
        year,
      }),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Failed to fetch results.");
        }
        return res.json();
      })
      .then((data) => console.log(data))
      .catch((error) => console.error(error));
  });
});
