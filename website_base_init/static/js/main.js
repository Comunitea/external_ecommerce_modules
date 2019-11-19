$(document).ready(function(){
    /*
        Open sub-menu with hover action
    */
    $('#top_menu li.dropdown').hover(function(){
        $(this).addClass('open');
        $(this).find('a.dropdown-toggle').attr('aria-expanded', 'true');
    }, function(){
        $(this).find('a.dropdown-toggle').attr('aria-expanded', 'false');
        $(this).removeClass('open');
    });
});
