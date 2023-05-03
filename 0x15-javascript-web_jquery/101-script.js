/**
 * This script adds, clears, and deletes
 * a list item
 */

$(function () {
    $('DIV#add_item').on('click', () => {
        $('UL.my_list').append('<li>Item</li>');
    });
    $('DIV#remove_item').on('click', () => {
        $('UL.my_list li:last-child').remove();;
    });
    $('DIV#clear_list').on('click', () => {
        $('UL.my_list li').remove();
    });
});