if (localStorage.getItem("access_token") === null) {
    window.location.href= "/login";
}
$(document).ready(function(){
    $("#username").text(` ${sessionStorage.getItem("username")}`);
    $("#email").text(`Email: ${sessionStorage.getItem("email")}`);
    $("#role").text(`role: ${sessionStorage.getItem("role")}`);
});

if (localStorage.getItem("access_token") === null) {
    window.location.href = "/login";
}

function handleProfilePhotoUpload() {
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = 'image/*';
    fileInput.style.display = 'none';

    fileInput.onchange = function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const profileImage = document.getElementById('profileImage');
                profileImage.src = e.target.result;

                sessionStorage.setItem('profileImageSrc', e.target.result);
            };
            // data:[<mediatype>][;base64],<data>
           // It also stores the base64 encoded image data in the session storage.
            reader.readAsDataURL(file);
        }
    };

    fileInput.click();
}

document.addEventListener('DOMContentLoaded', function() {
    const profileImage = document.getElementById('profileImage');
    const storedImageSrc = sessionStorage.getItem('profileImageSrc');

    if (storedImageSrc) {
        profileImage.src = storedImageSrc;
    }
});







