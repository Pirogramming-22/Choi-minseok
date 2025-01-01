//TODO1: 버튼을 불러온다 -> 버튼이 클릭 되었는지 확인한다.
//TODO2: 만약 클릭되었다면 숫자를 불러온다. -> 숫자값을 바꿔준다.
const minusButton = document.getElementById('minus_button');
const plusButton = document.getElementById('plus_button');
const counter = document.getElementById('counter');

console.log(counter);

minusButton.addEventListener('click', () => {
    counter.innerText = parseInt(counter.innerText) - 1;
});
plusButton.addEventListener('click', (event) => {
    counter.innerText = parseInt(counter.innerText) + 1;
});