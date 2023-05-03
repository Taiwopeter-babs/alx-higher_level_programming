// queries an api and loads the result
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
const $divHello = $('DIV#hello');

$(function () {
  $.get({
    url: url,
    success: function (data) {
      $divHello.text(data.hello);
    },
    error: function () {
      alert('The server could not process the request');
    }
  });
});
