function sendEmail(){

    var templateParams = {
        from_name: document.getElementById("name").value,
        email_id: document.getElementById("email").value,
        message: document.getElementById("message").value,
    };    

    emailjs.send("service_7uxqkgs","template_uqyayx3",templateParams)
        .then(function (res) {
            document.getElementById("name").value = "";
            document.getElementById("email").value = "";
            document.getElementById("message").value = "";
            alert(" Your email was sent successfully" + res.text);
        })
}

