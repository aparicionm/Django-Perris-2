$(document).on('ready',function (){
 		
    $.getJSON('js/comunas-regiones', function(data) {
        $.each(data, function(key, value) {
            $("#region").append('<option name="' + key + '">' + value + '</option>');
        });
    });
});

$(function() {
      $("#perris-formulario").validate({
        rules: {
          correo: {
            required: true,
            correo: true
          }
        },
        messages: {
          correo: {
            required: 'Ingresa tu correo electrónico',
            correo: 'Formato de correo no válido'
          }
        }
      });
    });