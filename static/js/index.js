document.addEventListener("DOMContentLoaded", function () {
  const facultyField = document.querySelector('[name="faculty"]');
  const departmentField = document.querySelector('[name="department"]');

  // Function to update the department choices based on selected faculty
  facultyField.addEventListener("change", function () {
    const selectedFaculty = facultyField.value;
    fetch(`get_departments`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ faculty: selectedFaculty }),
    })
      .then((response) => response.json())
      .then((data) => {
        departmentField.innerHTML = "";
        data.departments.forEach(function (department) {
          const option = document.createElement("option");
          option.value = department[0];
          option.textContent = department[1];
          departmentField.appendChild(option);
        });
      });
  });
});
