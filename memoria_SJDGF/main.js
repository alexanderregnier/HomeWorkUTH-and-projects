//inicializacion de variables
let tarjetaDestapadas = 0;
let tarejeta1 = null;
let tarejeta2 = null;
let primerResultado = null;
let segundoResultado = null;
let movimientos = 0;
let Aciertos = 0;
let temporizador = false;
let timer = 40;
let tiempoRegresivoId = null;
let timerInicial = 40;

//apuntando documento html
let mostrarMovimientos = document.getElementById('movimientos');
let mostrarAciertos = document.getElementById('Aciertos');
let mostrarTiempo = document.getElementById('t-restante');

//funciones de numeros random
let numeros = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8];
numeros = numeros.sort(()=>{return Math.random()-0.5});
console.log(numeros);

//funciones
function contartiempo(){
    tiempoRegresivoId = setInterval(()=>{
        timer--;
        mostrarTiempo.innerHTML = `Tiempo: ${timer} segundos`;
        if(timer == 0){
            clearInterval(tiempoRegresivoId);
            bloquearTarejrtas();
        }
    },1000);
}

function bloquearTarejrtas(){
    for(let i = 0; i<=15; i++){
        let tarjetaBloqueda = document.getElementById(i);
        tarjetaBloqueda.innerHTML = numeros[i];
        tarjetaBloqueda.disabled = true;
    }
}

//funcion principal
function destapar(id){

    //temporizador
    if(temporizador == false){
        contartiempo();
        temporizador = true;
    }

    tarjetaDestapadas++;
    console.log(tarjetaDestapadas);
    
    if (tarjetaDestapadas == 1){
        //mostrar traejta
        tarejeta1 = document.getElementById(id);
        primerResultado = numeros[id]
        tarejeta1.innerHTML = primerResultado;

        //deshabilitar primer boton
        tarejeta1.disabled = true;
    }else if(tarjetaDestapadas == 2){

        //mostrar seggundo numero
        tarejeta2 = document.getElementById(id);
        segundoResultado = numeros[id];
        tarejeta2.innerHTML = segundoResultado;

        //deshabilitar segundo boton
        tarejeta2.disabled = true;

        //incrementar movimientos
        movimientos++;
        mostrarMovimientos.innerHTML = `movimientos: ${movimientos}`;

        if(primerResultado == segundoResultado){
            //encerrar contador tarjetas destapadas
            tarjetaDestapadas = 0;

            //aumentar aciertos
            Aciertos++;
            mostrarAciertos.innerHTML = `Aciertos: ${Aciertos}`;
        
            if(Aciertos == 8){
                clearInterval(tiempoRegresivoId);
                mostrarAciertos.innerHTML = `Aciertos: ${Aciertos} promedio si`;
                mostrarTiempo.innerHTML = `EL DIABLO MI LOCO ${timerInicial - timer} segndos tan poco?, digo es mucho si eso yo duro eso, primedio `
                mostrarMovimientos.innerHTML = `movimientos: ${movimientos} diablo mi loco que movimientos fueron esos`;
            }
        }else{
            //mostrar momentanemanete los valores
            setTimeout(()=>{
                tarejeta1.innerHTML = ' ';
                tarejeta2.innerHTML = ' ';
                
                tarejeta1.disabled = false;
                tarejeta2.disabled = false;
                
                tarjetaDestapadas = 0;
                
            },800);

        }
    }

}
