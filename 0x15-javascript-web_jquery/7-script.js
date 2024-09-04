// Task 7: Fetches the character name from the API and displays it in the HTML tag DIV#character
$(document).ready(function () {
    $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
        $('#character').text(data.name);
    });
});
