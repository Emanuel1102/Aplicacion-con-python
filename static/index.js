let showRegister = ()=>{
    let input = document.querySelector("#contraseña-register")
    if (input.type==="password") {
        input.type="text"
    }else{
        input.type="password"
    }
}

let showLogin = ()=>{
    let input = document.querySelector("#contraseña-login")
    if (input.type==="password") {
        input.type="text"
    }else{
        input.type="password"
    }
}