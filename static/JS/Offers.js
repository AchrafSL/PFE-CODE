function redirectToProduct(variable2,productId){
    var form = document.forms[variable2];
    document.getElementById("productId").value = productId;

    form.submit();
}

/* Chat gpt solution because i didn't know these things */
/*The DOMContentLoaded event is fired when the initial HTML document has been completely loaded
 and parsed, without waiting for stylesheets, images, and subframes to finish loading. */


/* The input event is fired whenever the value of an <input>, <textarea>, or <select>
element changes as a result of user input (e.g., typing, pasting, or deleting text).
The function passed as the second argument is a callback function that will be executed whenever
the input event occurs on the searchInput element. */
document.addEventListener('DOMContentLoaded', function() {
    var searchInput = document.getElementById('search-input');
    var form = document.getElementById('SearchProduct');

    searchInput.addEventListener('input', function() {
        var searchTerm = searchInput.value;
        if (searchTerm == '') {
            form.method = "POST";
            form.submit();
        }
    });

});

