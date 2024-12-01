let weatherData = {
    corod:{lon: 30.2642, lat: 59.8944},
    weather:[{id: 800, main: "Clear", description: "ясно", icon:"01n" }],
    base:"stations",
    main:{
        temp: 15.03,
        feels_like: 14.65,
        temp_min: 14.08,
        temp_max: 15.03,
        pressure: 1011,
        humidity: 79,
        sea_level: 1011,
        grnd_level: 1009,
    },
    visibility: 10000,
    wind:{speed: 3, deg: 150},
    clouds:{all: 0},
    dt: 1727203506,
    sys:{
        type: 2,
        id: 197864,
        country: "RU",
        sunrise: 1727149703,
        sunset: 1727193203
    },
    timezone: 10800,
    id: 498817,
    name:"Санкт-Петербург",
    cod: 200,
};

//Возвращение очищенного объекта с нужными данными
function parseWeatherData(weatherData) {
    return {
        city: weatherData.name,
        description: weatherData.weather[0].description,
        temperature: weatherData.main.temp,
        feels_like: weatherData.main.feels_like,
        wind_speed: weatherData.wind.speed,
    };
}

//Создание элементов на странице 
function renderWeatherData(weatherData) {
    const container = document.getElementById('displayWeather');
    container.innerHTML = '';
    
    //Заголовок
    const title = document.createElement('h1');
    title.classList.add('text-center', 'my-4');
    title.textContent = `Сейчас в г. ${weatherData.city} - ${weatherData.description}`;

    //Температура
    const tempElement = document.createElement('p');
    tempElement.classList.add('fs-3', 'text-center');
    tempElement.textContent = `Температура: ${weatherData.temperature}°C`;

    //Ощущает как
    const feelsLikeElement = document.createElement('p');
    feelsLikeElement.classList.add('fs-4', 'text-center');
    feelsLikeElement.textContent = `Ощущается как: ${weatherData.feels_like}°C`;

    //Скорость ветра
    const windSpeedElement = document.createElement('p');
    windSpeedElement.classList.add('fs-5', 'text-center');
    windSpeedElement.textContent = `Скорость ветра: ${weatherData.wind_speed} м/с`;

    //Добавляем все элементы в контейнер
    container.appendChild(title);
    container.appendChild(tempElement);
    container.appendChild(feelsLikeElement);
    container.appendChild(windSpeedElement);
}

//Добавляем событие
document.addEventListener('DOMContentLoaded', function() {
    let parsedWeather = parseWeatherData(weatherData);
    renderWeatherData(parsedWeather);
});