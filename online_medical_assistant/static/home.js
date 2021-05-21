


//Log in / Sing in
// class don't works some time then use the id.

function logid() {
    let login = document.getElementById('login');
    let singin = document.getElementById('singin');
    login.style.display = 'none';
    singin.style.display = 'inline-block';



}

function singid() {
    let singin = document.getElementById('singin');
    let login = document.getElementById('login');
    singin.style.display = 'none';
    login.style.display = 'inline-block';
}




//when onclick is in 'a' then put in link # or link
function prompt() {
    let prompt_display = document.getElementById('prompt');

    prompt_display.style.display = 'block';


}


//some functions not work then try change the name of function
function cose() {
    let prompt_display = document.getElementById('prompt');

    prompt_display.style.display = 'none';

}


// This is menu.


let display = "none";

function drop() {

    //    let navbar = document.getElementById('navbar');


    let menu = document.getElementById('menu');


    let sp1 = document.getElementById('sp1');

    let sp2 = document.getElementById('sp2');

    let sp3 = document.getElementById('sp3');

    let sp4 = document.getElementById('sp4');


    //    let navbar = document.getElementsByClassName('navbar>ul')

    if (display == "none") {
        sp1.style.animation = 'span1 .2s ease-in-out 0s 1 forwards';
        sp4.style.animation = 'span4 .2s ease-in-out 0s 1 forwards';
        sp2.style.animation = 'span2 .2s ease-in-out 0s 1 forwards';
        sp3.style.animation = 'span3 .2s ease-in-out 0s 1 forwards';

        // menu.style.display = "block";
        //    menu.style.transition = 'all .5s ease-in-out 0s';

        display = "block";

           menu.style.animation = 'Darshan .3s ease-in-out 0s 1 forwards'
    }

    else {


        sp1.style.animation = 'rspan1 .2s ease-in-out 0s 1 forwards';
        sp4.style.animation = 'rspan4 .2s ease-in-out 0s 1 forwards';
        sp2.style.animation = 'rspan2 .2s ease-in-out 0s 1 forwards';
        sp3.style.animation = 'rspan3 .2s ease-in-out 0s 1 forwards';

        // menu.style.display = "none";
        display = "none";


           menu.style.animation = 'Darshan1 .3s ease-in-out 0s 1 forwards'


    }
    //    if (menu.style.display != "block") {

    //        menu.style.display = "block";

    //        menu.style.animation = 'Darshan .3s ease-in-out 0s 1 forwards'
    //    }

    //    else {

    //        menu.style.display = 'none';

    //        menu.style.animationDirection = 'reverse'

    //        menu.style.animation = 'Darshan .5s ease-in-out 0s 1 forwards'


    //    }
}




function focus() {


}






