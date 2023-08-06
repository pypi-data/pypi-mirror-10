//TODO
$(document).ready(function(){
	$(".bootfile").on('click', function(){
		$(".chosen-bootfile").removeClass("chosen-bootfile");
		$this = $(this)
		$.ajax({
				url:"/bootcode/",
				type:"POST",
				data:{file:$(this).find("p").first().text()},
				success: function(data, status){

					$this.addClass("chosen-bootfile");
				},error:function(x, status, error){
					console.log(x, status, error);
				}
			});
	});
});