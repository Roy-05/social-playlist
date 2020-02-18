const path = window.location.pathname;

//Display the appropiate navbar options on each page
//For example, we don't want logout as an option on the login, signup page. 
if (path === '/') {
    //original
    // $('.navbar').addClass("hidden");

    $('.navbar').addClass("active");
}
else if(path === '/signup') {
    //original
    $('#nav-logout').addClass("hidden");
    $('#nav-signup').addClass("active");

    // $('#nav-logout').addClass("active");
    // $('#nav-signup').addClass("hidden");
    $('#nav-remove_song').addClass("hidden");
}
else if(path === '/login') {
    //original
    $('#nav-logout').addClass("hidden");
    $('#nav-login').addClass("active");

    // $('.navbar').addClass("hidden");
    // $('#nav-logout').addClass("hidden");
    // $('#nav-signup').addClass("hidden");
    $('#nav-remove_song').addClass("hidden");
}
else if(path === '/playlist') {
    //original
    $('#nav-signup').addClass("hidden");
    $('#nav-login').addClass("hidden");

    // $('#nav-signup').addClass("active"); //why are these changes not working?
    // $('#nav-login').addClass("active");
    $('#nav-remove_song').addClass("active");
}
//added by me to test, doesn't work for some reason
else if(path === '/add_song') {
    //original
    $('#nav-signup').addClass("hidden");
    $('#nav-login').addClass("hidden");

    // $('#nav-signup').addClass("active"); //why are these changes not working?
    // $('#nav-login').addClass("active");
    // $('#nav-remove_song').addClass("active");
}

else if(path === '/logout') {
    //no -op
}