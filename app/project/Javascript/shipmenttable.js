if (localStorage.getItem("access_token") === null) {
    window.location.href= "/login";
}

$(document).ready(function(){
    const token = localStorage.getItem("access_token");
    fetch(`/shipment`,{
    method : "GET",
      headers : {
        "Authorization": `${localStorage.getItem("access_token")}`,
        'Content-Type': 'application/json',
      },
    })
    .then(response => {
          if (response.status !== 200) {
            throw new Error(`Status ${response.status}`);
          }
          return response.json();
        }).then(response => {
          console.log(response);
          let shipment_data = "";
          for (let shipment_no = 0; shipment_no < response.length; shipment_no++) {
              const shipment = response[shipment_no];
     
              shipment_data = shipment_data + "<tr><td>"
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
              + shipment.shipment_description + "</td></tr>"
          }
          console.log(shipment_data);
          $("#table_data").html(shipment_data);
          console.log(data);
        }).catch(error => {
          // alert(error.message);
          console.log("data hasn't pushed to html");
        })
      });


function logout() {
    localStorage.removeItem("access_token");
    sessionStorage.removeItem("username");
    sessionStorage.removeItem("email");
    sessionStorage.removeItem("role");
    window.location.href= "/login";
        // You can add more cleanup here if needed
    }
    