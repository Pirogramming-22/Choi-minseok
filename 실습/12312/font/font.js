// todo: 슬라이더 불러오기 -> 슬라이더가 어디까지 갔는지 인식해야함
// todo: 글자 불러오기 슬라이더 이동 값만큼 글자 굵기 조절

const slider = document.getElementById('text_slider');
const textContainer = document.getElementById('text_container');

const texts = textContainer.children;
console.log(texts);

slider.addEventListener("input", (event) => {
    console.log(event);
    Array.from(texts).map((text) => {
        text.style.fontWeight = event.target.value * 10;
    });
});