function passwordForgotActionChange(){
    var form = document.forms["LoginForm"];
    form.action = "/passwordForgot";
    form.submit();
}
function ReturnToLoginActionChange(Variable1){
    var form = document.forms[Variable1];
    form.action = "/Login";
    form.method = "POST";
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
            document.forms["LoginForm"].submit();

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

function ValidateResetPWD(){
    var Email = document.forms["ResetPassword"]["E_mail"].value;
    const emailPattern = /^[A-Za-z0-9_\-\.]+\@[A-Za-z0-9_\-\.]+\.[A-Za-z]{2,4}$/ ;
    // match is not working because emailPattern is not a string it's a regex
    if (!emailPattern.test(Email)){
        // NOT A VALID EMAIL :
        document.getElementById("errorMsg").style.display = "block";
        return false;
    }
    return true
}




function validateResetPWDForm(){
    var password = document.forms["reset_form"]["Password"].value;
    var ConfirmPassword  = document.forms["reset_form"]["ConfirmPassword"].value;
    var Email = document.forms["reset_form"]["Email"].value;
    


    if (ConfirmPassword == "" || password == "") {
        document.getElementById("errorMsg").innerHTML = "Please fill in all fields";
        document.getElementById("errorMsg").style.display = "block";
        return false;
    }

    // Test if the password is valid : MSGS
    // 1 " Password requires at least one lowercase character"
    const lowercaseRegex = /(?=.*[a-z]+)/ ;
    if (!lowercaseRegex.test(password)){
        document.getElementById("errorMsg").innerHTML = "Password requires at least one lowercase character";
        document.getElementById("errorMsg").style.display = "block";
        return false;
    }
    // 2 " Password requires at least one uppercase character"
    const uppercaseRegex = /(?=.*[A-Z]+)/ ;
    if (!uppercaseRegex.test(password)){
        document.getElementById("errorMsg").innerHTML = "Password requires at least one uppercase character";
        document.getElementById("errorMsg").style.display = "block";
        return false;
    }
    
    // 3 "Password requires at least one special character "
    const specialCharacterRegex = /(?=.*[#?!@$%^&*-.]+)/ ;
    if (!specialCharacterRegex.test(password)){
        document.getElementById("errorMsg").innerHTML = "Password requires at least one special character";
        document.getElementById("errorMsg").style.display = "block";
        return false;
    }
    
    // 4 "Password requires at least one number "
    const numberRegex = /(?=.*[0-9]+)/ ;
    if (!numberRegex.test(password)){
        document.getElementById("errorMsg").innerHTML = "Password requires at least one number";
        document.getElementById("errorMsg").style.display = "block";
        return false;
    }
    
    // 5 "Password requires 8 characters minimum"
    const minimumRegex = /.{8,}/ ;
    if (!minimumRegex.test(password)){
        document.getElementById("errorMsg").innerHTML = "Password requires 8 characters minimum";
        document.getElementById("errorMsg").style.display = "block";
        return false;
    }
    else 
    {

        if (ConfirmPassword != password) {
            document.getElementById("errorMsg").innerHTML = "Passwords do not match";
            document.getElementById("errorMsg").style.display = "block";
            return false;
        }
    }

    // Check using axios if the new_password is the same as the one in the db if so give an error
    axios.post('/CheckPassword', {
        email: Email,
        passwd: password
    })
    .then((response) => {
        if (response.data.pswd_exist == "false") {
            document.forms["reset_form"].submit();

        } else {
            document.getElementById("errorMsg").innerHTML = "New password matches current password. Please choose a different password.";
            document.getElementById("errorMsg").style.display = "block";
        }
    })
    .catch((error) => {
        console.log(error);
    });

    return false;
}