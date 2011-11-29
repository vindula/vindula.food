$j = jQuery.noConflict();

$j(document).ready(function(){

    var initialLocation;
    var siberia = new google.maps.LatLng(60, 105);
    var newyork = new google.maps.LatLng(40.69847032728747, -73.9514422416687);
    var browserSupportFlag =  new Boolean();
    var marker = new Array(document.querySelectorAll("input.address").length);
    var infowindow = new Array(document.querySelectorAll("input.address").length);
    
    function initialize() {
        geocoder = new google.maps.Geocoder();
        var myOptions = {
            zoom: 13,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
        
        for(var c=1; c <= document.querySelectorAll("input.address").length; c++)
        {
            createMark(c);
        }
    
        function createMark(number) {
            var address = document.getElementById("address"+number).value;
            var name = document.getElementById("name"+number).value;
            var url = './restaurant';
            var id = document.getElementById("id"+number).value;
            
            geocoder.geocode( {'address': address}, function(results, status) {
                
                if (status == google.maps.GeocoderStatus.OK) 
                {
                    var image = 'http://www.google.com/intl/en_us/mapfiles/ms/micons/restaurant.png';
                    marker[number-1] = new google.maps.Marker({
                        map: map,
                        position: results[0].geometry.location,
                        icon: image
                    });
                }
                else 
                {
                    alert("Geocode was not successful for the following reason: " + status);
                }
                
                infowindow[number-1] = new google.maps.InfoWindow({
                    content: '<div>'+                              
                                '<h2><a href="'+url+'?id='+id+'" target="_blank">'+name+'</a></h2>'+
                             '</div>'+
                             '<div>'+
                                address+
                             '</div>',

                    size: new google.maps.Size(50,50)
                });
                
                google.maps.event.addListener(marker[number-1], 'click', function() {
                    infowindow[number-1].open(map, marker[number-1]);
                });
                
                $j('.address-map'+number).click(function(){
                    var pos = marker[number-1].getPosition();
                    map.setCenter(pos);
                    map.setZoom(15);
                    for(var x=0; x < infowindow.length; x++)
                    {
                        if(x != number-1)
                          infowindow[x].close();
                    }
                    google.maps.event.trigger(marker[number-1], 'click');
                });
                
            });
            
            
        }
      
        // Try HTML5 geolocation
        if(navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var pos = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
                var image = 'http://www.google.com/intl/en_us/mapfiles/ms/micons/arrow.png';
                var marker = new google.maps.Marker({
                    map:map,
                    draggable:true,
                    animation: google.maps.Animation.DROP,
                    position: pos,
                    title: "Você está aqui.",
                    icon: image
                });
                map.setCenter(pos);
            }, function() {
                   handleNoGeolocation(browserSupportFlag);
               });
        // Try Google Gears Geolocation
        } else if (google.gears) {
            browserSupportFlag = true;
            var geo = google.gears.factory.create('beta.geolocation');
            geo.getCurrentPosition(function(position) {
                initialLocation = new google.maps.LatLng(position.latitude,position.longitude);
                map.setCenter(initialLocation);
            }, function() {
                handleNoGeoLocation(browserSupportFlag);
               });
        } else {
        // Browser doesn't support Geolocation
            browserSupportFlag = false;
            handleNoGeolocation(browserSupportFlag);
        }
        
    } 
    
    
    google.maps.event.addDomListener(window, 'load', initialize);
    
});