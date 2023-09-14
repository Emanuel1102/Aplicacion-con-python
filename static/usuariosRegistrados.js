document.querySelectorAll(".boton-ventana").forEach(function(boton){
    boton.addEventListener("click", function(){
        this.nextElementSibling.showModal()
    })
})

document.querySelectorAll(".ventana button").forEach(function(boton_cerrar){
    boton_cerrar.addEventListener("click", function(){
        this.closest(".ventana").close()
    })
})