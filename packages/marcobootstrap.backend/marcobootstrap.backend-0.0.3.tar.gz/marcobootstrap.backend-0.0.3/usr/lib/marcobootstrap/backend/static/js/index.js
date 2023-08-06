function nodo(info){
	/**function:nodo(info)
		Generates the node HTML string.
	*/
    var cadena = "<div class='node not-chosen'>";
    cadena += "<p class='ip'>"+info+"</p>";
    cadena += "<input class='deploy' type='checkbox'></input>"
    cadena += "</div>";
    return cadena;
}

$(document).ready(function(){
  /**function:ready_line_12(line 12)
	Waits for the page to be fully loaded 
	in order to securely perform operations.
	Then it requests the information about the nodes
	on the network
  */
  $.ajax({
    url:"/nodes/",
    type: 'GET',
    success: function(nodes, textStatus, x){
      var html_nodes = "";
      $("#count").text(nodes.length)
      for(var ip in nodes){
        html_nodes += nodo(nodes[ip]);
      }
      $("#listanodos").html("").append(html_nodes);

    },
    error: function(x, status, error){
    	console.log("Error en la detección de los nodos")
    },
    dataType: 'json'
  });

});


$(document).ready(function(){
	/**function:ready_line42(line 42)
		Creates the main panel and binds the click events,
		time picker and other 
	*/
	$("#schedule").prop("disabled", false);
	$('#datetimepicker').datetimepicker({
		minDate: new Date()
	});

	$(".glyphicon-remove").on("click", function(){
		if(confirm("¿Está seguro de que desea eliminar esta imagen? Esta acción es irreversible")){
			var $tarfile = $(this).closest(".tarfile");
			var filename = $tarfile.find("p").text();

			$.ajax({
				url:"/removetar/",
				type:"POST",
				data:{file:filename},
				success: function(data, status){
					$tarfile.hide(400, "swing", function(){
						$tarfile.remove();
					});
				},error:function(x, status, error){
					console.log(x, status, error);
				}
			});

		}else{
			console.log("No eliminar");
		}
	});

	$("#listanodos").on('click', "input[type=checkbox]", function(){
        console.log($(this).closest(".node").toggleClass("chosen").toggleClass("not-chosen"));
    });

	$(".tarfile").on("click", function(){
		if($(this).hasClass("list-group-item-info")){
			$(this).removeClass("list-group-item-info");
		}else{
			$(".list-group-item-info").removeClass("list-group-item-info");
			$(this).addClass("list-group-item-info");
		}
		
	});

	$("#schedule").on('click', function(){
		$(".alert.alert-success").hide();
		$(".alert.alert-danger").hide();
		$nodos = $(".deploy:checked");
		var nodos_str="";
		if($nodos.length < 1){
			alert("Debe elegir al menos un nodo sobre el que realizar la acción");
			return;
		}else{
			$nodos.each(function(index, element){
				nodos_str+=$(element).siblings(".ip").text() + ",";
			});
		}

		$schedule_btn = $(this);
		$(this).prop("disabled", true);

		var operation = $("#operation").val();

		if(operation == "update" && $(".list-group-item-info").length < 1){
			alert("Debe elegir una imagen a instalar");
			$(this).prop("disabled", true);
		}

		schedule_date = $('#datetimepicker').val();

		schedule_date = new Date(schedule_date);
		var aux = new Date().getTime();


		if ( Object.prototype.toString.call(schedule_date) === "[object Date]" ) {
  			//http://stackoverflow.com/a/1353711/2628463
	  		if ((!isNaN(schedule_date.getTime())) && aux < schedule_date.getTime())  {  // schedule_date.valueOf() could also work
	    		
	    		date_seconds = schedule_date.getTime()/1000.0;
	    		
	    		$.ajax({
					type:"POST",
					url:"/schedule/",
					data:{schedule: date_seconds, 
						nodes:nodos_str, 
						operation: $("#operation").val(),
						image: $(".list-group-item-info").find("p").first().text()},
					traditional:true,
					beforeSend:function(){

					},success:function(){
						$(".alert.alert-success").show(400, "swing");
					},error:function(err){
						$(".alert.alert-danger #errortext").text("Error. El servidor respondió: "+ err);
						$(".alert.alert-danger #errortext").show(400, "swing");
					}, complete: function(){
						$schedule_btn.prop("disabled", false);
					}
				});
	  		}else {
	    		alert("La fecha es inválida");// date is not valid
	  		}
		}else {
		  alert("Error en el formato");
		}
		$(this).prop("disabled", false);
	});
});