$(function()
{
    $.get
	(
		"https://swapi-api.hbtn.io/api/films/?format=json", 
		function(data, textStatus)
        {
          console.log(data);
        	$.each(data.results, function(index, movie)
          {
				    $("UL#list_movies").append($("<li></li>").text(movie.title));
          });
        },
		"json"
	);		
});