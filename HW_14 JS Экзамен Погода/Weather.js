// https://api.openweathermap.org/data/2.5/weather?q=Москва&appid=89d4ef259b167357f183cf4ab0d66ff3&units=metric&lang=ru

const apiKey ='89d4ef259b167357f183cf4ab0d66ff3';
const units = 'metric';
const lang = 'ru';

const input = document.getElementById('input');
const formButton = document.getElementById('formButton');
const airPollutionDiv = document.getElementById('airPollution');
const forecastDiv = document.getElementById('forecastDiv');
const currentWeatherDiv = document.getElementById('currentWeather');

const airPollutionDescriptionObj = {
    1: { description: 'Отличное', bsClass: 'alert-success'},
    2: { description: 'Хорошее', bsClass: 'alert-primary'},
    3: { description: 'Удовлетворительное', bsClass: 'alert-warning'},
    4: { description: 'Плохое', bsClass: 'alert-danger' },
    5: { description: 'Ужасное', bsClass: 'alert-danger'}
};

//Функция получает город из формы, формирует URL для запроса к GEOAPI, выполняет запрос, получает ответ, возвращает объект с данными о городе. lat lon ключи (создадим новый компактный объект)

async function getGeoByCityName(cityName) {
    const url = `http://api.openweathermap.org/geo/1.0/direct?q=${cityName}&limit=1&appid=${apiKey}`;
    const response = await fetch(url);
    if (response.ok) {
        const data = await response.json();
        //Проверка на пустой массив Alert
        if (data.length === 0) {
            alert('Город не найден');
            throw new Error('Город не найден');
        }     
        clearData = {
            lat: data[0].lat,
            lon: data[0].lon
        };
        
        return clearData;
    } else {
        console.error('Ошибка при получении данных');
        throw new Error(`HTTP-код ошибки: ${response.status}`);
    }
}

function getUrlByInput(lat,lon) {
    let weatherUrlsObject = {
        currentWeather: `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}`,
        forecastWeather: `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&appid=${apiKey}`,
        airPollution: `http://api.openweathermap.org/data/2.5/air_pollution?lat=${lat}&lon=${lon}&appid=${apiKey}`
    };
    return weatherUrlsObject;
}

async function getWeather(url) {
    const response = await fetch(url);
    if (response.ok) {
        console.log('Получен успешный ответ от URL:' + url);
        return await response.json(); 
        } else {
            console.error('Ошибка при получении данных от URL:' + url);
            throw new Error(`HTTP-код ошибки: ${response.status}`);
        }    
    } 

formButton.addEventListener('click', async (event) => {
    event.preventDefault();
    const cityName = input.value;
    // Запишем cityName в LocalStorage
    localStorage.setItem('cityName', cityName);
    // Функция отрисовывает погоду по названию города
    displayAllWeather(cityName);
    });

// Добавим листнер на документ, чтобы по загрузке страницы, проверяли наличие города в LocalStorage и если он там есть, он  становился бы в value input'а и вызывался бы методом displayAllWeather по этоу городу

document.addEventListener('DOMContentLoaded', () => {
    const cityName = localStorage.getItem('cityName');
    if (cityName) {
        input.value = cityName;
        displayAllWeather(cityName);
    }
});

async function displayAllWeather(cityName) {
    let geoData = await getGeoByCityName(cityName);
    console.log(geoData);
    let urlsObject = getUrlByInput(geoData.lat, geoData.lon);
    console.log(urlsObject);

    // Получаем данные о погоде (вариант параллельно)
    let weatherData = await Promise.all([
        getWeather(urlsObject.currentWeather),
        getWeather(urlsObject.forecastWeather),
        getWeather(urlsObject.airPollution),
    ]);

    // массив из объектов с данными о погоде - weatherData
   let resultWeatherData = {
    currentWeather: weatherData[0],
    forecastWeather: weatherData[1],
    airPollution: weatherData[2],
   };

   console.log(resultWeatherData);
   //состояние воздуха
   displayAirPollution(resultWeatherData.airPollution);
   //Текущая погода
   displayCurrentWeather(resultWeatherData.currentWeather);
   //Прогноз погоды на 5 дней
   displayForecastWeather(resultWeatherData.forecastWeather);
}


