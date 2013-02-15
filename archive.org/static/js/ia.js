$(function() {
    $('.serpid').each(function(index) {
	var serpy = $(this)
	url = '/ajax?id=' + serpy.html()
	$.get(url, function(data) {
	    var filez = JSON.stringify(data);
	    serpy.html(filez);
	    serpy.css('visibility', 'visible');
	});
    });
});