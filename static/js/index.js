document.addEventListener("DOMContentLoaded", function () {
  const results = document.getElementById("search_results");
  results.style.display = "none";

  // Inject CSS for shaking effect and red border
  const style = document.createElement("style");
  style.innerHTML = `
    .shake {
      animation: shake 0.5s ease-in-out;
    }

    @keyframes shake {
      0% { transform: translateX(0); }
      25% { transform: translateX(-5px); }
      50% { transform: translateX(5px); }
      75% { transform: translateX(-5px); }
      100% { transform: translateX(0); }
    }

    .invalid {
      border: 2px solid red;
    }
  `;
  document.head.appendChild(style);

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

        const placeholderOption = document.createElement("option");
        placeholderOption.value = "";
        placeholderOption.textContent = "Select Department";
        placeholderOption.disabled = true;
        placeholderOption.selected = true;
        departmentField.appendChild(placeholderOption);

        data.departments.forEach(([value, text]) => {
          const option = document.createElement("option");
          option.value = value;
          option.textContent = text;
          departmentField.appendChild(option);
          departmentField.required = true;
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
  const search = document.getElementById("search");

  function validateFields() {
    let isValid = true;

    const fieldsToValidate = [
      { element: facultyField, value: faculty, name: "faculty" },
      { element: departmentField, value: department, name: "department" },
      { element: semesterField, value: semester, name: "semester" },
      { element: examTypeField, value: exam_type, name: "exam_type" },
      {
        element: document.getElementById("id_course_name"),
        value: course_name,
        name: "course_name",
      },
    ];

    fieldsToValidate.forEach((field) => {
      const input = field.element;
      if (field.value === "") {
        input.classList.add("invalid", "shake");
        setTimeout(() => input.classList.remove("shake"), 500);
        isValid = false;
      } else {
        input.classList.remove("invalid");
      }
    });

    return isValid;
  }

  search.addEventListener("click", function (e) {
    e.preventDefault();

    if (!validateFields()) {
      return;
    }

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
      .then((res) => res.json())
      .then((data) => {
        if (data.length > 0) {
          results.style.display = "block";

          let content = `
            <section>
              <h2 style="margin-bottom: 20px">Search Results: <strong>${data.length}</strong></h2>
              <div class="results">
          `;

          data.forEach((element, index) => {
            content += `
              <div class="tile">
                <i class="bi bi-filetype-pdf"></i>
                <a href="media/${element.question_file}" download id="download-${element.course_name}" name="download">${element.course_name}<br>${element.semester}_${element.year}</a>
              </div>
            `;
          });

          content += `
              </div>
            </section>
          `;

          results.innerHTML = content;
          document.getElementsByName("download").forEach((element) => {
            element.addEventListener("click", function () {
              var download = true;
              fetch("question_results", {
                method: "POST",
                header: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({ download }),
              })
            });
          });
        } else {
          results.style.display = "block";
          results.innerHTML = `
            <section>
              <h2 style="margin-bottom: 20px">No Results Found</h2>
            </section>
          `;
        }
      });
  });
});
