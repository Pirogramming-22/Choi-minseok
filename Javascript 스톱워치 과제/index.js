const time = document.querySelector('#watch-time');
const startBtn = document.querySelector('#start');
const stopBtn = document.querySelector('#stop');
const resetBtn = document.querySelector('#reset');
const records = document.querySelector('#record-data');
const checkAllBtn = document.querySelector('#record-all');
const deleteAllbtn = document.querySelector('#btn-delAll');
const deleteSelbtn = document.querySelector('#btn-delSel');

function convertToMilliseconds(timeString) {
    const [minutes, seconds] = timeString.split(':').map(Number);
    const totalMilliseconds = (minutes * 60 + seconds) * 1000;
    return totalMilliseconds;
}
function convertMillisecondsToMinSec(milliseconds) {
    const totalSeconds = Math.floor(milliseconds / 1000);
    
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;
    
    const formattedMinutes = minutes.toString().padStart(2, '0');
    const formattedSeconds = seconds.toString().padStart(2, '0');
    
    return `${formattedMinutes} : ${formattedSeconds}`;
}

let addTime = null;
function startTime(){
    if(!addTime){
        let now = convertToMilliseconds(time.innerHTML);
        addTime = setInterval(function(){
            now = now+1000;
            time.innerHTML = convertMillisecondsToMinSec(now);
        }, 1000);
    }
}

function stopTime(){
    if(addTime){
        const recordList = document.createElement('div');
        recordList.className = 'record-list';

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.className = 'check';

        const timeSpan = document.createElement('span');
        timeSpan.textContent = time.innerHTML;

        const emptySpan = document.createElement('span');

        recordList.appendChild(checkbox);
        recordList.appendChild(timeSpan);
        recordList.appendChild(emptySpan);
        records.appendChild(recordList);
        clearInterval(addTime);
        addTime = null;
    }
}

function resetTime(){
    clearInterval(addTime);
    addTime = null;
    time.innerHTML = '00 : 00';
}

function checkAll(){
    for(let check of records.children){
        check.children[0].checked=checkAllBtn.checked;
    }
}

function deleteAll(){
    records.innerHTML = ``;
}
function deleteSel(){
    for(let check of records.children){
        if(check.children[0].checked){
            check.remove();
        }
    }
}
startBtn.addEventListener('click', startTime);
stopBtn.addEventListener('click', stopTime);
resetBtn.addEventListener('click', resetTime);
checkAllBtn.addEventListener('change', checkAll);
deleteAllbtn.addEventListener('click', deleteAll);
deleteSelbtn.addEventListener('click', deleteSel);