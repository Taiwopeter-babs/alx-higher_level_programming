// queries an api with AJAX get
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
const $listMovies = $('UL#list_movies');

$(function () {
  $.get({
    url: url,
    success: function (films) {
      $.each(films.results, function (idx, film) {
        $listMovies.append('<li>' + film.title + '</>');
      });
    }
  });
});
