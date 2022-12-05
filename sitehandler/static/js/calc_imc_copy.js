$(document).ready(function(){
    $('#crmSendButton').click(
        function(){
            $('#crmResultContainer').css('display', 'none');
            $('.crmError').css('display', 'none');

            var lpPeso = parseInt($('#crmPeso').val());

            var lpAltura = parseInt($('#crmAltura').val());

            if(isNaN(lpPeso) || lpPeso < 35 || lpPeso > 200 || isNaN(lpAltura) || lpAltura < 50 || lpAltura > 270){

                $( ".crmError" ).fadeIn( "slow", function() {});

            }else{
                var lpIMC = (lpPeso/(lpAltura * lpAltura))*10000;
                var lpIMCRound = Math.round(lpIMC * 100) / 100;
                var lpRango = crmRange(lpIMCRound);
                $('#crmIMC').text(lpIMCRound);
                $('#crmRango').text(lpRango);
            }
        }
    );
});

function crmRange(imc){



    switch (true) {

    case (imc <= 18.80):

        var rango = "peso deficiente";

        break;

    case (imc > 18.81 && imc <= 24.60):

        var rango = "peso adecuado";

        break;

    case (imc > 25.61 && imc <= 28.60):

        var rango = "sobrepeso";

        break;

    case (imc > 28.61 && imc <= 45):

        var rango = "obesidad";

        break;

    case (imc > 45):

        var rango = "obesidad mórbida";

        break;

    }



    return rango;



}
  