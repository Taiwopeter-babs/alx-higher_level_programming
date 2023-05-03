// queries an api with AJAX get
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$(function () {
  $.ajax({
    url: url,
    success: function (data) {
      $('DIV#character').text(data.name);
    }
  });
});
