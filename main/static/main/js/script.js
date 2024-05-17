var modal = document.getElementById('myModal');

// Get the image and insert it inside the modal - use its "alt" text as a caption
let img_id;
const get_id = (id_img) => {
    console.log(id_img)
    var img = document.getElementById(id_img);
    var modalImg = document.getElementById("img01");
    var captionText = document.getElementById("caption");
    img.onclick = function () {
        modal.style.display = "block";
        modalImg.src = this.src;
        captionText.innerHTML = this.alt;
    }

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
    }
}



const buttons = document.querySelectorAll('.button');

buttons.forEach(button => {
    const dropdown = button.querySelector('.button__dropdown');

    if (dropdown) {
        const svg = button.querySelector('.chevron');

        button.addEventListener('click', function () {
            dropdown.classList.toggle('active');
            svg.classList.toggle('active')
        });
    }
});


const searchBtn = document.querySelector('.search__arrow')
const searchBigCard = document.querySelector('.frame23')
const searchContainer = document.querySelector('.search')
const bgShadow = document.querySelector('.shadow')

searchContainer.addEventListener('click', () => {
    // searchBtn.classList.toggle('active')
    searchContainer.classList.toggle('active')
    searchBigCard.classList.toggle('active')
    bgShadow.classList.toggle('active')
})

bgShadow.addEventListener('click', () => {
    // searchBtn.classList.toggle('active')
    searchContainer.classList.toggle('active')
    searchBigCard.classList.toggle('active')
    bgShadow.classList.toggle('active')
})



const chooseBtns = document.querySelectorAll('.choose__btn')

chooseBtns.forEach(button => {
    button.addEventListener('click', () => {
        button.classList.toggle('active')
    })
})




document.addEventListener('DOMContentLoaded', function () {
    const filterForm = document.getElementById('filter-form');
    const filterSubmit = document.getElementById('filter-submit');

    // Обработчик нажатия на кнопку "Найти"
    filterSubmit.addEventListener('click', function (event) {
        event.preventDefault(); // Отменяем стандартное поведение кнопки

        // Собираем значения выбранных параметров
        const selectedYear = document.querySelector('.filter__col.active .choose__btn.selected').dataset.year || '';
        const selectedSpec = document.querySelector('.filter__col.active .choose__btn.selected').dataset.spec || '';

        // Создаем новый URL с параметрами фильтрации
        let url = "{% url 'index' %}?";
        if (selectedYear && selectedSpec) {
            url += "year=" + selectedYear + "&" + "specialization=" + selectedSpec;
        } else if (selectedYear) {
            url += "year=" + selectedYear;
        } else if (selectedSpec) {
            url += "specialization=" + selectedSpec;
        }

        // Перенаправляем пользователя по новому URL
        window.location.href = url;
    });

    // Обработчик клика на элемент фильтрации
    var filterItems = document.querySelectorAll('.choose__btn');
    filterItems.forEach(function (item) {
        item.addEventListener('click', function () {
            // Убираем класс selected у всех элементов
            filterItems.forEach(function (item) {
                item.classList.remove('selected');
            });
            // Добавляем класс selected к выбранному элементу
            this.classList.add('selected');
        });
    });

    var yearsCol = document.getElementById('years__col');
    yearsCol.addEventListener('wheel', function (event) {
        if (event.deltaY !== 0) {
            event.preventDefault();
            yearsCol.scrollLeft += event.deltaY;
        }
    });
});

























document.addEventListener('DOMContentLoaded', function () {
    const slider = document.querySelector('.slider');
    const slides = document.querySelector('.slides');
    const slideWidth = slider.offsetWidth; // Ширина слайдера
    let slideIndex = 0;

    function nextSlide() {
        if (slideIndex < 2) {
            slideIndex++;
        } else {
            slideIndex = 0;
        }
        slides.style.transform = `translateX(-${slideIndex * slideWidth}px)`;
    }

    // Автоматическое переключение слайдов каждые 3 секунды
    setInterval(nextSlide, 3000);
});












