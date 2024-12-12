document.getElementById("registration-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting

    // Collect form data
    const name = document.getElementById("name").value;
    const mobile = document.getElementById("mobile").value;
    const aadhar = document.getElementById("aadhar").value;

    console.log("User Registered:", { name, mobile, aadhar });
    alert("Registration Successful!");

    // You can add code here to send the data to a backend server
});
