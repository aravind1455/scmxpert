if (localStorage.getItem("access_token") === null) {
    window.location.href= "/login";
}

$(document).ready(function(){
    const token = localStorage.getItem("access_token");

    function redirectToLogin() {
        window.location.href = "/login";
    }

    // Check if token exists and not expired
    if (token) {
        fetch(`/shipment`, {
            method: "GET",
            headers: {
                "Authorization": `${localStorage.getItem("access_token")}`,
                'Content-Type': 'application/json',
            },
        })
        .then(response => {
            if (response.status === 401) {
                alert("Unauthorized access. Redirecting to login...");
                redirectToLogin();
                return Promise.reject("Unauthorized");
            }

            if (response.status !== 200) {
                throw new Error(`Status ${response.status}`);
            }
            return response.json();
        })
        .then(response => {
            if (response.status_code === 400) {
                $("#error").text(response.detail);
            }

            let shipment_data = "";
            for (let shipment_no = 0; shipment_no < response.length; shipment_no++) {
                // Access the current shipment in the loop
                const shipment = response[shipment_no];
                shipment_data = shipment_data + "<tr><td>"
                    + shipment.user + "</td><td>"
                    + shipment.shipment_number + "</td><td>"
                    + shipment.container_number + "</td><td>"
                    + shipment.route_details + "</td><td>"
                    + shipment.goods_type + "</td><td>"
                    + shipment.device + "</td><td>"
                    + shipment.expected_delivery + "</td><td>"
                    + shipment.po_number + "</td><td>"
                    + shipment.delivery_number + "</td><td>"
                    + shipment.ndc_number + "</td><td>"
                    + shipment.batch_id + "</td><td>"
                    + shipment.serial_number + "</td><td>"
                    + shipment.shipment_description + "</td></tr>";
            }

            $("#table_data").html(shipment_data);

            // Add event listener for search button
            $("#searchButton").click(function() {
                const username = $("#usernameInput").val().trim();
                if (username !== "") {
                    // Perform search based on username
                    //It takes each item from the response array and checks if the user property of that item matches the username variable.
                    const filteredData = response.filter(item => item.user === username);
                    if (filteredData.length > 0) {
                        // Display filtered data
                        let filteredHtml = "";
                        filteredData.forEach(item => {
                            filteredHtml += "<tr><td>"
                                + item.user + "</td><td>"
                                + item.shipment_number + "</td><td>"
                                + item.container_number + "</td><td>"
                                + item.route_details + "</td><td>"
                                + item.goods_type + "</td><td>"
                                + item.device + "</td><td>"
                                + item.expected_delivery + "</td><td>"
                                + item.po_number + "</td><td>"
                                + item.delivery_number + "</td><td>"
                                + item.ndc_number + "</td><td>"
                                + item.batch_id + "</td><td>"
                                + item.serial_number + "</td><td>"
                                + item.shipment_description + "</td></tr>";
                        });
                        $("#table_data").html(filteredHtml);
                    } else {
                        $("#error").text("No shipments found ");
                        setTimeout(function () {
                            $("#error").text("");
                        }, 2000);
                    }
                } else {
                    $("#error").text("Please enter a username");
                    setTimeout(function () {
                        $("#error").text("");
                    }, 2000);
                    
                }
            });
        })
        .catch(error => {
            $("#error").text(error.message);
            // $("#error").css("visibility", "visible");
            setTimeout(function () {
                $("#error").text("");
            }, 2000);
        });
    } else {
        console.log("Token is missing, redirecting to login page");
        alert("Unauthorized access. Redirecting to login...");
        redirectToLogin();
    }
});

$(document).ready(function() {
    if (sessionStorage.getItem('role') === "admin") {
        $("#adminvis").css("display", "block");
    }
})

function logout() {
    localStorage.removeItem("access_token");
    sessionStorage.removeItem("username");
    sessionStorage.removeItem("email");
    sessionStorage.removeItem("role");
    window.location.href= "/";
}