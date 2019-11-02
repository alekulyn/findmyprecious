$(document).ready(function() {
	$('#su_s').on('click', function () {
		var user = $('#su_u').val();
		var pass = $('#su_p').val();
		$.ajax({
			type:"GET",
			url: "signup",
			data: {
				user: user,
				pass: pass
			},
			success: function (data) {
				return;
			}
		})
	});
	
	$('#si_s').on('click', function () {
		var user = $('#si_u').val();
		var pass = $('#si_p').val();
		$.ajax({
			type:"GET",
			url: "signin",
			data: {
				user: user,
				pass: pass
			},
			success: function (data) {
				
			}
		})
	});
})
