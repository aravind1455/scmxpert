if (localStorage.getItem("access_token") === null) {

    window.location.href= "/login";
}

if (sessionStorage.getItem("role") === "user") {
    alert("Only Admin can change")
    window.location.href = "/Dashboard";
}

document.addEventListener("DOMContentLoaded", function () {
    $(document).ready(function () {
        $("#submit").on("click", function (event) {
            event.preventDefault();
            const token = localStorage.getItem("access_token");
            if (token) {
                // Token is available, make authenticated request
                fetch("/changeroleuser", {
                    method: "POST",
                    headers: {
                        "Authorization": `${localStorage.getItem("access_token")}`,
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        "user": $("#user").val(),
                    }),
                })
                    .then(response => {
                        return response.json();
                    })
                    .then(response => {
                        // console.log(response);
                        $("#error").text(response.message);
                    })
                    .catch(error => {
                        // console.log("Error:", error.message);
                        $("#error").text("user not found");
                    });
            } else {
                console.log("Token not available. Perform authentication or redirect to login page.");
                alert("Unauthorized access. Redirecting to login...");
                window.location.href = "/login";
            }
        });
    });
});


function logout() {
    localStorage.removeItem("access_token");
    sessionStorage.removeItem("username");
    sessionStorage.removeItem("email");
    sessionStorage.removeItem("role");
    window.location.href= "/";
        // You can add more cleanup here if needed
    }
    