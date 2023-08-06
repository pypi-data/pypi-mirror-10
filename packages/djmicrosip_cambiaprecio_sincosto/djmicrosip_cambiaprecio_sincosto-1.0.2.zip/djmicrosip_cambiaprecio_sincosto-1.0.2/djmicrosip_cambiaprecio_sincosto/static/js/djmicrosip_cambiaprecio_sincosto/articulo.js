$("input[name$='precio']").each(function() {
	// alert($(this).val())
})

$(".precio_original_impuestos").each(function(){
	var precio_original = parseFloat($(this).parent().find("input[name$='precio']").val());
	var impuesto_porcentaje = parseFloat($("#id_impuesto_porcentaje").val()).toFixed(2);
	var valor = precio_original * (1+(impuesto_porcentaje/100));
	var $precio_nuevo = $(this).parent().parent().parent().find(".precio_mas_iva");
	$precio_nuevo.val(valor.toFixed(2));
	$(this).text(valor.toFixed(2));
})

$(".incremento").on("input",function(){
	
	if ($(this).val() == '') {
		$(this).val(0);
	};

	var precio_original = parseFloat($(this).parent().parent().find(".precio_original_impuestos").text());
	var $precio_nuevo = $(this).parent().parent().find(".precio_mas_iva");
	var porcentaje_incremento = parseFloat($(this).val());
	$precio_nuevo.val((precio_original*(1+(porcentaje_incremento/100))).toFixed(2))
	$precio_nuevo.trigger("change");
});

$(".precio_mas_iva").on("change",function(){
	actualiza_precio_original($(this));

});

$(".precio_mas_iva").on("input",function(){
	var $incremento = $(this).parent().parent().find(".incremento");
	var precio_nuevo = parseFloat($(this).val());
	var precio_original = parseFloat($(this).parent().parent().find(".precio_original_impuestos").text());
	var incremento = (precio_nuevo * 100 / precio_original)-100;
	$incremento.val(incremento.toFixed(2));
	actualiza_precio_original($(this));
	if (true) {};
});

function actualiza_precio_original($precio_mas_iva){
	var $precio_original = $precio_mas_iva.parent().parent().find("input[name$='precio']");
	var impuesto_porcentaje = parseFloat($("#id_impuesto_porcentaje").val()).toFixed(2);
	var precio_original = parseFloat(parseFloat($precio_mas_iva.val())/(1+(impuesto_porcentaje/100))).toFixed(2);
	$precio_original.val(precio_original);
}