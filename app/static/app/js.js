blue_icon = {
	      url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
}
red_icon = {
	      url: "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
}
green_icon = {
	      url: "http://maps.google.com/mapfiles/ms/icons/green-dot.png"
}

function refresh_map () {
	$.ajax({
		type:"POST",
		url: "getmarkers",
		success: function (data) {
			if (data.status == "success") {
				data.pins = JSON.parse(data.pins)
				//fetch pins from data.pins and display them
				for (var i = 0; i < data.pins.length; i++) {
					var pt_lat_lng = new google.maps.LatLng(data.pins[i].latitude, data.pins[i].longitude);
					var loc = new google.maps.Marker({
						position: pt_lat_lng,
						title: data.pins[i].title,
						icon: ((data.pins[i].found) ? green_icon : red_icon)
					});

					google.maps.event.addListener(loc, 'click', (function(loc, i) {
						return function () {
							if (infoWindow) {
								infoWindow.close()
							}
							var iw = new google.maps.InfoWindow({
								content: '<b>Reporter:</b> ' + data.pins[i].user + '<br>' +
									 '<b>Title:</b> ' + data.pins[i].title + '<br>' +
									 '<b>Description:</b> ' + data.pins[i].desc + '<br>'
							});
							infoWindow = iw;
							iw.open(map,loc);
						}
					})(loc, i));
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
					$('.hero').hide();
				} else {
					$('#message').show();
					$('#message').text('Message: Login failed. Please try again.');
				}
			}
		})
	});

	$('#logout').on('click', function () {
		$.ajax({
			type:"POST",
			url: "logout",
			success: function (data) {
				if (data == "success") {
					$('#message').text('Message: Logout successful. Thank you.');
					$('#currentuser').text('Logged in as: guest');
					$('.hero').show();
				}
			}
		})
	});
	
	$('#ap_s').on('click', function () {
		var title = $('#title').val();
		var desc = $('#desc').val();
		var lat = marker.position.lat;
		var lng = marker.position.lng;
		var found = $('input[name=itemtype]:checked').val() == "found";
		$.ajax({
			type:"POST",
			url: "addmarker",
			data: {
				title: title,
				desc: desc,
				latitude: lat,
				longitude: lng,
				found: found
			},
			success: function (data) {
				if (data == "success") {
					//refresh map
					refresh_map();
					//clear temporary pin and pin fields
					marker.setMap(null);
					marker = null;
					$('title').val('');
					$('desc').val('');
					$('input[name=itemtype]').prop('checked', false);
				}
			}
		})
	});
})
