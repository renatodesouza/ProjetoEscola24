//Esta funcao captura informacoes do destinatario escolhido
// e preenche parte do formulario de mensagem com nome do destinatario
// e o id do destinatario 

$(document).ready(function(){
    $('.destinatario-item').click(function(e){
        e.preventDefault();
        var destinatarioValue = $(this).data('value');
        var destinatarioNome = $(this).text();


        console.log(destinatarioValue);
        console.log(destinatarioNome);

        $('#destinatario-input').val(destinatarioValue);
        $('#destinatario-nome').text(destinatarioNome);
    });
});


