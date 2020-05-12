function sendMail(contactForm) {
    emailjs.send("outlook", "contactForm", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "enquiry": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response, contactForm.name.value = "", contactForm.email.value = "", contactForm.message.value = "", alert("Your email has been sent"));
        },
        function(error) {
            console.log("FAILED", error, contactForm.name.value = "", contactForm.email.value = "", contactForm.message.value = "", alert("There was an error please try again"));
        }
    );
    return false;
}

