
// function InventarioManager(args) {
//   var $articulo = args.$articulo
//   var $ubicacion = args.$ubicacion
//   var $articuloContainer = $articulo.parent().parent()
//   var $submitBtn = args.$submitBtn
//   var $unidadesContiner = args.$unidadesContiner
//   var $unidades = args.$unidades
//   var $serie = args.$serie
//   var $serie_container = $serie.parent()
//   var almacen = args.almacen
//   var documentos = args.documentos
//   var $tipo_seguimiento = args.$tipo_seguimiento

//   var $articulo_clave = args.$articulo_clave
//   var $articulo_serie = args.$articulo_serie
//   var $articuloSerieContainer = $articulo_serie.parent().parent()
//   var $detailcontiner = args.$detailcontiner
//   var $manejarseries = args.$manejarseries
//   var $almacen = args.$almacen
//   var es_small = $("#extra_mobile_btn:visible").length>0;
//   var articulocontados_manager = new ManejadorArticulosContados({ almacen_nombre: almacen, })

//   var manejarseries = $manejarseries[0].checked
//   var tipo_seguimiento = 'N';
//   var modoRapido = $("#chbx_modorapido:checked").length>0
//   $($manejarseries).on('change', function(){
//     manejarseries = $manejarseries[0].checked
//     $articulo_serie.parent().parent().hide()
//     if (manejarseries) {
//       $serie.show()
//       $articulo_clave.hide()
//       $articulo_serie.focus()
//       $articulo.parent().hide()  

//     }
//     else{
//       $serie.hide()
//       $articulo_clave.show()
//       $articulo.focus()
//       $articulo.parent().show()   
//     }

    
//   })

//   if (es_small) {
//     $ubicacion = $("#ubicacionMobil")
//   }
//   $articulo_serie.parent().parent().hide()
//   $serie.hide()
//   $unidadesContiner.hide()
//   $detailcontiner.hide()
  
//   IsValid = function(){
//     if ($ubicacion.val() == ''){
//         alert("El campo ubicacion es obligatorio")
//         if (es_small){
//           $("#extra_mobile_btn").trigger("click")
//         }

//         $ubicacion.focus()
//         return false
//     }
//     else if ($articulo.find("option:selected").val() == undefined)
//     {
//       alert("El campo articulo es obligatorio")
//       $articulo.parent().find("input").focus()
//       return false
//     }
//     else if ($unidades.val() == '')
//     { 

//       alert("El campo unidades es obligatorio")
//       $unidades.show()
//       $unidades.focus()
//       return false
//     }
//     else if ($.isNumeric($unidades.val()) == false )
//     {
//       $unidades.show()
//       alert("Unidades incorrectas")
//       $unidades.focus()
//       return false
//     }

