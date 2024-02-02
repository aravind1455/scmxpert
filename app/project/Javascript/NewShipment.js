
if (localStorage.getItem("access_token") === null) {
    window.location.href= "/login";
}

$(document).ready(function(){
    if (sessionStorage.getItem("role")==="admin"){
        $("#update").css("display","flex");
        $("#update1").css("display","flex");
    }
});

document.addEventListener("DOMContentLoaded", function () {
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0');
    var yyyy = today.getFullYear();

    today = yyyy + '-' + mm + '-' + dd;
    document.getElementById('expected_delivery').min = today;
});

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("submit").addEventListener("click", function (event) {
        event.preventDefault();

        const token = localStorage.getItem("access_token");

        function isTokenExpired() {
            const tokenExpiration = localStorage.getItem("access_token");
            if (!tokenExpiration) {
                return true;
            }

            const expirationTime = new Date(tokenExpiration).getTime();
            const currentTime = new Date().getTime();

            return currentTime > expirationTime;
        }

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
                } else {
                    throw new Error(response.status);
                }
            })
            .then(jsonresponse => {
                if (jsonresponse.error_message) {
                    throw new Error(jsonresponse.error_message);
                }
            })
            .catch(error => {
                if (error === "Unauthorized" || error.message === "Token has expired") {
                    console.log("Token is expired. Logging out...");
                    alert("Unauthorized access. Redirecting to login...");
                    window.location.href = "/login";
                    return;
                }

                console.log("Error:", error.message);
                $("#error").text(error.message);
                $("#error").css("visibility", "visible");
                setTimeout(function () {
                    $("#error").text("");
                }, 2000);
            });
        } else {
            console.log("Token is missing or expired, redirecting to login page");
            alert("Unauthorized access. Redirecting to login...");
            window.location.href = "/login";
        }
    });
});

function logout() {
    localStorage.removeItem("access_token");
    sessionStorage.removeItem("username");
    sessionStorage.removeItem("email");
    sessionStorage.removeItem("role");
    window.location.href= "/";
}
