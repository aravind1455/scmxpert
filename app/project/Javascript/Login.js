
console.log("working");
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('submit').addEventListener('click', function (event) {
        // Prevent the default action (navigation to the specified URL)
        event.preventDefault();

        // Validate captcha first
        const userCaptcha = document.getElementById('userCaptcha').value;
        const generatedCaptcha = document.getElementById('captcha').textContent;

        if (userCaptcha !== generatedCaptcha) {
            alert('Captcha is invalid. Please try again.');
            return;
        }

        // Now, proceed with username and password validation
        console.log($("#username").val());
        console.log($("#password").val());

        const formData = new FormData();
        formData.append("username", $("#username").val());
        formData.append("password", $("#password").val());

        fetch("/login", {
            method: "POST",
            body: formData
        })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    return response.json().then(error => {
                        throw new Error(error.detail);
                    });
                }
            })
            .then(response => {
                localStorage.setItem("access_token", `Bearer ${response.access_token}`);
                sessionStorage.setItem("username", `${response.username}`);
                sessionStorage.setItem("email", `${response.email}`);
                sessionStorage.setItem("role", `${response.role}`);

                if (localStorage.getItem("access_token") !== null) {
                    window.location.href = "/Dashboard";
                }
            })
            .catch(error => {
                $("#error").text(`${error.message}`);
                setTimeout(function () {
                    $("#error").text("");
                }, 2000);
            });
    });
});

    // captcha generator
    function generateCaptcha() {
        const captchaElement = document.getElementById('captcha');
        const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        let captcha = '';

        for (let i = 0; i < 6; i++) {
            captcha += characters.charAt(Math.floor(Math.random() * characters.length));
        }

        captchaElement.textContent = captcha;
    }

    // Initial captcha generation
    generateCaptcha();

    // Button click event for captcha generation
    document.getElementById('generateCaptchaBtn').addEventListener('click', function () {
        generateCaptcha();
    });


// logout
function logout() {
    localStorage.removeItem("access_token");
    sessionStorage.removeItem("username");
    sessionStorage.removeItem("email");
    sessionStorage.removeItem("role");
    window.location.href= "/";
    // You can add more cleanup here if needed
}

