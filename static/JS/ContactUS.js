function ConstactUSFormVerif(){
    var ContactUSName = document.forms["ContactUSForm"]["ContactUSName"].value;
    var ContactUSEmail = document.forms["ContactUSForm"]["ContactUSEmail"].value;
    var ContactUSMSG = document.forms["ContactUSForm"]["ContactUSMSG"].value;

    
    if (ContactUSName == "" ||ContactUSEmail == "" || ContactUSMSG == "") {
        document.getElementById("errorMsg").innerHTML = "Please fill in all fields.";
        document.getElementById("errorMsg").style.display = "block";
        return false;
    }
    const emailPattern = /^[A-Za-z0-9_\-\.]+\@[A-Za-z0-9_\-\.]+\.[A-Za-z]{2,4}$/ ;
    // match is not working because emailPattern is not a string it's a regex
    if (!emailPattern.test(ContactUSEmail)){
        // NOT A VALID EMAIL :
        document.getElementById("errorMsg").innerHTML = "Please enter a valid email address";
        document.getElementById("errorMsg").style.display = "block";
        return false;
    }
    else{
        document.getElementById("errorMsg").style.display = "none";
        return true;
    }

}