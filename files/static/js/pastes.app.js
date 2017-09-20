$(document).ready(function() {
	$('#submit_paste').click(function() {
		var paste = $('#paste');

		if (paste.val().length > 0) {
			// This is kinda hacky, but I'm not sure how to avoid hard coding the url here
			var paste_url = window.location.pathname; 
			$.post(paste_url, { 'paste': paste.val() })
			.done(function(data) {
				if (data['status'] == 200 && data['url'] != "") {
					window.location = data['url'];
				} else {
					$('#errors').html('<p>'+data['msg']+'</p>');
				}
			}).fail(function(data) {
				alert('Something broke');
			});
		} else {
			alert('You have to paste something to upload it here.');
		}
	});
});