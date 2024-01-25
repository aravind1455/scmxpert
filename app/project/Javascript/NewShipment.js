if (localStorage.getItem("access_token") === null) {
    window.location.href= "/login";
}
document.addEventListener("DOMContentLoaded", function () {
    // Set the minimum date for the date input field to today's date
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); // January is 0!
    var yyyy = today.getFullYear();

    today = yyyy + '-' + mm + '-' + dd;
    document.getElementById('expected_delivery').min = today;
});
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("submit").addEventListener("click", function (event) {
        event.preventDefault();
        console.log("Dom load", localStorage.getItem("access_token"));

        const token = localStorage.getItem("access_token");

        // Function to check if the token is expired
        function isTokenExpired() {
            const tokenExpiration = localStorage.getItem("access_token");
            if (!tokenExpiration) {
                return true; // Token expiration information not available
            }

            const expirationTime = new Date(tokenExpiration).getTime();
            const currentTime = new Date().getTime();

            return currentTime > expirationTime;
        }

        // Check if token exists and not expired
        if (!isTokenExpired()) {
            fetch("/myshipments", {
                method: "POST",
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem("access_token")}`,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "shipment_number": $("#shipment_number").val(),
                    "container_number": $("#container_number").val(),
                    "route_details": $("#route_details").val(),
                    "goods_type": $("#goods_type").val(),
                    "device": $("#device").val(),
                    "expected_delivery": $("#expected_delivery").val(),
                    "po_number": $("#po_number").val(),
                    "delivery_number": $("#delivery_number").val(),
                    "ndc_number": $("#ndc_number").val(),
                    "batch_id": $("#batch_id").val(),
                    "serial_number": $("#serial_number").val(),
                    "shipment_description": $("#shipment_description").val(),
                }),
            })
                .then(response => {
                    if (response.status === 200) {
                        return response.json();
                    } else if (response.status === 401) {
                        // Token unauthorized or expired, redirect to login page
                        console.log("Token unauthorized or expired. Redirecting to login page.");
                        window.location.href = "/login";
                        // Returning a rejected promise to skip the next then block
                        return Promise.reject("Unauthorized");
                    } else {
                        $("#error-message").text("Please Enter the empty fields");
                        $("#error-message").css("visibility", "visible");
                    }
                })
                .then(jsonresponse => {
                    console.log("API Response:", jsonresponse);
                
                    // Check if the response contains an error message
                    if (jsonresponse.error_message) {
                        throw new Error(jsonresponse.error_message);
                    }
                })
                .catch(error => {

                    if (error === "Unauthorized" || error.message === "Token has expired") {
                        // Perform logout or additional actions here
                        console.log("Token is expired. Logging out...");
                        // You might want to clear the local storage or perform other logout actions
                        // localStorage.clear();
                        window.location.href = "/login"; // Redirect to logout page
                        return; // Skip displaying error messages
                    }
                
                    // Handle other errors
                    console.log("Error:", error.message);
                
                    // Display the error message
                    $("#error").text(error.message);
                    $("#error").css("visibility", "visible");
                });
        } else {
            // Token is missing or expired, redirect to login page
            console.log("Token is missing or expired, redirecting to login page");
            window.location.href = "/login";
        }
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