// Функция (либо в листнер запсиать), которая принимает объект с сототоянием воздуха и опираясь airPollutionDescriptionObj в airPollution меняет цвет класса и текст 
function displayAirPollution(airPollution) {
    const airPollutionDescription = airPollutionDescriptionObj[airPollution.list[0].main.aqi];
    // Проверяем сколько классов на элементе airPollution
    const airPollutionClasses = airPollutionDiv.classList;
    //Если классов больше, чем 1, то удаляем последний
    if (airPollutionClasses.length > 1) {
        airPollutionDiv.classList.remove(airPollutionClasses[airPollutionClasses.length - 1]);
    }
    // Добавляем класс
    airPollutionDiv.classList.add(airPollutionDescription.bsClass);
    // Добавляем текст
    airPollutionDiv.textContent = airPollutionDescription.description;
    airPollutionDiv.innerHTML = `
        <div>${airPollutionDescription.description}</div>`;
}
// Функция которая добывает ссылку на иконку погоды
function getIconUrl(iconCode, size) {
    if (size === undefined) {
        size = '';
    }
    else if (size === '4x') {
        size = '@4x';
    }
    else if (size === '2x') {
        size = '@2x';
    }
    else {
        throw new Error('Неизвестный размер');
    }
    return `https://openweathermap.org/img/wn/${iconCode}${size}.png`;
}

function displayCurrentWeather(currentWeather) {
    const cityName = currentWeather.name;
    const iconID  = currentWeather.weather[0].icon;
    const iconUrl = getIconUrl(iconID, '4x');
    const temp = currentWeather.main.temp;
    const feelsLike = currentWeather.main.feels_like;
    const windSpeed = currentWeather.wind.speed;
    
    // Очистим старые данные (оставляя заголовок)
    currentWeatherDiv.innerHTML = `
        <h3>Текущая погода</h3>
        <p><img src="${iconUrl}" alt="Иконка погоды"> ${cityName}</p>
        <p>Температура: ${temp}°C (ощущается как: ${feelsLike}°C)</p>
        <p>Скорость ветра: ${windSpeed} м/с</p>`;    
}

// Функция, которая в forecastDiv в конец добавляет наследника Table и рисует BS5 таблицу с прогнозом погоды
// Принимает объект с прогнозом погоды

// В таблице столбцы: дата, время, иконка (маленькая), температура,ощущается как, ветер.

function displayForecastWeather(forecastWeather) {
    const tableBody = forecastDiv.querySelector('tbody');
    // Очистим старые данные
    tableBody.innerHTML = '';
    // Объявляем цикл, который перебирает массив forecastWeather.list и создает строки таблицы
    for (let weatherObj of forecastWeather.list) {
        // Получаем данные из очередного объекта

        const dateTime = weatherObj.dt_txt; //"2022-08-30 15:00:00"
        const date = dateTime.split(' ')[0];
        const time = dateTime.split(' ')[1].split(':')[0] + 'ч.';
        const finalDateTime = date + ' ' + time;
        const idIcon = weatherObj.weather[0].icon;
        const iconUrl = getIconUrl(idIcon);
        const temp = weatherObj.main.temp;
        const windSpeed = weatherObj.wind.speed;

        // Создаем строку таблицы
        const row = `<tr>
            <td>${finalDateTime}</td>
            <td><img src="${iconUrl}" alt="Иконка погоды"></td>
            <td>${temp}</td>
            <td>${windSpeed}</td>
        </tr>`;

        // Добавляем строку в таблицу
        tableBody.innerHTML += row;
    }
}

    