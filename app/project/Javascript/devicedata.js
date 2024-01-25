if (localStorage.getItem("access_token") === null) {
    window.location.href= "/login";
}
document.addEventListener('DOMContentLoaded', function () {
    // Clear the scriptExecuted flag when the page is loaded
    // sessionStorage.removeItem('scriptExecuted');

    if (!sessionStorage.getItem('scriptExecuted')) {
        console.log('Document ready');
        console.log('Role from sessionStorage:', sessionStorage.getItem('role'));

        // Check if the scriptExecuted flag is not set
        if (!sessionStorage.getItem('scriptExecuted')) {
            if (sessionStorage.getItem('role') === 'admin') {
                console.log('Redirecting to /devicedata');
                window.location.href = '/devicedata';
            } else {
                console.log('Redirecting to /adminpage');
                window.location.href = '/adminpage';
            }

            // Set the flag to indicate that the script has been executed
            sessionStorage.setItem('scriptExecuted', true);
        }
    }
});




$(document).ready(function () {
    const token = localStorage.getItem("access_token");

    function redirectToLogin() {
        console.log("Redirecting to login page");
        window.location.href = "/login"; // Change "/login" to the actual login page URL
    }

    $("#submit").on("click", function (event) {
        event.preventDefault();
        const selectedDeviceId = $("#device_id").val();

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
                    // Token unauthorized or expired, redirect to login page
                    console.log("Token unauthorized or expired. Redirecting to login page.");
                    window.location.href = "/login";
                } else {
                    throw new Error(`Status ${response.status}`);
                }
            }
        
            return response.json();
        })
        .then(response => {
            console.log(response); // Log the entire response to the console
        
            if (response.status_code === 400) {
                // Include details from the response in the error message
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
        
                // Update HTML once after the loop
                $("#table_data1").html(ship_data);
            } else {
                // Throw an error directly to the catch block
                throw new Error("Invalid data format");
            }
        })
        .catch(error => {
            // Handle the error thrown in the previous block
            console.log("Error:", error.message);
            $("#error").text(error.message);
            setTimeout(function () {
                $("#error").text(""); // Clear the error message
            }, 2000);
    
        });
    });
});


// Select the elements with the class "menuicn" and "navcontainer"
let menuicn = document.querySelector(".menuicn");
let nav = document.querySelector(".navcontainer");

// Add an event listener to the "menuicn" element for click events
menuicn.addEventListener("click", () => {
  // Toggle the "navclose" class on the "navcontainer" element
  // This class likely controls the visibility of a navigation menu
  nav.classList.toggle("navclose");
});

//  $(document).ready(function() {
//     if (sessionStorage.getItem("role") === "user") {
//         window.location.href= "/adminpage";
//     }
//   });
function logout() {
  localStorage.removeItem("access_token");
  // sessionStorage.removeItem("username");
  // sessionStorage.removeItem("email");
  // sessionStorage.removeItem("role");
  sessionStorage.clear();
  window.location.href= "/login";
  // You can add more cleanup here if needed
}