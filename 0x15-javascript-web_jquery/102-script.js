// get the language translation of `hello` from an api


$(function () {
    const $inputLanguage = $('INPUT#language_code');
    const $submitButton = $('INPUT#btn_translate');
    const url = 'https://www.fourtonfish.com/hellosalut/hello/';

    $submitButton.on('click', () => {
        $.get({
            url: url,
            parameters: `lang=${$inputLanguage.val()}`,
            success: function(data) {
                $('DIV#hello').text(data.code);
            },
            error: function() {
                alert(`lang=${$inputLanguage.val()}`);
            }
        })
    })
});