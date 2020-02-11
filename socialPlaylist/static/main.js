const path = window.location.pathname;

//Display the appropiate navbar options on each page
//For example, we don't want logout as an option on the login, signup page. 
if (path === '/') {
    $('.navbar').addClass("hidden");
}
else if(path === '/signup') {
    $('#nav-logout').addClass("hidden");
    $('#nav-signup').addClass("active");

}
else if(path === '/login') {
    $('#nav-logout').addClass("hidden");
    $('#nav-login').addClass("active");
}
else if(path === '/playlist') {
    $('#nav-signup').addClass("hidden");
    $('#nav-login').addClass("hidden");
}
else if(path === '/logout') {
    //no -op
}