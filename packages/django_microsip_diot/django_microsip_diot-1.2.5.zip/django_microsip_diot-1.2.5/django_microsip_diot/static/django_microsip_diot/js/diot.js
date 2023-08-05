var page = 1;
var id_selected=0;
$("#integradas").trigger("change");
// $("#inicio_ext").hide();
// MODAL DE PAGOS PARCIALES
var $tasa_iva_modal = $("#tasa_iva_modal");
var $importe_sin_iva_modal = $("#importe_sin_iva_modal");
var $proporcion_modal = $("#proporcion_modal");
var $iva_acreditable_modal = $("#iva_acreditable_modal");
var $iva_sin_acreditar_modal = $("#iva_sin_acreditar_modal");
var $iva_retenido_modal = $("#iva_retenido_modal");
var $descuento_modal = $("#descuento_modal");
var $id_xml = $("#id_xml");

// MODAL DE CAPTURA MANUAL
var $tasa_iva_manual = $("#tasa_iva_manual");
var $importe_sin_iva_manual = $("#importe_sin_iva_manual");
var $proporcion_manual = $("#proporcion_manual");
var $iva_acreditable_manual = $("#iva_acreditable_manual");
var $iva_sin_acreditar_manual = $("#iva_sin_acreditar_manual");
var $iva_retenido_manual = $("#iva_retenido_manual");
var $descuento_manual = $("#descuento_manual");

$("#integradas").on("change",function(){
	if ($(this).is(":checked"))
	{
		$(".diot_xml").show();
	}
	else
	{
		$(".diot_xml").hide();
		$(".diot_xml").find(".chk_repo").attr("checked",false);
	};
	var num_mostrados = String($("#tabla_repositorios").find("tr:visible").length-1);
	$("#paginacion").children().text('Mostrando '+num_mostrados+' de '+String(total))
});

$("#id_repos_ext").on("change",function(){
	if ($(this).is(":checked"))
	{
		$("#inicio_ext").show();
	}
	else
	{
		$("#inicio_ext").hide();
	};
});

$("#integrar").on("change",function(){
	var checked = $(this).is(":checked");
	$(".chk_repo:enabled").each(function(){

		$(this).attr("checked",checked);
		$(this).trigger("change");
	});
});

$("#sincronizar_catalogo").on("click",function(){
	$("#sincronizar_catalogo").attr("disabled",true);
	$.ajax({
		url:'/diot/exporta_proveedores',
		type:'get',
		data:{
		},
		success:function(data){
			if (data.nuevos > 0)
			{
				alert("se agregaron "+data.nuevos+" Proveedores nuevos.");
			}
			else
			{
				alert("Proceso Terminado.\nNo se agregaron nuevos proveedores.");
			};
			$("#sincronizar_catalogo").attr("disabled",false);
		},
		error:function(data){
			$("#sincronizar_catalogo").attr("disabled",false);
			alert("Error Interno en el servidor");
		}
	})
});

