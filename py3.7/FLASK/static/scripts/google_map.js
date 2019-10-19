function myMap() {
    var mapProp= {
    center:new google.maps.LatLng(_lat, _lng),
    zoom:12,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
    var housePosition={lat: parseFloat(_lat), lng: parseFloat(_lng)};
    var marker = new google.maps.Marker({
        position: housePosition,
        map: map,
        title: _title
        });
    }
