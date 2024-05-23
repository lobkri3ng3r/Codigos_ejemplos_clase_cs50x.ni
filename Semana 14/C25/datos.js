var nombre = "Michael Mejia";
var edad = 20;

var concatenar = nombre + "  " + edad;


let datos = document.getElementById("datos");
datos.innerHTML = `
    <h1>ESTO ES UN CONTENEDOR DE DATOS</h1>
    <h2>Mi nombre es ${nombre}</h2>
    <h2>Tengo la edad de ${edad} anios</h2>

`;

let info = document.getElementById("ndatos");

function validar(){


    let texto = "ESTO ES EL RESULTADO";
    let f = document.getElementById("nah");
    f.innerHTML = texto;

    if(edad >= 18){
        info.innerHTML = `
        <h1>Eres mayor de edad, ya vas preso!!!</h1>
        `;
    }else{
        info.innerHTML = `
        <h1>Eres menor de edad, puedes mandar preso a alguien!!!</h1>
        `;
    }
}