$("#crear_txt").on("click",function(){
	var checked_repos = $(".chk_repo:checked");
	var dic_diot = {}
	checked_repos.each(function(){
		var rfc = $(this).parent().parent().find("#rfc").text().trim();
		var nombre = $(this).parent().parent().find("#nombre").text();
		var id_fiscal = $(this).parent().parent().find("#id_fiscal").val();
		var importe = parseFloat($(this).parent().parent().find("#importe").text().replace("$ ",""));
		var iva = parseFloat($(this).parent().parent().find("#iva").text().replace("$ ",""));
		var iva_retenido = parseFloat($(this).parent().parent().find("#iva_retenido").val());
		var descuento = parseFloat($(this).parent().parent().find("#descuento").val());
		var subtotal = parseFloat($(this).parent().parent().find("#subtotal").val());
		var folio = $(this).parent().parent().find("#folio").text().trim();
		var tipo_comprobante = $(this).parent().parent().find("#tipo_comprobante").val();
		var pagado = parseFloat($(this).parent().parent().find("#pagado").text().replace("$ ",""));
		var pagado_h = parseFloat($(this).parent().parent().find("#pagado_h").val());
		var iva_descuentos = parseFloat($(this).parent().parent().find("#iva_descuentos").val());
		var iva_no_acreditable = parseFloat($(this).parent().parent().find("#iva_no_acreditable").val());
		var ieps = parseFloat($(this).parent().parent().find("#ieps").val());
		var extranjero = 'N'
		debugger;
		if (rfc == "None")
		{
			rfc=id_fiscal;
			extranjero = 'S'
		}
		var tasa0 = 0;
		var tasa16 = 0;

		if (descuento>0)
		{
			if ($(this).parent().parent().attr("style") != "background-color: bisque;")
			{
				importe = subtotal-descuento;
			}
			else
			{
				if (iva == 0)
				{
					importe = pagado-pagado_h;
				}
				else
				{
					importe = pagado-(pagado_h/1.16);
				};
			};

		};

		if (subtotal>importe && descuento>0)
		{
			subtotal=importe;
		};


		if (iva == 0)
		{
			if ($(this).parent().parent().attr("style") != "background-color: bisque;")
			{
				tasa0 = subtotal;
				iva = 0;
			}
			else
			{
				tasa0 = subtotal;
				iva = tasa16*0.16;
			}
			
		}
		else
		{
			if ($(this).parent().parent().attr("style") != "background-color: bisque;")
			{
				tasa16 = iva *100/16;
				tasa0 = subtotal-tasa16;
			}
			else
			{
				tasa16 = subtotal;
				iva = tasa16*0.16;
			}
			// tasa16 = subtotal;
			// iva = tasa16 *.16
		};
		importe = subtotal

		if (tasa0 >= ieps)
		{
			tasa0 = tasa0-ieps;
		};

		if (rfc in dic_diot == false){
			dic_diot[rfc] = {}
			dic_diot[rfc]['extranjero'] = extranjero
			dic_diot[rfc]['nombre'] = nombre
			dic_diot[rfc]['tasa0'] = 0
			dic_diot[rfc]['tasa16'] = 0
			dic_diot[rfc]['retenido'] = 0
			dic_diot[rfc]['iva_no_acreditable'] = 0
			dic_diot[rfc]['iva_descuentos'] = 0
			dic_diot[rfc]['detalles'] = []
		}
		
			dic_diot[rfc]['tasa0'] += tasa0;
			dic_diot[rfc]['tasa16'] += tasa16;
			dic_diot[rfc]['retenido'] += iva_retenido;
			dic_diot[rfc]['iva_no_acreditable'] += iva_no_acreditable;
			dic_diot[rfc]['iva_descuentos'] += iva_descuentos;
		

		dic_diot[rfc]['detalles'].push([String(folio),importe,iva])
	});
	var detallado=false;
	if (confirm("Desea Agregar los detalles por Proveedor al Archivo?")==true)
	{
		detallado = true;
	};

	checked_repos.each(function(){
		var integrar = 'N';
		var id = $(this).val();
		var row = $(this).parent().parent();	
		if (row.attr("style") != "background-color: bisque;")
		{

			$.ajax({
				url:'/diot/pago_total',
				type:'get',
				data:{
					'id': id,
				},
				success:function(data){
				},
				error:function(data){
				}
			});
		}
		else
		{
			var pago = parseFloat($(this).parent().parent().find("#pagado").text().replace("$ ",""));
			$.ajax({
				url:'/diot/pago_parcial',
				type:'get',
				data:{
					'id': id,
					'pago':pago,
				},
				success:function(data){
				},
				error:function(data){
				}
			});
		};				
	});


	$.ajax({
		url:'/diot/create_file',
		type:'get',
		data:{
			'dic_diot':JSON.stringify(dic_diot),
			'fecha_inicio':fecha_inicio,
			'detallado':detallado,
		},
		success:function(data){
			
		},
		error:function(data){
			alert("Error.\nSe recomienda Sincronizar el Catalogo de Proveedores antes de generar el archivo.");
		},
		complete:function(){
			window.location.replace(this.url);

		}
	})
});

// $(window).scroll(function() {
//    if($(window).scrollTop() + $(window).height() == $(document).height()) {
//        page+=1;
//        $.ajax({
//       		url:'/diot/paginacion',
//       		type:'get',
//       		data:{
//       			'page':page,
//       			'fecha_inicio':fecha_inicio,
//       			'fecha_fin':fecha_fin,
//       			'inicio_ext':inicio_ext,
//       			'repos_ext':repos_ext,
//       		},
//       		success:function(data){
//       			if (!data.error)
//       			{
					
//       				data.pagina.forEach(function(repo){

//       					var options = { year: "numeric", month: "long",
//       						day: "numeric" };
//       					var style = "";
//       					var fecha = new Date(repo[0].fecha);
//       					var fecha_ini = new Date(fecha_inicio);
//       					fecha_string = fecha.toLocaleDateString("es-es",options);
      					
