function calculateShipping() {
    // Fetch user inputs
    const destination = document.getElementById('destination').value;
    const weight = parseFloat(document.getElementById('weight').value);
    const km = document.getElementById('km').value;
    const deliverySpeed = document.getElementById('deliverySpeed').value;
  
    // Perform shipping rate calculation (replace this with your actual calculation logic)
    const shippingRate = calculateRate(weight,deliverySpeed,km);
  
    // Display the result to the user
    const resultContainer = document.getElementById('result');
    resultContainer.innerHTML = `<p>Shipping to :${destination}</p><p>Estimated Shipping Rate: $${shippingRate.toFixed(2)}</p>`;
  }
  
  function calculateRate(weight,deliverySpeed,km) {
    // Replace this with your actual shipping rate calculation logic
    // For simplicity, let's say the rate is $0.5 per kg plus $1 for expedited and $2 for express
    let baseRate = 0.5 * weight;
    let distance = 1*km
    let speedRate = (deliverySpeed === 'expedited') ? 1 : (deliverySpeed === 'express') ? 2 : 0;
  
    return baseRate + speedRate+distance;
  }
  