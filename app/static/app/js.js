function refresh_map () {
	$.ajax({
		type:"POST",
		url: "getmarkers",
		success: function (data) {
			if (data.status == "success") {
				data.pins = JSON.parse(data.pins)
				console.log(data);
				//fetch pins from data.pins and display them
				for (var i = 0; i < data.pins.length; i++) {
					var pt_lat_lng = new google.maps.LatLng(data.pins[i].latitude, data.pins[i].longitude);
					var loc = new google.maps.Marker({
						    position: pt_lat_lng,
						    title: data.pins[i].title
					});
					loc.setMap(map);
				}
			}
		}
	})
};

$(document).ready(function() {
	refresh_map();

	$('#su_s').on('click', function () {
		var user = $('#su_u').val();
		var pass = $('#su_p').val();
		$.ajax({
			type:"POST",
			url: "signup",
			data: {
				user: user,
				pass: pass
			},
			success: function (data) {
				//data is the success message
				$('#message').show();
				$('#message').text('Message: Login created. Now please sign in.');
			}
		})
	});
	
	$('#si_s').on('click', function () {
		var user = $('#si_u').val();
		var pass = $('#si_p').val();
		$.ajax({
			type:"POST",
			url: "signin",
			data: {
				user: user,
				pass: pass
			},
			success: function (data) {
				if (data.status == "success") {
					$('#message').show();
					$('#message').text('Message: Login successful. Thank you.');
					$('#currentuser').text('Logged in as: ' + data.name);
				} else {
					$('#message').show();
					$('#message').text('Message: Login failed. Please try again.');
				}
			}
		})
	});
	
	$('#ap_s').on('click', function () {
		var title = $('#title').val();
		var desc = $('#desc').val();
		var lat = marker.position.lat;
		var lng = marker.position.lng;
		$.ajax({
			type:"POST",
			url: "addmarker",
			data: {
				title: title,
				desc: desc,
				latitude: lat,
				longitude: lng
			},
			success: function (data) {
				if (data == "success") {
					//refresh map
					refresh_map();
				}
			}
		})
	});
})
