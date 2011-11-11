$j = jQuery.noConflict();

$j(document).ready(function(){

    var initialLocation;
    var siberia = new google.maps.LatLng(60, 105);
    var newyork = new google.maps.LatLng(40.69847032728747, -73.9514422416687);
    var browserSupportFlag =  new Boolean();
    
    function initialize() {
        geocoder = new google.maps.Geocoder();
        var myOptions = {
            zoom: 13,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
        
        var c=1;
        do
        {
            
            var address = document.getElementById("address"+c).value;
            geocoder.geocode( {'address': address}, function(results, status) {
                
                if (status == google.maps.GeocoderStatus.OK) 
                {
                    var image = 'http://www.google.com/intl/en_us/mapfiles/ms/micons/restaurant.png';
                    var marker = new google.maps.Marker({
                        map: map,
                        position: results[0].geometry.location,
                        icon: image
                    });
                }
                else 
                {
                    alert("Geocode was not successful for the following reason: " + status);
                }                                
            });
            c++;
        }while(c <= document.querySelectorAll("input.address").length);
      
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