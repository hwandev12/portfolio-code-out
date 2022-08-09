// create pop up message for logout

let link3 = document.querySelector("#pop_link")
let exit = document.querySelector(".exit")
let message = document.querySelector(".popup_message")
let header_home = document.querySelector(".masthead")
let content2 = document.querySelector(".main_home")
let main_home = document.body
console.log(main_home)



link3.addEventListener("click", function(e) {
    message.style.transform = "scale(1)"
    message.style.transition = "0.4s all ease"
    header_home.style.backgroundColor = '#444'
    main_home.classList.add("hidden")
    header_home.style.backgroundBlendMode = 'darken'
    content2.style.backgroundColor = '#444'
    content2.style.backgroundBlendMode = 'darken'
    e.stopPropagation();
})
exit.addEventListener("click", function(e) {
    message.style.transform = "scale(0)"
    message.style.transition = "0.4s all ease"
    header_home.style.backgroundColor = '#444'
    main_home.classList.remove("hidden")
    header_home.style.backgroundBlendMode = 'normal'
    content2.style.backgroundColor = 'white'
    content2.style.backgroundBlendMode = 'normal'
    e.stopPropagation();
})

window.onclick = function(event) {
    if (event.target == header_home) {
        message.style.transform = "scale(0)"
        header_home.style.backgroundColor = '#444'
        main_home.classList.remove("hidden")
        header_home.style.backgroundBlendMode = 'normal'
        content2.style.backgroundColor = 'white'
    	content2.style.backgroundBlendMode = 'normal'
        event.stopPropagation();
    }
}
