$.getJSON('http://127.0.0.1:5000/api/', function(response){
    var people = response;
    $.each(people, function(i, person){
        var tr = $('<tr id="'+ person.name + '"></tr>');
        tr.appendTo("#people");
        $('<td id="' + person.id + '">' + person.name + '</td>').appendTo(tr);
        $('<td>' + person.age + '</td>').appendTo(tr);
    });
});

$(document).on('click', 'td', function () {
    var id = $(this).attr('id');
    var url = 'http://127.0.0.1:5000/api/id/'+id;
    $.getJSON(url, function(response) {
        $('h1').empty();
        $('table').hide();
        $('body').append('<h1>' + response.name + ' ' + response.age + '</h1>');
    });
});
