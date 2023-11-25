if (document.getElementsByTagName("input")){
    const btn = document.getElementById("sign_up")
    btn.addEventListener( "click", (e) => {
        const inputs = document.getElementsByTagName("input")
        if(inputs[1].value.startsWith(" ") || inputs[2].value.startsWith(" ") || inputs[3].value.startsWith(" ")) {
            e.preventDefault()
        }
    })
}