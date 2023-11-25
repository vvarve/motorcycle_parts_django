document.querySelector("#form_product").style.display = "none";
let register_product = document.getElementById("reg_title")
register_product.style.cursor = "pointer"

register_product.addEventListener( "click", () => {
    if (document.getElementById("form_product").style.display !== "grid"){
        document.getElementById("form_product").style.display = "grid";
    }
    else {
        document.getElementById("form_product").style.display = "none"
    }
})

if (document.getElementById("form_product")) {
    const form_sended = document.getElementById("form_product")
    form_sended.addEventListener( "submit", (e) => {
        const inputs = form_sended.getElementsByTagName("input")
        if (inputs[1].value.startsWith(" ") || inputs[2].value.startsWith(" ") || inputs[3].value.startsWith(" ")){
            e.preventDefault()
        }
    }) 
}

let delete_adv = document.querySelectorAll("#delete")

delete_adv.forEach(event_delete => {
    event_delete.addEventListener( "click", (e) => {
        const event_delete_bool = confirm("Do you want delete this?")
        if (!event_delete_bool) {
            e.preventDefault()
        }
    })
})