var geocoder;
var map;
var marker;

function initialize() 
{
	geocoder = new google.maps.Geocoder();
	var latlng = new google.maps.LatLng(-23.548566,-46.64443);
	var myOptions = 
	{
		zoom: 16,
		center: latlng,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	}
	map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
}

function codeAddress() {
	var address = document.getElementById("address").value;
	geocoder.geocode( { 'address': address}, function(results, status) {
		
		if (status == google.maps.GeocoderStatus.OK) 
		{
			map.setCenter(results[0].geometry.location);
			marker = new google.maps.Marker({
				map: map,
				position: results[0].geometry.location
			});
		} 
		
		else 
		{
		    alert("Geocode was not successful for the following reason: " + status);
		}
		
		var infowindow = new google.maps.InfoWindow({
			
			content: '<div>' +
			             '<h2>'+document.getElementById("name").value+'</h2>'+
			         '</div>' +
					 '<div>'+
					   document.getElementById("address").value+
					 '</div>',

	        size: new google.maps.Size(100,100)
	    });
	    
	    google.maps.event.addListener(marker, 'click', function() {
	        infowindow.open(map, marker);
	    });
		
	});
	
	
}

google.maps.event.addDomListener(window, 'load', initialize); 
google.maps.event.addDomListener(window, 'load', codeAddress);