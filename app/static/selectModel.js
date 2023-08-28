function selectModel(modelName) {
    fetch('/select/model', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            model_type: modelName.toLowerCase()
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

    day = (day < 10) ? '0' + day : day;
    month = (month < 10) ? '0' + month : month;
    return `${day}.${month}.${year}`
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
