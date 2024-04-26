function redirectToProduct(variable2,productId){
    var form = document.forms[variable2];
    document.getElementById("productId").value = productId;

    form.submit();
}
