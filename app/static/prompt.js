function makePrompt(text, word) {
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
    .then(result => {
        document.getElementById("result").textContent = result;
    });
}