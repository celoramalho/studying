//Chalenges
function sayHello() {
    console.log('Hello World');
}
;
function sayHelloWithName(name) {
    console.log(`Hello ${name}`);
}


function double(number) {
    return number * 2;
}

sayHello();

let name = "Marcelo";
sayHelloWithName(name);

let number = 5;
console.log(double(number));

let numero1 = 35;
let numero2 = 27;
let numero3 = 22;

function calcula_media(num1, num2, num3) {
    return (num1 + num2 + num3) / 3;
}

console.log(calcula_media(numero1, numero2, numero3));


let numero4 = 82;
let numero5 = 137;

function retorna_maior(num1, num2) {
    if (num1 > num2) {
        return num1;
    }
    else {
        return num2;
    }
}
console.log(retorna_maior(numero4, numero5));

let numero6= 13;

function quadrado_do_numero(num) {
    return num * num;
}
console.log(quadrado_do_numero(numero6));