//     return true
//   }

  // ShowNewEntries = function(data){
  //   var $articulo_tr = $("#articulo-"+data.articulo_id).parent().parent()
  //   var contenido_existencia = data.existencia
  //   var span_class_name
  //   if (data.tipo_seguimiento=='S') {
  //     var span_class_name = "seriesSinContar"
  //     if (data.series_por_contar<=0) {
  //       span_class_name = "seriesContadas"
  //     }
  //     contenido_existencia += " <a href='#'> <span class='badge "+span_class_name+"'>Faltan "+data.series_por_contar+"</a>"
  //   }

  //   // Cuando ya existe en la tabla
  //   if ($articulo_tr.length>0)
  //   {
  //     $articulo_tr.children(":last").html(contenido_existencia);
  //     var temp = $articulo_tr.addClass("warning")[0]
  //     $articulo_tr.remove()
  //     $("#ultimos_articulos_contados tbody").prepend(temp)
  //   }
  //   // Si no existe en tabla
  //   else
  //   {  
  //     var contados = parseInt($("#articulosContadosId").text()) + 1
  //     $("#articulosContadosId").text(contados)
  //     $articulo_tr = "<tr class='warning'><td>"+data.articulo_clave+"<input type='hidden' id='articulo-"+data.articulo_id +"' value='"+data.articulo_id+"'/> </td><td>"+data.articulo_nombre+"</td><td>"+contenido_existencia+"</td></tr>"
  //     $("#ultimos_articulos_contados tbody").prepend($articulo_tr)
  //   }

  //   if (data.tipo_seguimiento=='S') 
  //   {  
  //     articulocontados_manager.StartSeriesAddEvents($articulo_tr, span_class_name)
  //   }

  //   $articulo.parent().find(".deck.div").find(".remove").trigger("click")
        
  //   if(es_small)
  //   {
  //     if($("#chbx_modorapido:checked").length>0)
  //     {

  //       $articulo_clave.show()
  //       $articulo_clave.focus()
  //       $articulo.parent().find("input").hide()
  //     }
  //     else
  //     {
  //       $articulo.parent().find("input").show()
  //       $articulo.parent().find("input").focus()
  //       $articulo_clave.hide();
  //     }
  //   }

  //   if (es_small)
  //   {
  //     $articulo.parent().hide()
  //   }
  //   else
  //   {
  //     $articulo_clave.show()
  //   }

  //   if (manejarseries) 
  //   {
  //     $articulo_serie.focus()
  //     $articulo.parent().hide()
  //     $articulo_clave.hide()
  //   }
  //   else
  //   {
  //     if (modoRapido && es_small)
  //     {  
  //       $articulo_clave.show()
  //     }
      
  //     if (modoRapido)
  //     {
  //       $articulo_clave.focus()
  //     }
  //     else
  //     {
  //       $articulo.parent().show()
  //       $articulo.parent().find("input").focus()
  //     }
  //   }
  //   $submitBtn.attr("disabled",false)
  //   if (es_small)
  //   {
  //     $("body").scrollTop(100)
  //   }
  // }

//   SendData = function(){
//     $submitBtn.attr("disabled",true)

//     // datos para enviar a servidor
//     data = {
//       'entrada_id': documentos.entrada_id,
//       'salida_id': documentos.salida_id,
//       'ubicacion': $ubicacion.val(),
//       'unidades': $unidades.val(),
//       'costo_unitario':0,
//       'articulo_id': $articulo.val()[0],
//       'almacen_nombre':almacen,
//       'tipo_seguimiento': $tipo_seguimiento.val()
//     }
//     if ($tipo_seguimiento.val() == 'S'){
//       data.serie =  $serie.val()
//     }

//     $.ajax({
//       url:'/inventarios/agregar_existencia/', 
//       type : 'get', 
//       data:data, 
//       success: function(data){
//         // Mostrar nuevas entradas
//         ShowNewEntries(data)
//       }
//     });


//   }

//   onSubmit = function(){
//     // Si el formulario es valido
//     if(IsValid()){
//       // Envia los datos
//       SendData()
//     }
//   } 

//   clearForm = function(){
//     $articulo_clave.val('')
//     $articulo_clave.show()
//     $articulo_serie.val('')
//     $unidades.val('')

//     $detailcontiner.hide()
//     $unidadesContiner.hide()
//     // $articulo_serie.attr("disabled",false);
//     if (manejarseries)
//     {
//       $articulo_serie.focus()
//       $articulo.parent().hide()
//     }
//   }

//   if (es_small== false){
//     $("#cancel_btn").hide()
//   }

//   showDetallesMovimientos = function($selected_article){
//      $.ajax({
//       url:'/inventarios/get_movimientos_articulo/', 
//       type : 'get', 
//       data:{
//         'almacen_id' : $almacen.val(),
//         'articulo_id': $selected_article.val()[0],
//       }, 
//       success: function(data){
//         var detalles = data.detalles
//         var articulo_nombre = $selected_article.parent().find(".deck.div").children().contents()[1].data
        
//         $("#modalMovmentsTitle").html("<h4>"+articulo_nombre+"</h4>")
          