//       					debugger;
//       					$('#tabla_repositorios').find('tbody').append( "<tr> <td> <input type='checkbox' class='chk_repo' value='"+repo[0].id+"'>  </td><td id='fecha' "+style+"><small>"+fecha_string+"</small></td> <td id='folio'> "+  repo[0].folio+"<input type='hidden' id='tipo_comprobante' value='"+repo[0].tipo_comprobante+"''></td> <td id='nombre'><small>"+repo[0].nombre+"</small><input type='hidden' id='pagado_h' value='"+repo[0].pagado+"}}'><input type='hidden' id='pago' value='0'></td><td id='rfc'>"+repo[0].rfc+" <input type='hidden' id='id_fiscal' value='"+repo[0].taxid+"'></td><td id='pagado' class='text-right'>$ "+repo[0].pagado+"</td><td id='importe' class='text-right'>$ "+repo[0].importe+"</td> <td id='iva' class='text-right'>$ "+repo[1]+"<input type='hidden' id='subtotal' value='"+repo[2]+"'>  <input type='hidden' id='descuento' value='"+repo[3]+"'> <input type='hidden' id='iva_retenido' value='"+repo[4]+"'></td><td><button class='btn options' data-toggle='modal' data-target='#options_Modal' ><i class='glyphicon glyphicon-usd'></i></button></td></tr>" );
//       					var $row = $('#tabla_repositorios').find('tbody').find("tr").last();
//       					if (repo[0].pagado >= repo[0].importe)
//       					{
//       						$row.addClass("diot_xml");
//       						$row.find(".options").remove();
//       					};

//       					if (fecha<fecha_ini)
//       					{
//       						$row.find("#fecha").addClass("extemporanea");
//       					};

//       					if (repo[0].integrar == 'S')
//       					{
      						
//       						if (parseFloat(repo[0].pagado < repo[0].importe))
//       						{
//       							$row.attr("style","background-color: bisque;");
//       						};
//       					};
      					
//       				});
//       				var num_mostrados = String($("#tabla_repositorios").find("tr").length-1);
//       				total = data.total;
//       				$("#paginacion").children().text('Mostrando '+num_mostrados+' de '+String(total))
//       			}
      			
//       		},
//       		error:function(data){
//       		}
//        });

//    }
// });

$("#crear_paises").on("click",function(){
	$("#crear_paises").attr("disabled",true);
	$.ajax({
		url:'/diot/crear_paises',
		type:'get',
		data:{
		},
		success:function(data){
			if (data.nuevos > 0)
			{
				alert("se agregaron "+data.nuevos+" Paises nuevos.");
			}
			else
			{
				alert("Proceso Terminado.\nNo se agregaron nuevos paises.");
			};
			$("#crear_paises").attr("disabled",false);
		},
		error:function(data){
			$("#crear_paises").attr("disabled",false);
			alert("Error Interno en el servidor");
		}
	})
});

$(".chk_repo").on("change",function(){

	var row = $(this).parent().parent();
	if ((row.attr("style") == "background-color: bisque;") && (!$(this).is(":checked")) )
	{
		$(this).attr("disabled",true);
		var pagado_inicial = row.find("#pagado_h").val()
		row.find("#pagado").text("$ "+pagado_inicial);
	}
	
	var integrar = 'S';
	var id = $(this).val();
	if (!$(this).is(":checked"))
	{
		integrar = 'N'
	};
	$.ajax({
		url:'/diot/change_xml_status',
		type:'get',
		data:{
			'integrar':integrar,
			'id': id,
		},
		success:function(data){
		},
		error:function(data){
		}
	})
});

