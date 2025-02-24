document.addEventListener("DOMContentLoaded", function() {
    fetch("films.json")
        .then(response => response.json())
        .then(data => {
            loadFilms(data);
            document.getElementById("search").addEventListener("input", function() {
                filterFilms(data);
            });
            document.getElementById("filter-column").addEventListener("change", function() {
                filterFilms(data);
            });
        })
        .catch(error => console.error("Ошибка загрузки данных:", error));
});

function loadFilms(data) {
    let container = document.getElementById("filmsContainer");
    container.innerHTML = "";
    data.forEach(film => {
        let filmCard = document.createElement("div");
        filmCard.classList.add("film-card");
        filmCard.style.backgroundImage = `url(${film.cover})`;
        filmCard.innerHTML = `
                    <div class="film-info">
                        <div class="film-title">${film.title}</div>
                        <div class="film-details">Director: ${film.director}</div>
                        <div class="film-details">Producers: ${film.producers}</div>
                        
                        <div class="film-details">Box Office: ${film.box_office}</div>
                        <div class="film-details">Country: ${film.country}</div>
                        <div class="film-details">Year: ${film.year}</div>
                    </div>
                `;
        container.appendChild(filmCard);
    });
}

function filterFilms(data) {
    let query = document.getElementById("search").value.toLowerCase();
    let column = document.getElementById("filter-column").value;
    let filtered = data.filter(film => film[column].toString().toLowerCase().includes(query));
    loadFilms(filtered);
}