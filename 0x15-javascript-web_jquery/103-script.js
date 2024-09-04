// Task 13: Fetches and prints how to say “Hello” depending on the language code entered by the user and when pressing Enter
$(document).ready(function () {
    function fetchHello() {
        const langCode = $('#language_code').val();
        $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function (data) {
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(function () {
        fetchHello();
    });

    $('#language_code').keypress(function (e) {
        if (e.which === 13) {
            fetchHello();
        }
    });
});
