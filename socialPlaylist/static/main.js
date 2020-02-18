const path = window.location.pathname;

//Display the appropiate navbar options on each page
//For example, we don't want logout as an option on the login, signup page. 
if (path === '/') {
    $('.navbar').addClass("hidden");
}
else if(path === '/signup') {
    $('#nav-logout').addClass("hidden");
    $('#nav-playlist').addClass("hidden");
    $('#nav-add_song').addClass("hidden");
    $('#nav-signup').addClass("active");
}
else if(path === '/login') {
    $('#nav-logout').addClass("hidden");
    $('#nav-playlist').addClass("hidden");
    $('#nav-add_song').addClass("hidden");
    $('#nav-login').addClass("active");
}
//The regex matches all strings of the format: '/playlist/{n}' where n is number b/w 1-99
else if(path === '/playlist' || path.match(/^(\/playlist\/[1-9]|[1-9][0-9]$)/)) {
    $('#nav-signup').addClass("hidden");
    $('#nav-login').addClass("hidden"); 
}
else if(path === '/add_song') {
    $('#nav-signup').addClass("hidden");
    $('#nav-login').addClass("hidden"); 
    $('#nav-add_song').addClass("active");
}
else if(path === '/logout') {
    //no -op
}