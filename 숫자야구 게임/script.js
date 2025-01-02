const numbers = [];
while(numbers.length < 3) {
    const number = Math.floor(Math.random() * 9) + 1;
    if(numbers.includes(number)) {
        continue;
    }
    numbers.push(number);
}
//console.log(numbers);
let attemps = 9;
const att  = document.getElementById('attempts');
att.innerHTML = `${attemps}`;

function check_numbers() {
    let strike=0;
    let ball=0;
    const number1 = parseInt(document.getElementById('number1').value);
    const number2 = parseInt(document.getElementById('number2').value);
    const number3 = parseInt(document.getElementById('number3').value);
    if(number1 == number2 || number2 == number3 || number3 == number1|| number1 == '' || number2 == ''|| number3==''){
        number1.value = ''; number2.value = ''; number3.value = '';
    } else {
        if(number1 == numbers[0]){
            strike++;
        }else if(numbers.includes(number1)){
            ball++;
        }
        if(number2 == numbers[1]){
            strike++;
        }else if(numbers.includes(number2)){
            ball++;
        }
        if(number3 == numbers[2]){
           strike++;
        }else if(numbers.includes(number3)){
            ball++;
        }
    }
    const container = document.getElementById('results');
    if(strike == 0 && ball == 0){
        container.innerHTML += `<div>${number1}${number2}${number3} : <span class="out">O<span></div>`;
    }else
        container.innerHTML += `<div>${number1}${number2}${number3} : ${strike} <span class="strike">S</span> ${ball} <span class="ball">B</span></div>`;
    if(strike==3){
        const img = document.getElementById('game-result-img');
        img.src="success.png";
        const buttons = document.getElementsByClassName('submit-button');
        for (let i = 0; i < buttons.length; i++) {
            buttons[i].disabled = true;
        }
    }
    attemps--;
    att.innerHTML = `${attemps}`;
    if(attemps == 0) {
        const img = document.getElementById('game-result-img');
        img.src="fail.png";
        const buttons = document.getElementsByClassName('submit-button');
        for (let i = 0; i < buttons.length; i++) {
            buttons[i].disabled = true;
        }
    }
}