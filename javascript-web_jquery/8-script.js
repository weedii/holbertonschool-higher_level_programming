$(function () {
  $.getJSON(
    'https://swapi-api.hbtn.io/api/films/?format=json',
    function (data) {
      for (var i = 0; i < data.results.length; i++) {
        const lst_item = $('<li></li>').text(data.results[i].title)
        $('UL#list_movies').append(lst_item)
      }
    }
  )
})
