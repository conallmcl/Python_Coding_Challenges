console.log("please work")
temp_element = document.querySelector(".temp")
city_element = document.querySelector(".city")
search_element = document.querySelector("input")
button_element = document.querySelector("button")
image_element = document.querySelector(".weather-icon")

OpenWeatherAPIKey = "3f0d7a3bfa407a788c7db9caa27126ce" 
default_location = "Belfast"
// fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city name}&appid=${OpenWeatherAPIKey}`)
// fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${54.607868}&lon=${-5.926437}&appid=${OpenWeatherAPIKey}`).then(response => response.json()).then(data => {
//     console.log(data)
//     city_element.innerText = data.name
//     temp_element.innerText = `${Math.round(data.main.temp - 273.15)}°C`
// })

runSearch = ()=>{
    if (search_element.value.length === 0){
        searchquery = "Belfast"
    }else{
        searchquery = search_element.value
    }
    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${searchquery}&appid=${OpenWeatherAPIKey}`).then(response => response.json()).then(data => {
    console.log(data)
    city_element.innerText = data.name
    temp_element.innerText = `${Math.round(data.main.temp - 273.15)}°C`
    weather = data.weather[0].main
    image_element.src = `static/img/weather-app-icons/${weather}.png`
})}

runSearch()