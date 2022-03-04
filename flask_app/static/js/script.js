function random(max) {
    return Math.floor(Math.random() * max)
}

fetch("https://type.fit/api/quotes")
    .then(response => response.json())
    .then(coderData => document.getElementById('quote').innerText = coderData[random(1000)].text)
    .catch(err => console.log(err))

