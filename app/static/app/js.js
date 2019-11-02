$(document).ready(function() {
	//csrftoken = $.cookie('csrftoken');

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
				if (data == "success") {
					$('#message').show();
					$('#message').text('Message: Login successful. Thank you.');
				} else {
					$('#message').show();
					$('#message').text('Message: Login failed. Please try again.');
				}
				//Data could be success or failure
			}
		})
	});
})
