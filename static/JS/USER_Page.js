function redirectDelete(variable2)
{
    var form = document.forms[variable2];
    form.action = "/DeleteAccount";
    form.method = "POST";
    form.submit();
}

function redirectLogout(variable2){
    var form = document.forms[variable2];
    form.action = "/logout";
    form.method = "POST";
    form.submit();
}


function handleFileUpload(){
    document.getElementById('uploadForm').submit();
}

function confirmDelete()
{
    var result = confirm("Are you sure you want to delete your account?");
    if(result){
        return true;
    }
    else{
        return false;
    }
}
