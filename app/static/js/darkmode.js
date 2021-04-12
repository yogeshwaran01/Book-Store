var element = document.getElementById('dark')
element.addEventListener('click', switcher);
element.dataset.clicked = "1"

function darkMode() {
    var element = document.body;
    element.classList.toggle("dark-mode");
    var ele = document.getElementsByClassName('card')
    var eles = document.getElementsByClassName('card-text')
    var art = document.getElementsByClassName('article')

    for(i=0; i<ele.length; i++){
        ele[i].classList.toggle("card-dark")
    }
    for(i=0; i<eles.length; i++){
        eles[i].classList.toggle("card-text-dark")
    }
    for(i=0; i<art.length; i++){
        art[i].classList.remove("article")
        art[i].classList.toggle("lighter")
    }
    var d = document.getElementsByClassName('card-footer')
    if (d.length != 0) {
        for(i=0; i<ele.length; i++){
            d[i].classList.toggle("card-footer-dark")
        }
    }

}

function switcher() {

    var txt = "🌞 Light"
    if(!!this.dataset.clicked) {
        this.dataset.clicked = "";


    } else {
        this.dataset.clicked = "1";
        txt = "🌙 Dark";
    }
    this.innerHTML = txt;

}
