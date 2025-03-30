let timer;
let timeRemaining;
let isTimerRunning = false;

document.getElementById("startBtn").addEventListener("click", startTimer);
document.getElementById("resetBtn").addEventListener("click", resetTimer);

function startTimer() {
    if (isTimerRunning) return;

    let minutes = document.getElementById("minutesInput").value;
    timeRemaining = minutes * 60;
    // converts into seconds
    isTimerRunning = true;

    document.getElementById("status").innerHTML = "Mode: Timer";

    timer = setInterval(() => {
        timeRemaining--;
        // with each second
        let mins = Math.floor(timeRemaining / 60);
        let secs = timeRemaining % 60;
        document.getElementById("display").innerHTML = mins + ":" + secs;
        if (timeRemaining == 0) {
            clearInterval(timer);
            isTimerRunning = false;
            showClock();
        }
    }, 1000);
}

function showClock() {
    if (isTimerRunning) return;

    setInterval(() => {
        let now = new Date();
        let hours = now.getHours();
        let minutes = now.getMinutes();
        let seconds = now.getSeconds();
        document.getElementById("display").innerHTML = hours + ":" + minutes + ":" + seconds;
    }, 1000);
}

function resetTimer() {
    clearInterval(timer);
    isTimerRunning = false;
    showClock();
}
