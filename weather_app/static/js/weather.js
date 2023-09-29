console.log("please work")

OpenWeatherAPIKey = "3f0d7a3bfa407a788c7db9caa27126ce"
fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${54.607868}&lon=${-5.926437}&appid=${OpenWeatherAPIKey}`).then(response => response.json()).then(data => console.log(data))