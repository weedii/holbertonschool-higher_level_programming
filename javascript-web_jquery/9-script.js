$(function() {
  $.getJSON('https://stefanbohacek.com/hellosalut/?lang=fr', function(data) {
    var hello = $(data).find('#hello').text();
    $('DIV#hello').text(hello);
  });
});
