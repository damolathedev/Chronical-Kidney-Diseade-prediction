function saveFormData() {
    const formData = {};
    // Get all input elements in the form
    const formInputs = document.querySelectorAll('input, select');
    formInputs.forEach(input => {
        // Save the input value with the input id as the key
        formData[input.id] = input.value;
    });
    // Convert the formData object to a JSON string and save to localStorage
    localStorage.setItem('formData', JSON.stringify(formData));
}

// Function to load form data from localStorage
function loadFormData() {
    const formDataString = localStorage.getItem('formData');
    if (formDataString) {
        const formData = JSON.parse(formDataString);
        // Set the input values based on the stored formData
        for (const key in formData) {
            const inputElement = document.getElementById(key);
            if (inputElement) {
                inputElement.value = formData[key];
            }
        }
    }
}

// Function to clear form data from localStorage
function clearFormData() {
    localStorage.removeItem('formData');
}

// Event listener to save form data on input change
document.addEventListener('input', saveFormData);

// Load form data when the page is loaded
document.addEventListener('DOMContentLoaded', loadFormData);