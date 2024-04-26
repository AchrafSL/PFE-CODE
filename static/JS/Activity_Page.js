function RedirectToPayed(var1,idOrder){
    var form = document.forms[var1];
    form.action = "/Payed";
    form.method = "POST";
    document.getElementById("idOrder").value = idOrder;
    form.submit();
}
function confirmTreatStatus(){
    var result = confirm("Note: Changing the status to 'Treated' will remove the order from the clients' orders list and retain the same information submitted by the user. Are you sure you want to mark this order as 'Treated'?");
    if(result){
        return true;
    }
    else{
        return false;
    }
}



function confirmRoleChange(formName) {
    var selectedRole = document.getElementsByClassName('Role')[0].value;
    var email_UserId = document.forms[formName]["ChangeRoleInput"].value;

    // if the input is an email check if it's a valid email and show the error msg:
    if (isNaN(email_UserId)) {

        const emailPattern = /^[A-Za-z0-9_\-\.]+\@[A-Za-z0-9_\-\.]+\.[A-Za-z]{2,4}$/ ;
        // match is not working because emailPattern is not a string it's a regex
        if (!emailPattern.test(email_UserId)){
            // NOT A VALID EMAIL :
            document.getElementById("ErrorMSG").innerHTML = "Please enter a valid email address";
            document.getElementById("ErrorMSG").style.display = "block";
            return false;
        }
    }

    if (!selectedRole || selectedRole === 'Please Select a role :') {
        document.getElementById("ErrorMSG").innerHTML = " Please fill all fields ";
        document.getElementById("ErrorMSG").style.display = "block";
        return false;
    } else {
        document.getElementById("ErrorMSG").style.display = "none";
        var result = confirm("Are you sure you want to change the USR role to " + selectedRole);
        if (result) {
            return true;
        } else {
            return false;
        }
    }
}
