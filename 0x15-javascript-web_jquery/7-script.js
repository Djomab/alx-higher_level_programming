$(function()
{
  const endpoint = 'https://swapi-api.hbtn.io/api/people/5/?format=json'
	$.get(endpoint, function(data, textStatus)
	{
    $('DIV#character').text(data.name);
	});
});