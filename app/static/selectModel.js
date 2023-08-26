function selectModel(modelName) {
    fetch('/select/model', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            model: modelName
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    });
}

function sendText(text, word) {
    fetch('/prompt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: text,
            word: word
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    });
}


function prettyDate(dateString) {
    let date = new Date(dateString);
    let day = date.getDate();
    let month = date.getMonth() + 1;
    let year = date.getFullYear();
    let hours = date.getHours();
    let minutes = date.getMinutes();

    day = (day < 10) ? '0' + day : day;
    month = (month < 10) ? '0' + month : month;
    hours = (hours < 10) ? '0' + hours : hours;
    minutes = (minutes < 10) ? '0' + minutes : minutes;

     return `${day}.${month}.${year} ${hours}:${minutes}`
}

function setCurDate(){
     return new Date().toLocaleDateString()
}

if (document.getElementsByClassName("date")){
   let dates = document.getElementsByClassName("date")
    for (let i = 0; i < dates.length; i++){
        let cur = dates[i].innerText
        dates[i].innerText = prettyDate(cur)
    }
} else {
    document.getElementById("date-container").innerText = setCurDate()
}
