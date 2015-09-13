<script>
/* Data points defined as an array of LatLng objects */

function initMap() {
	var heatmapData = [
	new google.maps.LatLng(37.782, -122.447),
	new google.maps.LatLng(37.782, -122.445),
	new google.maps.LatLng(37.782, -122.443),
	new google.maps.LatLng(37.782, -122.441),
	new google.maps.LatLng(37.782, -122.439),
	new google.maps.LatLng(37.782, -122.437),
	new google.maps.LatLng(37.782, -122.435),
	new google.maps.LatLng(37.785, -122.447),
	new google.maps.LatLng(37.785, -122.445),
	new google.maps.LatLng(37.785, -122.443),
	new google.maps.LatLng(37.785, -122.441),
	new google.maps.LatLng(37.785, -122.439),
	new google.maps.LatLng(37.785, -122.437),
	new google.maps.LatLng(37.785, -122.435)
	];

	var sanFrancisco = new google.maps.LatLng(37.774546, -122.433523);


	map = new google.maps.Map(document.getElementById("googleMap"), {
		zoom: 13,
		center: sanFrancisco,
		mapTypeId: google.maps.MapTypeId.SATELLITE
	});

	heatmap = new google.maps.visualization.HeatmapLayer({
		data: heatmapData,
		map: map
	});
	heatmap.setMap(map);
	}
google.maps.event.addDomListener(window, 'load', initMap);
</script>