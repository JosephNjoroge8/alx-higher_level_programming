// Task 12: Fetches and prints how to say “Hello” depending on the language code entered by the user
$(document).ready(function () {
    $('#btn_translate').click(function () {
        const langCode = $('#language_code').val();
        $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function (data) {
            $('#hello').text(data.hello);
        });
    });
});
