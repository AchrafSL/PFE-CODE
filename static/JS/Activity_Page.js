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

function ConfirmOfferModification(){
    var offerId = document.forms["ModifyOffersForm"]["offerID"].value;
    if (isNaN(offerId)){
        document.getElementById("ErrorMSG3").innerHTML = "The value of OfferId should be a number";
        document.getElementById("ErrorMSG3").style.display = "block";
        return false;
    }
    if (offerId == ''){
        document.getElementById("ErrorMSG3").innerHTML = "Please Fill OfferID field ";
        document.getElementById("ErrorMSG3").style.display = "block";
        return false;
    }
    
}

function VerifyOfferModifying(formName){
    //Get data :
    var name = document.forms[formName]["name"].value;
    var offerPrice = document.forms[formName]["Offer_price"].value;
    var duration = document.forms[formName]["duration"].value;
    var description = document.forms[formName]["description"].value;

    // Check if any field is empty : 
    if (!name || !offerPrice || !duration || !description) {
        document.getElementById("ErrorMSG4").innerHTML = "Please fill all fields ";
        document.getElementById("ErrorMSG4").style.display = "block";
        return false; 
    }

    // Check if the price and duration is numbers
    if (isNaN(offerPrice) || isNaN(duration))
    {
        document.getElementById("ErrorMSG4").innerHTML = "Offer_price and Duration must be numeric values";
        document.getElementById("ErrorMSG4").style.display = "block";
        return false; 
    }


}





function ConfirmOfferRemoval(){
    var offerId = document.forms["RemoveOfferForm"]["offerID"].value;
    if (offerId == ''){
        document.getElementById("ErrorMSG2").innerHTML = "TPlease Fill OfferID field";
        document.getElementById("ErrorMSG2").style.display = "block";
        return false;
    }
    if (isNaN(offerId)){
        document.getElementById("ErrorMSG2").innerHTML = "The value of OfferId should be a number";
        document.getElementById("ErrorMSG2").style.display = "block";
        return false;
    }
    else{
        document.getElementById("ErrorMSG2").style.display = "none";
        var result = confirm("Are you sure you want to delete the offer with the following ID ?\n\nOffer ID: " + offerId);
        if(result){
            return true;
        }
        else{
            return false;
        }
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
