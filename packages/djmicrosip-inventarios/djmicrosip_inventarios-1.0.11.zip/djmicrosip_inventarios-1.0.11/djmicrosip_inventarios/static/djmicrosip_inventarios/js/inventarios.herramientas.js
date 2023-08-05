function cerrar_inventario(){
  $.ajax({
      url:'/inventarios/close_inventario_byalmacen_view/', 
      type : 'get', 
      data:{
        'almacen_id' : $("#almacen_id").val(),
      }, 
      success: function(data){ 
        alert(data.mensaje);
        window.location = "/inventarios/almacenes/";
      },
      error: function() {
        },
    });  
}

function AgregarArticuloSinExistencia(args){
  var $triggerBtn = args.$triggerBtn

  mostrar_articulos_agregados = function(data){
    if (data.articulos_agregados > 0)
    {
      mensaje ='Se agregaron '+ data.articulos_agregados+ ' Articulos'
      if (data.articulo_pendientes > 0)
        mensaje = 'La aplicacion solo genero ' + data.articulos_agregados+ ' Articulos, faltaron de generar '+data.articulo_pendientes + ' Articulos.'
      alert(mensaje);
    }
    else
    {
      if (data.message != '')
        alert(data.message);
      else
        alert('No hay articulos por inicializar');
    }
  }

  AddArticles = function(){
    if ( $triggerBtn.attr("disabled") == "disabled")
      return false

    $triggerBtn.hide();
    $triggerBtn.attr("disabled",true);
    $("#btnCancel").hide()
    $("#id_agregando_span, #id_agregando_span_all").attr("class","");

    $.ajax({
      url:'/inventarios/add_articulossinexistencia/', 
      type : 'get', 
      data:{
        'almacen_id' : $("#almacen_id").val(),
      }, 
      success: function(data){ 
        mostrar_articulos_agregados(data)
        $("#articulosnocont_porlinea_Modal, #articulosnocont_Modal").modal("hide")
        $("#btnCancel").show()
      },
      error: function() {
        alert('fallo algo')
      },
    }); 
  }

  $triggerBtn.on("click", function(){
    AddArticles()
  })
}

AgregarArticuloSinExistencia({
  $triggerBtn: $("#btn_agregar_articulosinexistencia"),
})