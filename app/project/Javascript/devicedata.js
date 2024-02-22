if (localStorage.getItem("access_token") === null) {
    window.location.href = "/login";
}

$(document).ready(function () {
    if (sessionStorage.getItem("role") === "admin") {
        $("#update").css("display", "flex");
        $("#update1").css("display", "flex");
    }
});

document.addEventListener('DOMContentLoaded', function () {
    if (sessionStorage.getItem('role') !== 'admin') {
        console.log('Redirecting to /adminpage');
        window.location.href = '/adminpage';
    }
});
// Fetch device data on button click
$(document).ready(function () {
    $("#submit").on("click", function (event) {
        event.preventDefault();
        const selectedDeviceId = $("#device_id").val();
 // Make a POST request to '/devicedatafirst'
        fetch("/devicedatafirst", {
            method: "POST",
            headers: {
                "Authorization": `${localStorage.getItem("access_token")}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                Device_ID: selectedDeviceId
            }),
        })
            .then(response => {
                if (!response.ok) {
                    if (response.status === 401) {
                        console.log("Token unauthorized or expired. Redirecting to login page.");
                        alert("Unauthorized access. Redirecting to login...");
                        window.location.href = "/login";
                    } else {
                        throw new Error(`Status ${response.status}`);
                    }
                }
                return response.json();
            })
             // Construct HTML table rows based on the device data
            .then(response => {
                console.log(response);

                if (response.status_code === 400) {
                    throw new Error(` ${response.detail}`);
                }

                if (response.data && Array.isArray(response.data)) {
                    let ship_data = "";

                    for (let shipment_no = 0; shipment_no < response.data.length; shipment_no++) {
                        const shipment = response.data[shipment_no];

                        ship_data += "<tr><td>" +
                            shipment.Device_ID + "</td><td>" +
                            shipment.Battery_Level + "</td><td>" +
                            shipment.First_Sensor_temperature + "</td><td>" +
                            shipment.Route_From + "</td><td>" +
                            shipment.Route_To + "</td></tr>";
                    }
                    $("#table_data1").html(ship_data);
                } else {
                    throw new Error("Invalid data format");
                    // $("#error").text("Invalid data format");
                }
            })
            .catch(error => {
                console.log("Error:", error.message);
                $("#error").text(error.message);
                $("#error").css("visibility", "visible");
                setTimeout(function () {
                    $("#error").text("");
                }, 2000);
            });
    });
});


let menuicn = document.querySelector(".menuicn");
let nav = document.querySelector(".navcontainer");

menuicn.addEventListener("click", () => {
    nav.classList.toggle("navclose");
});
// Function to handle user logout
function logout() {
    localStorage.removeItem("access_token");
    sessionStorage.clear();
    window.location.href = "/";
}
