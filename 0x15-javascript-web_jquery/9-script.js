// Task 9: Fetches the value of hello in French and displays it in the HTML tag DIV#hello
$(document).ready(function () {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
        $('#hello').text(data.hello);
    });
});
