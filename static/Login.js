function passwordForgotActionChange(){
    var form = document.forms["LoginForm"];
    form.action = "/passwordForgot";
    form.submit();
}
function ReturnToLoginActionChange(){
    var form = document.forms["ResetPassword"];
    form.action = "/Login";
    form.method = "GET";
    form.submit();
}

function validateForm(){
    // Check email validation :
    var Email = document.forms["LoginForm"]["email"].value;
    var Password  = document.forms["LoginForm"]["password"].value;


    if (Email == "" || Password == "") {
        document.getElementById("errorMsg").innerHTML = "Please enter your email and password";
        document.getElementById("errorMsg").style.display = "block";
        return false;
    }

    const emailPattern = /^[A-Za-z0-9_\-\.]+\@[A-Za-z0-9_\-\.]+\.[A-Za-z]{2,4}$/ ;
    // match is not working because emailPattern is not a string it's a regex
    if (!emailPattern.test(Email)){
        // NOT A VALID EMAIL :
        document.getElementById("errorMsg").innerHTML = "Please enter a valid email address";
        document.getElementById("errorMsg").style.display = "block";
        return false;
    }

    axios.post('/CheckLogin', {
        email: Email,
        passwd: Password
    })
    .then((response) => {
        if (response.data.usr_exist == "true") {
            alert("User exists");
            document.forms["SignupForm"].submit();

        } else {
            alert("User doesn't exist");
            document.getElementById("errorMsg").innerHTML = "Sorry, looks like that's the wrong email or password.";
            document.getElementById("errorMsg").style.display = "block";
        }
    })
    .catch((error) => {
        console.log(error);
    });

    return false;
}