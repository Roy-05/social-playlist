const nav = document.getElementsByClassName('navbar')[0],
    signup = document.getElementById('nav-signup'),
    login = document.getElementById('nav-login'),
    logout = document.getElementById('nav-logout'),
    path = window.location.pathname;

//Display the appropiate navbar options on each page
//For example, we don't want logout as an option on the login, signup page. 
if (path === '/') {
    $(nav).addClass("hidden");
}
else if(path === '/signup') {
    $(logout).addClass("hidden");
    $(signup).addClass("active");

}
else if(path === '/login') {
    $(logout).addClass("hidden");
    $(login).addClass("active");
}
else if(path === '/playlist') {
    $(signup).addClass("hidden");
    $(login).addClass("hidden");
}
else if(path === '/logout') {
    //no -op
}