$(document).ready(function(){
	/**function:ready_scheduled_1
	POSTs a cancelling request
	*/
	$(".glyphicon-remove").on("click", function(){
		$remove_btn = $(this);
		$.ajax({
			type: "POST",
			url: "/cancel/",
			data: {id: $remove_btn.closest(".panel").find("#identifier").text()},
			beforeSend: function(){
				
			}, success:function(data){
				$remove_btn.closest(".panel").hide(400, "swing", function(){
					$remove_btn.remove();
				});
			}, error:function(err){
				console.log("error: "+err)
			}
		});

		
	});
});