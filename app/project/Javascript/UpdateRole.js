if (localStorage.getItem("access_token") === null) {
    // $("#error-message").text("Error: You are not allowed to access this page. Please login to continue.");
    window.location.href= "/login";
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
                        if (!response.ok) {
                            throw new Error(`Status ${response.detail}`);
                        }
                        console.log("Authenticated request successful");
                        return response.json();
                    })
                    .then(data => {
                        console.log(data.message);
                        console.log(data.message);
                        // if (data && data.message && data.message == "Role updated successfully"){
                        //     // window.location.href = "/login";
                        // }
                        $("#error").text(data.message);
                    })
                    .catch(error => {
                        console.log("Error:", error.message);

                        if (error ) {
                            $("#error").text(`User not found`);
                        } else {
                            // Check if it's a 404 response indicating "User not found"
                            if (error && error.status === 404) {
                                $("#error").text("User not found. Please check the username and try again.");
                            } else {
                                $("#error").text("An unexpected error occurred. Please try again later.");
                            }
                        }
                    });
            } else {
                // Token is not available, handle authentication or redirect to login
                console.log("Token not available. Perform authentication or redirect to login page.");
            }
        });
    });
});





function logout() {
    localStorage.removeItem("access_token");
    sessionStorage.removeItem("username");
    sessionStorage.removeItem("email");
    sessionStorage.removeItem("role");
    window.location.href= "/login";
        // You can add more cleanup here if needed
    }
    