//         var msg=  "<h4> Valores iniciales</h4> <strong>Existencia: </strong>"+ data.existencia_inicial+" <br/><h4> Movimientos</h4>\n <table class='table table-striped table-hover'><tr><th>Usuario/Ubicacion</th><th>Unidades</th><th>fecha</th></tr>";
//         for(detalle in detalles){
//           msg += "<tr><td>"+detalles[detalle].usuario+"/"+detalles[detalle].ubicacion+"</td><td>"+ detalles[detalle].unidades +'</td><td>' +detalles[detalle].fechahora+'</td></tr>';
//         }
//         msg+="</table>"
//         $("#movimiento_articulo_modal .modal-body").html(msg)
//         $("#movimiento_articulo_modal").modal()
//       },
//       error: function() {
//         alert('algo fallo')
//       },
//     });  
//   }

//   showControlsToAddExistence = function(args){
//     var ya_ajustado = args.ya_ajustado
//     tipo_seguimiento = args.articulo_seguimiento
//     $("#articuloSeguimientoUnidadesId").val(tipo_seguimiento)
//     // Si es seguimento por series y ya esta ajustado
//     if (tipo_seguimiento == 'S' && ya_ajustado){
//       $articulo.parent().find(".deck.div").find(".remove").trigger("click")
//       $articulo.parent().parent().hide()
//       $articulo_serie.focus()
//       alert('Serie ya contada en el inventario')
//     }
//     else{
//       var detalle_movimientos_link=""
//       if (ya_ajustado)
//       {
//         detalle_movimientos_link = "<a tabindex='-1' id='id_detalle_movimientos' href='#' role='button' data-toggle='modal'><i class='glyphicon glyphicon-info-sign icon-white'></i></a>"
//       }
//       $detailcontiner.find(".articleDetailUnits").html(args.existencias + " en existencia. "+detalle_movimientos_link)
//       // $articleDetailState.find(".articleDetailState").html()
//       // $unidadesContiner.html()
//       var $selected_article = $articulo

//       if (tipo_seguimiento=='S') {
//         $selected_article = $articulo_serie
//       }

//       $("#id_detalle_movimientos").on("click", function(){ showDetallesMovimientos($selected_article) } )
//       $detailcontiner.show()
//       var por_contar = "";
//       $unidadesContiner.show()
//     }
//   }

//   getExistenciaArticulo = function (args){
//     var data = args

//     $.ajax({
//       url:'/inventarios/get_existencia_articulo/', 
//       type : 'get', 
//       data: data, 
//       success: function(data){
//         showControlsToAddExistence(data)
//       },
//       error: function() {
//         alert('fallo algo');
//       },
//     });
//   }

//   onArticleChange = function($article){
//     if (es_small)
//     {
//       $("body").scrollTop(100);
//     }

//     if( $article.val() == null )
//       clearForm()
//     //Si se seleciono un cliente
//     else{
//       $unidadesContiner.show()
//       $articulo_clave.hide()
//       var serie = $serie.val()
      
//       getExistenciaArticulo({
//         'almacen': almacen, 
//         'articulo_id': $article.val()[0],
//         'serie': serie,
//       })
//     }
//   }

//   $articulo.on( 'change', function(){
//     onArticleChange($articulo);
//   });

//   $articulo_serie.on( 'change', function(){
//     onArticleChange($articulo_serie);
//   });

//   $submitBtn.on('click', function(){
//     onSubmit()
//   })

//   $manejarseries.on('click', function(){
//   })

// }

// var manager = new InventarioManager({
//   $articulo: $("#id_articulo"),
//   $unidadesContiner: $("#unidades_div"),
//   $unidades: $("#id_unidades"),
//   $serie: $("#serieArticuloId"),
//   $articulo_serie: $("#id_articulo_serie"),
//   almacen: $("#almacen_nombre").val(),
//   $articulo_clave: $("#id_clave_articulo"),
//   $detailcontiner: $("#articleDetailId"),
//   $manejarseries: $("#manejarSeries"),
//   $almacen: $("#almacen_id"),
//   $ubicacion: $("#ubicacion"),
//   $tipo_seguimiento: $("#articuloSeguimientoUnidadesId"),
//   $submitBtn: $("#enviar_btn"),
//   documentos:{
//     entrada_id:$("#hidden_entrada_id").val(),
//     salida_id:$("#hidden_salida_id").val(),
//   }
// })

