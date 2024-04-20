function redirectDelete(variable2)
{
    var form = document.forms[variable2];
    form.action = "/DeleteAccount";
    form.method = "POST";
    form.submit();
}