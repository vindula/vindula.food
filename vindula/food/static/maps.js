$j = jQuery.noConflict();

$j(document).ready(function(){
	
    var directionDisplay;
    var minha_pos;
	var directionsService = new google.maps.DirectionsService();
    var browserSupportFlag =  new Boolean();
	
	var qdt_rest = document.querySelectorAll("input.address").length;
    var marker = new Array(qdt_rest);
    var infowindow = new Array(qdt_rest);
	var dest_pos = new Array(qdt_rest);
	
    function initialize(){
		directionsDisplay = new google.maps.DirectionsRenderer({suppressMarkers: true});
        var myOptions = {
            zoom: 13,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
		
        var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
		directionsDisplay.setMap(map);
        
        for(var c=1; c <= qdt_rest; c++)
        {
            createMark(c);
        }
    
        function createMark(number) {
			var geocoder = new google.maps.Geocoder();
            var address = document.getElementById("address"+number).value;
            var name = document.getElementById("name"+number).value;
			var id = document.getElementById("id"+number).value;
            var url = './restaurant';
            var image = 'http://www.google.com/intl/en_us/mapfiles/ms/micons/restaurant.png';
			var contador = number-1;

            geocoder.geocode( {'address': address}, function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) 
                {
					dest_pos[contador] = results[0].geometry.location;
                    marker[contador] = new google.maps.Marker({
                        map: map,
                        position: results[0].geometry.location,
                        icon: image
                    });
					
					infowindow[contador] = new google.maps.InfoWindow({
		                content: '<div>'+
		                            '<h2 id="secondHeading" class="secondHeading"><a href="'+url+'?id='+id+'" target="_blank">'+name+'</a></h2>'+
		                            '<div id="bodyContent">'+
		                                '<p>'+address+'</p>'+
		                            '</div>'+
		                         '</div>'
	                });
		                
	                google.maps.event.addListener(marker[contador], 'click', function() {
	                    infowindow[contador].open(map, marker[number-1]);
	                });
	                
	                $j('.address-map'+number).click(function(){
	                    var pos = marker[contador].getPosition();
	                    map.setCenter(pos);
	                    map.setZoom(15);
	                    for(var x=0; x < infowindow.length; x++)
	                    {
	                        if(x != number-1)
	                          infowindow[x].close();
	                    }
	                    google.maps.event.trigger(marker[number-1], 'click');
	                });
	                
	                $j('.tracaRota'+number).click(function(){
	                    tracaRota(minha_pos, dest_pos[contador]);
	                });
                }
                else 
                {
                    //alert("Geocode was not successful for the following reason: " + status);
                }
            });
        }

		// Try W3C Geolocation (Preferred)
		if(navigator.geolocation) {
			browserSupportFlag = true;
			navigator.geolocation.getCurrentPosition(function(position) {
				minha_pos = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
                var image = 'http://www.google.com/intl/en_us/mapfiles/ms/micons/arrow.png';
                var marker = new google.maps.Marker({
                    map:map,
                    draggable:true,
                    animation: google.maps.Animation.DROP,
                    position: minha_pos,
                    title: "Você está aqui.",
                    icon: image
                });
                map.setCenter(minha_pos);
                
                google.maps.event.addListener(marker, 'dragend', function() {
                    minha_pos = marker.getPosition();
                });
			}, function() {
                handleNoGeolocation(browserSupportFlag);
			});
			
		// Try Google Gears Geolocation
		} else if (google.gears) {
			browserSupportFlag = true;
			var geo = google.gears.factory.create('beta.geolocation');
			geo.getCurrentPosition(function(position) {
				minha_pos = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
                var image = 'http://www.google.com/intl/en_us/mapfiles/ms/micons/arrow.png';
                var marker = new google.maps.Marker({
                    map:map,
                    draggable:true,
                    animation: google.maps.Animation.DROP,
                    position: minha_pos,
                    title: "Você está aqui.",
                    icon: image
                });
                map.setCenter(minha_pos);
                
                google.maps.event.addListener(marker, 'dragend', function() {
                    minha_pos = marker.getPosition();
                });
			}, function() {
			    handleNoGeoLocation(browserSupportFlag);
			});
		// Browser doesn't support Geolocation
		} else {
			browserSupportFlag = false;
			handleNoGeolocation(browserSupportFlag);
		}
		
		function handleNoGeolocation(errorFlag) {
			var saopaulo = new google.maps.LatLng(-23.548842,-46.639023);
			if (errorFlag == true) {
				//alert("Falha no serviço de geolocalização.");
			} else {
				alert("Seu navegador não tem suporte para geolocalização. Use um navegador mais recente");
			}
			map.setCenter(saopaulo);
		}
    }
	
	function tracaRota(inicio, fim)
	{
		var request = {
			origin:inicio, 
			destination:fim,
			travelMode: google.maps.DirectionsTravelMode.DRIVING
		};
		
		directionsService.route(request, function(result, status) {
		  if (status == google.maps.DirectionsStatus.OK) {
		      directionsDisplay.setDirections(result);
		  }
		});
	}
    
    google.maps.event.addDomListener(window, 'load', initialize);
});