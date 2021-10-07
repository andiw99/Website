// document.getElementById("test").innerText = 5

let countEl = document.getElementById("test");
let error_message = document.getElementById("error");
let pos = 0;
let step = 0.5

let secondHand = document.getElementById("second-hand")
let minuteHand = document.getElementById("minute-hand")
let hourHand = document.getElementById("hour-hand")


let count = JSON.parse(localStorage.getItem("count"));
countEl.innerText = count;

if (count == null) {
    count = 0;
}


function increment() {
    console.log("The button was clicked");
    count += 1;
    console.log(count);
    countEl.innerText = count;
}

function decrement() {
    console.log("Decrement button was clicked");
    count -= 1;
    countEl.innerText = count;
}

function save() {
    localStorage.setItem("count", count)
    console.log("saved")
}

function raise_error() {
    error_message.innerText = "Sth went wrong, pls try again"
    console.log("purchase button clicked")
}

function myMove() {
    var elem = document.getElementById("animated_obj");
    id = setInterval(frame, 10);
    function frame() {
        if (pos === 91) {
            step = -step;
            pos += step;
            elem.style.left = pos + '%';
        } else if (pos === 0 && step < 0) {
            step = -step;
            pos += step;
            elem.style.left = pos + '%';
        } else {
            pos += step;
            elem.style.left = pos + '%';
        }
    }
}

function stopMyMove() {
        clearInterval(id)
}

function animate_clock() {
    let date = new Date();
    let seconds = date.getSeconds()/60;
    let minutes = date.getMinutes()/60;
    let hours = date.getHours()/12;

    secondHand.style.transform = "rotate(" + seconds * 360 + "deg)"
    minuteHand.style.transform = "rotate(" + minutes * 360 + "deg)"
    hourHand.style.transform = "rotate(" + hours *360 + "deg)"
}
animate_clock()
setInterval(animate_clock, 1000)