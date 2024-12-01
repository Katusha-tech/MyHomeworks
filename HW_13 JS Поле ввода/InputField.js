const input = document.querySelector('#input');
const formButton = document.querySelector('#formButton');
const deleteButton = document.querySelector('#deleteButton');
const localID = document.querySelector('#localID');

// Обработка клика по кнопке "Запомнить"
formButton.addEventListener('click', function(event) {
    event.preventDefault();
    const inputValue = input.value.trim(); // Обрезаем пробелы

    // Простая проверка на пустое поле
    if (inputValue === '') {
        alert('Поле не может быть пустым!'); // Показываем предупреждение через alert
    } else {
        localID.textContent = inputValue;  // Отображение в <p> элементе
        localStorage.setItem('inputValue', inputValue);  // Сохранение в localStorage
    }
});

// Загрузка данных из localStorage при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    const inputValue = localStorage.getItem('inputValue');
    if (inputValue) {
        localID.textContent = inputValue;  // Если данные есть, показываем их
    }
});

// Удаление данных из localStorage при клике на кнопку "Удалить"
deleteButton.addEventListener('click', function() {
    localStorage.removeItem('inputValue');
    localID.textContent = 'Данные не обнаружены';  // Обновляем текст
});
