// adds a new list element to a list on click
$('DIV#add_item').on('click', () => {
  $('UL.my_list').append('<li>Item</>');
});
