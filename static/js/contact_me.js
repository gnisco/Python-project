function sendMail(contact_form) {
    emailjs.send("gmail", "contact_form", {
        "from_name": contact_form.name.value,
        "from_email": contact_form.emailaddress.value,
        "enquiry": contact_form.enquirysummary.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response, contact_form.name.value = "", contact_form.emailaddress.value = "", contact_form.enquirysummary.value = "", alert("Your email has been sent"));
        },
        function(error) {
            console.log("FAILED", error, contact_form.name.value = "", contact_form.emailaddress.value = "", contact_form.enquirysummary.value = "", alert("There was an error please try again"));
        }
    );
    return false;
}