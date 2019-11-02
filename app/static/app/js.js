$(document).ready(function() {
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
				return;
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
	
	$('#addmarker').on('click', function () {
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
					//close form and refresh page
				}
			}
		})
	});
	
	$('.getmarkers').on('click', function () {
		$.ajax({
			type:"POST",
			url: "getmarkers",
			success: function (data) {
				if (data.status == "success") {
					//fetch pins from data.pins and display them
				}
			}
		})
	});
})
