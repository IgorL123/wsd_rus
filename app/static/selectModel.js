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