// COMPONENTES DE MODAL DE CAPTURA DE PAGOS PARCIALES
$(".options").on("click",function(){
	$id_xml = $(this).parent().parent().find(".chk_repo");
	var importe = parseFloat($(this).parent().parent().find("#importe").text().replace("$ ",""));
	var iva = parseFloat($(this).parent().parent().find("#iva").text().replace("$ ",""));
	var iva_retenido = parseFloat($(this).parent().parent().find("#iva_retenido").val());
	var descuento = parseFloat($(this).parent().parent().find("#descuento").val());
	var pagado = parseFloat($(this).parent().parent().find("#pagado").text().replace("$ ",""));
	var subtotal = parseFloat($(this).parent().parent().find("#subtotal").val());
	var pagado_h = parseFloat($(this).parent().parent().find("#pagado_h").val());
	var importe_sin_iva;


	if (descuento>0)
	{
		if ($(this).parent().parent().attr("style") != "background-color: bisque;")
		{
			importe = subtotal-descuento;
		}
		else
		{
			if (iva == 0)
			{
				importe = importe-pagado_h;
			}
			else
			{
				importe = (importe-pagado_h)/1.16;
			};
		};

	}
	else
	{
		if (iva == 0)
		{
			importe = importe-pagado_h;
		}
		else
		{
			importe = (importe-pagado_h)/1.16;
		};
	};

	if (subtotal>importe)
	{
		subtotal=importe;
	};

	if (iva==0)
	{
		importe_sin_iva = importe
		$tasa_iva_modal.val(0);
		$proporcion_modal.attr("disabled",true);
		$iva_acreditable_modal.attr("disabled",true);
		$iva_sin_acreditar_modal.attr("disabled",true);
		$iva_retenido_modal.attr("disabled",true);
	}
	else
	{
		importe_sin_iva = importe
		$tasa_iva_modal.val(16);
		$proporcion_modal.attr("disabled",false);
		$iva_acreditable_modal.attr("disabled",false);
		$iva_sin_acreditar_modal.attr("disabled",false);
		$iva_retenido_modal.attr("disabled",false);
	};
	$importe_sin_iva_modal.val(parseFloat(importe_sin_iva.toFixed(2)));
	$proporcion_modal.val(1.0);
	var iva_acreditable = ($importe_sin_iva_modal.val()*$proporcion_modal.val()*$tasa_iva_modal.val()/100).toFixed(2);
	$iva_acreditable_modal.val(iva_acreditable);
	$iva_sin_acreditar_modal.val(0);
	$iva_retenido_modal.val(iva_retenido);
	$descuento_modal.val(0);
});

$("#tasa_iva_modal").on("change",function(){
	if ($("#tasa_iva_modal").val()==0)
	{
		$proporcion_modal.attr("disabled",true);
		$iva_acreditable_modal.attr("disabled",true);
		$iva_sin_acreditar_modal.attr("disabled",true);
		$iva_retenido_modal.attr("disabled",true);
	}
	else
	{
		
		$proporcion_modal.attr("disabled",false);
		$iva_acreditable_modal.attr("disabled",false);
		$iva_sin_acreditar_modal.attr("disabled",false);
		$iva_retenido_modal.attr("disabled",false);
	};
});

$("#proporcion_modal").on("input",function(){
	$iva_acreditable_modal.val($importe_sin_iva_modal.val()*$proporcion_modal.val()*$tasa_iva_modal.val()/100);
	$iva_sin_acreditar_modal.val($importe_sin_iva_modal.val()*(1-$proporcion_modal.val())*$tasa_iva_modal.val()/100);
});

$("#importe_sin_iva_modal").on("input",function(){
	$proporcion_modal.trigger("input");
});

$("#modificar_xml").on("click",function(){
	var pagado = parseFloat($id_xml.parent().parent().find("#pagado").text().replace("$ ",""));
	var pagado_final;
	var $row = $id_xml.parent().parent();
	$row.attr("style","background-color: bisque;");
	$('.tags-modal-md').modal('hide');
	$row.find(".chk_repo").attr("checked","checked");
	$row.find(".chk_repo").attr("disabled",false);

	$row.find("#iva_descuentos").val($descuento_modal.val());
	$row.find("#iva_no_acreditable").val($iva_sin_acreditar_modal.val());
	$row.find("#iva_retenido").val($iva_retenido_modal.val());
	if ($(tasa_iva_modal).val()!=0)
	{
		var importe_mas_iva = parseFloat(($importe_sin_iva_modal.val() * (1+($tasa_iva_modal.val()/100))).toFixed(2));
		pagado_final = importe_mas_iva+pagado;
		$row.find("#subtotal").val(parseFloat($importe_sin_iva_modal.val()));
	}
	else
	{	
		pagado_final = parseFloat($importe_sin_iva_modal.val())+pagado;
		$row.find("#subtotal").val(parseFloat($importe_sin_iva_modal.val()));
	}
	
	$row.find("#pagado").text("$ "+pagado_final)
});


// COMPONENTES DE MODAL DE CAPTURA MANUAL
$("#tasa_iva_manual").on("change",function(){
	if ($("#tasa_iva_manual").val()==0)
	{
		$proporcion_manual.attr("disabled",true);
		$proporcion_manual.val(0);
		$proporcion_manual.trigger("input");

		$iva_acreditable_manual.attr("disabled",true);
		$iva_sin_acreditar_manual.attr("disabled",true);
		$iva_retenido_manual.attr("disabled",true);
	}
	else
	{
		
		$proporcion_manual.attr("disabled",false);
		$proporcion_manual.val(1);
		$proporcion_manual.trigger("input");
		$iva_acreditable_manual.attr("disabled",false);
		$iva_sin_acreditar_manual.attr("disabled",false);
		$iva_retenido_manual.attr("disabled",false);
	};
});

