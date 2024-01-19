if (localStorage.getItem("access_token") === null) {
    window.location.href= "/login";
}

$(document).ready(function () {
  const token = localStorage.getItem("access_token");

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
                  throw new Error(`Status ${response.status}`);
              }
              return response.json();
          })
          .then(response => {
              console.log(response);
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
          })
          .catch(error => {
              console.log("Error:", error.message);
          });
  });
});



// Check if the script has already been executed
if (!sessionStorage.getItem("scriptExecuted")) {
  $(document).ready(function() {
    console.log("Document ready");
    console.log("Role from sessionStorage:", sessionStorage.getItem("role"));

    if (sessionStorage.getItem("role") === "admin") {
      console.log("Redirecting to /devicedata");
      window.location.href = "/devicedata";
    } else {
      console.log("Redirecting to /adminpage");
      window.location.href = "/adminpage";
    }

    // Set the flag to indicate that the script has been executed
    sessionStorage.setItem("scriptExecuted", true);
  });
}




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
  sessionStorage.removeItem("username");
  sessionStorage.removeItem("email");
  sessionStorage.removeItem("role");
  window.location.href= "/login";
  // You can add more cleanup here if needed
}