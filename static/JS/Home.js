document.addEventListener("DOMContentLoaded", function() {
    // Tablaux des images :
    const imgsrc1 = ["static/Images/product_pics/Netflix accounts.jpg","static/Images/product_pics/prime.jpg"
    ,"static/Images/product_pics/Disney+.jpg","static/Images/product_pics/crunchyroll.jpg"
    , "static/Images/product_pics/HBOmax.jpg" ,"static/Images/product_pics/Snapchat+.jpg"]; 
    
    const imgsrc2 = [
        "static/Images/product_pics/duolingo.jpg",
        "static/Images/product_pics/grammarly.png",
        "static/Images/product_pics/Adobe Creative Cloud.png",
        "static/Images/product_pics/canva.jpg"
    ];

    //Tablaux des liens :
    const linksrc1 = [
        "Product_Description?productId=14",  // Netflix accounts
        "Product_Description?productId=16",  // Prime
        "Product_Description?productId=31",  // Disney+
        "Product_Description?productId=18",  // Crunchyroll
        "Product_Description?productId=34",  // HBO Max
        "Product_Description?productId=19"   // Snapchat+
    ];

    const linksrc2 = [
        "Product_Description?productId=23",  // duolingo
        "Product_Description?productId=24",  // grammarly
        "Product_Description?productId=20" ,  // adobe
        "Product_Description?productId=33",  // canva
    ];

    const EntertainmentImg= document.getElementById("EntertainmentImg");
    const EntertainmentLink = document.getElementById("EntertainmentLink");

    const ProductivityImg = document.getElementById("ProductivityImg");
    const ProductivityLink = document.getElementById("ProductivityLink");


    // Changer l'image and imgLink
    var i = 0;
    function changeImage1() {
        //Change EntertainmentImg
        EntertainmentImg.src = imgsrc1[i];
        //Change EntertainmentLink
        EntertainmentLink.href = linksrc1[i];
        i = (i + 1) % (imgsrc1.length);

    }

    var j = 0;
    function changeImage2(){
        //Change ProductivityImg
        ProductivityImg.src = imgsrc2[j];
        //Change ProductivityImgLink
        ProductivityLink.href = linksrc2[j];
        j = (j + 1) % (imgsrc2.length);
    }

    // Appel de changeImage a chaque 3s
    setInterval(changeImage1, 3000);
    setInterval(changeImage2, 3000);

});
