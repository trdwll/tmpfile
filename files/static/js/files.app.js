$(document).ready(function() {
	$('#pbar').hide();
	$('#upload_file').click(function() {
		$("#selected_file").trigger('click');
	});

	$('#upload').fileupload({
		send: function(e, data) {
			$('#pbar').show();
			$('#kewlurldude').empty();
			$('#upload_file').toggleClass('is-loading');
		},
		progressall: function (e, data) {
			var progress = data.loaded / data.total * 100;
			$('#pbar').val(progress);

			$('#prog').text(progress.toFixed(2)+'% / 100.00%');
			if (progress >= 100) {
				$('#prog').text('Upload complete!\nWe\'re processing your link and checksums, please wait!');
			}
		},
		done: function(e, data) {
			if (data.result["status"] == 200 && data.result["msg"] == "Ok") {
				$('#kewlurldude').html('Here\'s a direct link to the file you just uploaded: <br /><a href="'+data.result["url"]+'">'+data.result["url"]+'</a><br /><br />'+
					'<div class="box notification is-warning">'+
						'<p>'+
							'Here are the <a href="https://en.wikipedia.org/wiki/File_verification">checksums</a> of the file that you just uploaded.'+
							'Verify these with your local copy, if they\'re not the same contact us.'+
							'<ul>'+
								'<li>sha1: <code class="small">'+data.result["checksums"][0]+'</code></li>'+
								'<li>sha256: <code class="small">'+data.result["checksums"][1]+'</code></li>'+
								'<li>sha512: <code class="smaller">'+data.result["checksums"][2]+'</code></li>'+
							'</ul>'+
						'</p>'+
					'</div>'
				);
			} else { 
				$('<div class="notification is-danger">'+data.result["msg"]+'</div>').appendTo('#errors');
			}

			// Get rid of uploading displays
			$('#pbar').hide();
			$('#upload_file').toggleClass('is-loading');
			$('#prog').empty();
		}
	});
});