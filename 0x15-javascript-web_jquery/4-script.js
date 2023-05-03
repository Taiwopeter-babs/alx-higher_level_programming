// select element by id and toggle classes of another element

$('DIV#toggle_header').on('click', function () {
  $('header').toggleClass('red green');
});
