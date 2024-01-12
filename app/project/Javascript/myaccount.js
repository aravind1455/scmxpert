$(document).ready(function(){
    console.log("working");
    $("#username").text(` ${sessionStorage.getItem("username")}`);
    $("#email").text(`Email: ${sessionStorage.getItem("email")}`);
    $("#role").text(`role: ${sessionStorage.getItem("role")}`);
  });
// Function to handle profile photo upload

function handleProfilePhotoUpload() {
    // Create an input element for file selection
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = 'image/*';
    fileInput.style.display = 'none';

    // Set up an onchange event handler for the file input
    fileInput.onchange = function(event) {
        // Retrieve the selected file
        const file = event.target.files[0];
        if (file) {
            // Create a FileReader to read the selected file as a data URL
            const reader = new FileReader();
            reader.onload = function(e) {
                // Update the source of the profile image with the data URL
                const profileImage = document.getElementById('profileImage');
                profileImage.src = e.target.result;

                // Store the image source in sessionStorage
                sessionStorage.setItem('profileImageSrc', e.target.result);
            };
            reader.readAsDataURL(file);
        }
    };

    // Trigger a click event on the file input to initiate file selection
    fileInput.click();
}

// Display the stored image from sessionStorage on page load
document.addEventListener('DOMContentLoaded', function() {
    // Get the profile image element and the stored image source from sessionStorage
    const profileImage = document.getElementById('profileImage');
    const storedImageSrc = sessionStorage.getItem('profileImageSrc');

    // If a stored image source exists, set it as the source of the profile image
    if (storedImageSrc) {
        profileImage.src = storedImageSrc;
    }
});




// -------------------------------------------------------------------------------------



