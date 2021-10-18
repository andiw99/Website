// document.getElementById("test").innerText = 5

let error_message = document.getElementById("error");
let pos = 0;
let step = 0.5;
let button_running = false;
let button_step = 0.5;

let slide_pos = 0;
let article_1 = document.getElementById("article_1")

let secondHand = document.getElementById("second-hand")
let minuteHand = document.getElementById("minute-hand")
let hourHand = document.getElementById("hour-hand")


let count = JSON.parse(localStorage.getItem("count"));

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

    let hour_rotation = hours * 360 + minutes * 30

    secondHand.style.transform = "rotate(" + seconds * 360 + "deg)"
    minuteHand.style.transform = "rotate(" + minutes * 360 + "deg)"
    hourHand.style.transform = "rotate(" + hour_rotation + "deg)"
}

function slide_article(nr_articles, article_width=60) {
    slide_id = setInterval(frame, 5);
    let current_slide_pos = slide_pos
    console.log(article_1);
    console.log("slide_article wird ausgeführt");
    console.log(current_slide_pos);
    console.log(slide_pos);
    console.log("nr of articles:", nr_articles)
    function frame() {
        if (current_slide_pos - slide_pos === article_width || current_slide_pos - slide_pos === -article_width) {
            console.log("Wir brechen ab");
            clearInterval(slide_id);
        } else if((slide_pos === -(nr_articles - 1) * article_width && step > 0) || (slide_pos >= 0 && step < 0)) {
            step = -step;
            slide_pos -= step;
            console.log("wir laufen in den änderungsdings rein")
            article_1.style.marginLeft = slide_pos + 'vw';
            console.log("step:", step)
            console.log("slide_pos", slide_pos)
        } else {
            slide_pos -= step;
            article_1.style.marginLeft = slide_pos + 'vw';
            console.log("step:", step)
            console.log("slide_pos", slide_pos)
        }
    }
}


function swipe_left(nr_articles, article_width=60) {
    let current_slide_pos = slide_pos;
    if (button_running === false && current_slide_pos <= -article_width) {
        console.log("swiping...")
        slide_id = setInterval(frame, 5);
        button_running = true;
        function frame() {
            if (current_slide_pos - slide_pos === -article_width) {
                clearInterval(slide_id);
                button_running = false;
                button_step = 0.5
            } else {
                slide_pos += button_step;
                article_1.style.marginLeft = slide_pos + 'vw';
                console.log(article_1.style.marginLeft)
                console.log(button_running)
            }
        }

    } else {
        console.log("slide already running")
    }
    clearInterval(slide);
    slide = setInterval(function () { slide_article(nr_articles)}, 7000)
}

function swipe_right(nr_articles, article_width=60) {
    let current_slide_pos = slide_pos;
    if ( button_running === false && current_slide_pos >= -(nr_articles - 2) * article_width) {
        slide_id = setInterval(frame, 5);
        button_running = true;
            function frame() {
                if (current_slide_pos - slide_pos === article_width) {
                    clearInterval(slide_id);
                    button_running = false;
                    button_step = 0.5
                } else {
                    slide_pos -= button_step ;
                    article_1.style.marginLeft = slide_pos + 'vw';
                    console.log(article_1.style.marginLeft)
                    console.log(button_running)
                        }
                }

    } else {
    }
    clearInterval(slide);
    slide = setInterval(function () { slide_article(nr_articles)}, 7000)
}

function start_slide_article(article_nr) {
    console.log("starte sliding")
    change_indicator(article_nr)
    slide = setInterval(function () { slide_article(article_nr)}, 7000)
    indi = setInterval(function () {change_indicator(article_nr)}, 250)
}

function indicator(nr_articles) {
    let indicators = [];
    let indicators_width = nr_articles * 4;
    let whitespace_width = 100 - indicators_width
    for (let i=1; i <= nr_articles; i++) {
        indicators.push(document.getElementById("indicator_" + i))
        indicators[i-1].style.marginLeft = (whitespace_width/2 + i*2) + "%"
    }
    return indicators;
}


function change_indicator(nr_articles, article_width=60) {
    indicators = indicator(nr_articles)
    shown_article = Math.round(-slide_pos / article_width)
    console.log("shown article:", shown_article)
    for (let i=0; i< nr_articles; i++) {
        indicators[i].style.backgroundColor = "rgba(250,250,250,0.5)"
    }
    indicators[shown_article].style.backgroundColor = "rgba(250, 250, 250, 0.8)"
}

animate_clock()
setInterval(animate_clock, 1000)


