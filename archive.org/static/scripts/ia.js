$(function() {
    var page = '.nav-web';
    var url = window.location.href.split('/');
    if (url[url.length-1] !== '') {
	page = ".nav-" + url[url.length-1];
    }

    $('.menu ul li a').removeClass('active');
    $(page).addClass('active');

    
    $('.serpid').each(function(index) {
	var serpy = $(this)
	url = '/api/v1/resource/' + serpy.html() + '/meta'
	$.get(url, function(data) {
	    var filez = JSON.stringify(data);
	    serpy.html(filez);
	});
    });

    $('.serpresult').each(function(index) {
	var thisresult = $(this);
	var preview = thisresult.find('.serpid');
	thisresult.mouseover(function() {
	    preview.css('visibility', 'visible');
	}).mouseleave(function() {
	    preview.css('visibility', 'hidden');
	});
    });
});
