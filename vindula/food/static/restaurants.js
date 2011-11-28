$j = jQuery.noConflict();

$j(document).ready(function(){
	
    $j('select#order').change(function() { 
	   var url = $j("input[name='here_url']").val() + '/restaurantslist';
	   var selected = $j(this);
	   var index = selected.context.selectedIndex;
	   var option = selected.context.options[index];
       window.location = url + option.value;
	});
	
	$j('select#items_page').change(function() {
	   var url = $j("input[name='here_url']").val() + '/restaurantslist';
       var selected = $j(this);
       var index = selected.context.selectedIndex;
       var option = selected.context.options[index];
       window.location = url + option.value;
	});
	
	if ($j('input#error-specialty').val() == 'true')
	{
		alert('Essa especialidade não pode ser excluida pois está vinculada a um restaurante.')
	}
	
});