$("#proporcion_manual").on("input",function(){
	$iva_acreditable_manual.val($importe_sin_iva_manual.val()*$proporcion_manual.val()*$tasa_iva_manual.val()/100);
	$iva_sin_acreditar_manual.val($importe_sin_iva_manual.val()*(1-$proporcion_manual.val())*$tasa_iva_manual.val()/100);
});

$("#importe_sin_iva_manual").on("input",function(){
	$proporcion_manual.trigger("input");
});

$("#captura_manual").on("click",function(){
	var id = $("#id_proveedor").val();
	var lista = $("#id_fecha_manual").val().split("/");
	var nueva_fecha = lista[1]+"/"+lista[0]+"/"+lista[2]
	var fecha_serv = lista[2]+"-"+lista[1]+"-"+lista[0]
	var fecha = new Date(nueva_fecha);
	var options = { year: "numeric", month: "long",
      				day: "numeric" };
	var fecha_string = fecha.toLocaleDateString("es-es",options);
	var folio = $("#folio_manual").val();
	var nombre;
	var rfc;
	var importe = parseFloat($("#importe_sin_iva_manual").val()) + parseFloat($("#iva_acreditable_manual").val())
	$('.tags-modal-md').modal('hide');
	$.ajax({
		url:'/diot/captura_manual',
		type:'get',
		data:{
			'id_proveedor':id,
			'folio':folio,
			'fecha':fecha_serv,
			'importe':importe,
			'subtotal':$("#importe_sin_iva_manual").val(),
			'iva_acreditable':$("#iva_acreditable_manual").val(),
			'iva_no_acreditable':$("#iva_sin_acreditar_manual").val(),
			'iva_retenido':$("#iva_retenido_manual").val(),
			'iva_descuentos':$("#descuento_manual").val(),
		},
		success:function(data){
			nombre = data.nombre;
			rfc = data.proveedor_rfc;
			
			$('#tabla_repositorios').find('tbody').append( "<tr>"+
				"<td> <input type='checkbox' class='chk_repo' value='"+id+"' checked='checked'></td>"+
				"<td id='fecha'><small>"+fecha_string+"</small></td>"+
				"<td id='folio'> "+ folio+"</td>"+
				"<td id='nombre'><small>"+nombre+"</small></td>"+
				"<td id='rfc'>"+rfc+" </td>"+
				"<td id='pagado' class='text-right'>-</td>"+
				"<td id='importe' class='text-right'>$ "+importe+"</td>"+
				"<td id='iva' class='text-right'>$ "+$("#iva_acreditable_manual").val()+""+
					"<input type='hidden' id='subtotal' value='"+$("#importe_sin_iva_manual").val()+"'>"+
					"<input type='hidden' id='descuento' value=''>"+
					"<input type='hidden' id='iva_retenido' value='"+$("#iva_retenido_manual").val()+"'>"+
					"<input type='hidden' id='iva_no_acreditable' value='"+$("#iva_sin_acreditar_manual").val()+"'>"+
					"<input type='hidden' id='iva_descuentos' value='"+$("#descuento_manual").val()+"'>"+
				"</td>"+
				"<td></td>"+
				"<td></td>"+
			"</tr>" );
			$("#id_fecha_manual").val('');
			$("#folio_manual").val('');
			$("#proveedor_manual").find("#id_proveedor-deck").children().children().trigger("click");
			$("#importe_sin_iva_manual").val('');
			$("#proporcion_manual").val(1);
			$("#iva_acreditable_manual").val(0);
			$("#iva_sin_acreditar_manual").val(0);
			$("#iva_retenido_manual").val(0);
			$("#iva_descuentos").val(0);
		},
		error:function(data){
			alert("Error Interno en el servidor");
		}
	});
	
});

$(".remove").on("click",function(){
	 var row = $(this).parent().parent();
	 var id = row.find(".chk_repo").val();
	 var manual = 0;
	 if (row.find("#pagado").text() == '-') {manual = 1};
	 if (confirm("Seguro que desea dejar de mostrar este registro?")==true)
	 {
	 	$.ajax({
	 		url:'/diot/ocultar_repo',
	 		type:'get',
	 		data:{
	 			'id':id,
	 			'manual':manual,
	 		},
	 		success:function(data){
	 			row.hide();
	 			row.find(".chk_repo").attr("checked",false);
	 			row.find(".chk_repo").attr("disabled",true);
	 		},
	 		error:function(data){
	 			alert("Error Interno en el servidor");
	 		}
	 	});
	 };
});