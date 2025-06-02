function RedirectToPayed(var1,idOrder){
    var form = document.forms[var1];
    form.action = "/Payed";
    form.method = "POST";
    document.getElementById("idOrder").value = idOrder;
    form.submit();
}

function RedirectToRenewSub(var1,idSub){
    var form = document.forms[var1];
    form.action = "/RenewSub";
    form.method = "POST";
    document.getElementById("idSub").value = idSub;
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


    // Check the if the offerID does actually exist : 
    axios.post('/CheckOfferID', {
        offerID : offerId
    })
    .then((response) => {
        if (response.data.offerID_exist == "false") {
            document.getElementById("ErrorMSG3").innerHTML = "We couldn't find any offer with the provided ID. Please double-check the ID and try again.";
            document.getElementById("ErrorMSG3").style.display = "block";

        } else {
            document.getElementById("ErrorMSG3").style.display = "none";
            document.forms["ModifyOffersForm"].submit();
        }
    })
    .catch((error) => {
        console.log(error);
    });

    return false;



    
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





function VerifyAddOffer(formName){
    //Get data :
    var name = document.forms[formName]["name"].value;
    var offerPrice = document.forms[formName]["Offer_price"].value;
    var duration = document.forms[formName]["duration"].value;
    var description = document.forms[formName]["description"].value;
    // Check if any field is empty : 
    if (!name || !offerPrice || !duration || !description) {
        document.getElementById("ErrorMSG1").innerHTML = "Please fill all fields ";
        document.getElementById("ErrorMSG1").style.display = "block";
        return false; 
    }

    // Check if the price and duration is numbers
    if (isNaN(offerPrice) || isNaN(duration))
    {
        document.getElementById("ErrorMSG1").innerHTML = "Offer_price and Duration must be numeric values";
        document.getElementById("ErrorMSG1").style.display = "block";
        return false; 
    }
    
    // Check the name of the offer if it does actually exist : 
    axios.post('/CheckOfferName', {
        name : name
    })
    .then((response) => {
        if (response.data.name_exist == "true") {
            document.getElementById("ErrorMSG1").innerHTML = "Sorry, the product name you provided is already in use. Please consider choosing a different name for your offer.";
            document.getElementById("ErrorMSG1").style.display = "block";

        } else {
            document.getElementById("ErrorMSG1").style.display = "none";
            document.forms["AddOffersForm"].submit();
        }
    })
    .catch((error) => {
        console.log(error);
    });

    return false;

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

    // Check the if the offerID does actually exist : 
    axios.post('/CheckOfferID', {
        offerID : offerId
    })
    .then((response) => {
        if (response.data.offerID_exist == "false") {
            document.getElementById("ErrorMSG2").innerHTML = "We couldn't find any offer with the provided ID. Please double-check the ID and try again.";
            document.getElementById("ErrorMSG2").style.display = "block";

        } else {
            document.getElementById("ErrorMSG2").style.display = "none";
            var result = confirm("Are you sure you want to delete the offer with the following ID ?\n\nOffer ID: " + offerId);
            if(result){
                document.forms["RemoveOfferForm"].submit();
            }
        }
    })
    .catch((error) => {
        console.log(error);
    });

    return false;

    

}

function ConfirmUSERRemoval(){
    var UserID = document.forms["RemoveUSERForm"]["UserID"].value;
    if (UserID == ''){
        document.getElementById("ErrorMSGDeletUSR").innerHTML = "Please Fill UserID field";
        document.getElementById("ErrorMSGDeletUSR").style.display = "block";
        return false;
    }

    
    if (isNaN(UserID)){
        document.getElementById("ErrorMSGDeletUSR").innerHTML = "The value of UserID should be a number";
        document.getElementById("ErrorMSGDeletUSR").style.display = "block";
        return false;
    }

    // Check the if the UserID does actually exist : 
    axios.post('/CheckUserID', {
        UserID : UserID
    })
    .then((response) => {
        if (response.data.UserID_exist == "false") {
            document.getElementById("ErrorMSGDeletUSR").innerHTML = "We couldn't find any User with the provided ID. Please double-check the ID and try again.";
            document.getElementById("ErrorMSGDeletUSR").style.display = "block";

        } else {
            if(response.data.UserID_exist == "admin")
            {
                document.getElementById("ErrorMSGDeletUSR").innerHTML = "Apologies, it seems you're trying to delete an admin account. This action is restricted for security reasons.";
                document.getElementById("ErrorMSGDeletUSR").style.display = "block";
            }
            else{
                document.getElementById("ErrorMSGDeletUSR").style.display = "none";
                var result = confirm("Are you sure you want to delete the offer with the following ID ?\n\nOffer ID: " + UserID);
                if(result){
                    document.forms["RemoveUSERForm"].submit();
                }
            }

        }
    })
    .catch((error) => {
        console.log(error);
    });

    return false;

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


    if (!selectedRole || selectedRole === 'Please Select a role :' || email_UserId == '') {
        document.getElementById("ErrorMSG").innerHTML = " Please fill all fields ";
        document.getElementById("ErrorMSG").style.display = "block";
        return false;
    } else {



    // Check the if the UserID does actually exist : 
    axios.post('/CheckUserID', {
        UserID : email_UserId 
    })
    .then((response) => {
        if (response.data.UserID_exist == "false") {
            document.getElementById("ErrorMSG").innerHTML = "We couldn't find any User with the provided ID. Please double-check the ID and try again.";
            document.getElementById("ErrorMSG").style.display = "block";

        } else {
            if(response.data.UserID_exist == "admin")
            {
                document.getElementById("ErrorMSG").innerHTML = "Apologies, it seems you're trying to Change the role of an admin account. This action is restricted for security reasons.";
                document.getElementById("ErrorMSG").style.display = "block";
            }
            else{
                document.getElementById("ErrorMSG").style.display = "none";
                var result = confirm("Are you sure you want to change the USR role to " + selectedRole);
                if (result) {
                    document.forms[formName].submit();
                }
            }

        }
    })
    .catch((error) => {
        console.log(error);
    });


        

    }
    return false;
}



function confirmSubOperation(){
    var result = confirm("Are you sure you want to remove this subscription? This action cannot be undone and will terminate your access to the associated services");
    if(result){
        return true;
    }
    else{
        return false;
    }
}