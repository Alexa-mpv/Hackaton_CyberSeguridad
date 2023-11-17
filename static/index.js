

const buttonA = document.querySelector("#SendMessageBtn");
const input = document.querySelector("#UserInput");


buttonA.onclick = () => {
  alert(input.value);
  createJSON();
};

function createJSON() {
  const dict_values = {"ChatGPT":input.value};
  console.log(dict_values);
  const str = JSON.stringify(dict_values);
  console.log(str);
  $.ajax({
    url:"/test",
    type:"POST",
    contentType:"application/json",
    data: JSON.stringify(str)
    
    
    //success: function(response) {
    //  console.log("Success:", response);
    //},
    //error: function(error) {
    //  console.error("Error:", error);
    //}
  }).then(function (response) { // At this point, Flask has printed our JSON
    return response.text();
  }).then(function (text) {

    console.log('POST response: ');

    // Should be 'OK' if everything was successful
    console.log(text);
  });;
}

  fetch('/test')
      .then(function (response) {
          return response.text();
      }).then(function (text) {
          console.log('GET response text:');
          console.log(text); // Print the greeting as text
      });

function createJSON1() {
  
  fetch('/test', {

    // Declare what type of data we're sending
    headers: {
      'Content-Type': 'application/json'
    },

    // Specify the method
    method: 'POST',

    // A JSON payload
    body: JSON.stringify({
        "greeting": "Hello from the browser!"
    })
  }).then(function (response) { // At this point, Flask has printed our JSON
    return response.text();
  }).then(function (text) {

    console.log('POST response: ');

    // Should be 'OK' if everything was successful
    console.log(text);
  });
}

document.body.addEventListener("keypress", function(event) {
  console.log("si entro");
  if (event.key === "Enter") {
    event.preventDefault();
    document.getElementById("SendMessageBtn").click();
  }
});