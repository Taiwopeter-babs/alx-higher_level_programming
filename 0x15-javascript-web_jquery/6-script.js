// updates the text of an element
$(function () {
  $('DIV#update_header').on('click', () => {
    $('header').text('New Header!!!');
  });
});
