$(document).ready(function(){

    $('#crmSendButton').click(
        function(){

            $( ".crmResultContainer" ).fadeOut( "fast", function() {});
            $( ".crmError" ).fadeOut( "fast", function() {});

            var lpPesoPrevio = parseInt($('#crmPesoPrevio').val());
            var lpPesoActual = parseInt($('#crmPesoActual').val());
            var lpSemana = parseInt($('#crmSemana').val());

            if(isNaN(lpPesoPrevio) || lpPesoPrevio < 35 || lpPesoPrevio > 200 || isNaN(lpPesoActual) || lpPesoActual < 35 || lpPesoActual > 200){

                $( ".crmError" ).fadeIn( "slow", function() {});

            }else{

                var lpPesoGanado = (lpPesoActual - lpPesoPrevio);
                var lpPesoAdecuado = calculaRango(lpPesoPrevio, lpSemana);

                var lpSec = 0;

                function pesoCounter(){

                    if(lpSec<=lpPesoActual){
                        $('#crmMiPeso').text(lpSec);
                    }

                    ++lpSec;
                };

                function setDeceleratingTimeout(factor, times){
                  var internalCallback = function( t, counter )
                  {
                    return function()
                    {
                      if ( --t > 0 )
                      {
                        window.setTimeout( internalCallback, ++counter * factor );
                        pesoCounter();
                      }else{
                         $( ".crmResultContainer" ).fadeIn( "slow", function() {});
                      }
                    }
                  }( times, 0 );

                  window.setTimeout( internalCallback, factor );
                };

                setDeceleratingTimeout(1, (lpPesoActual+2) );

                $('#crmPesoGanado').text(lpPesoGanado);
                $('#crmWeek').text(lpSemana);
                $('#crmPesoAdecuado').text(lpPesoAdecuado);

            }
        }
    );

});

function calculaRango(peso, semana){

    switch (true) {
        case (semana < 8):
            var lpPesoAnt = peso;
            var lpPesoPos = peso;
            break;
        case (semana > 7 && semana < 11):
            var lpPesoAnt = peso;
            var lpPesoPos = peso + 1;
            break;
        case (semana > 10 && semana < 14):
            var lpPesoAnt = peso + 1;
            var lpPesoPos = peso + 2;
            break;
        case (semana > 13 && semana < 16):
            var lpPesoAnt = peso + 2;
            var lpPesoPos = peso + 3;
            break;
        case (semana > 15 && semana < 18):
            var lpPesoAnt = peso + 3;
            var lpPesoPos = peso + 4;
            break;
        case (semana > 17 && semana < 19):
            var lpPesoAnt = peso + 4;
            var lpPesoPos = peso + 5;
            break;
        case (semana == 19):
            var lpPesoAnt = peso + 4;
            var lpPesoPos = peso + 6;
            break;
        case (semana > 19 && semana < 22):
            var lpPesoAnt = peso + 5;
            var lpPesoPos = peso + 7;
            break;
        case (semana == 22):
            var lpPesoAnt = peso + 6;
            var lpPesoPos = peso + 8;
            break;
        case (semana == 23):
            var lpPesoAnt = peso + 6;
            var lpPesoPos = peso + 9;
            break;
        case (semana == 24):
            var lpPesoAnt = peso + 7;
            var lpPesoPos = peso + 9;
            break;
        case (semana == 25):
            var lpPesoAnt = peso + 7;
            var lpPesoPos = peso + 10;
            break;
        case (semana == 26):
            var lpPesoAnt = peso + 8;
            var lpPesoPos = peso + 10;
            break;
        case (semana == 27):
            var lpPesoAnt = peso + 8;
            var lpPesoPos = peso + 11;
            break;
        case (semana == 28):
            var lpPesoAnt = peso + 9;
            var lpPesoPos = peso + 11;
            break;
        case (semana > 28 && semana < 31):
            var lpPesoAnt = peso + 9;
            var lpPesoPos = peso + 12;
            break;
        case (semana == 31):
            var lpPesoAnt = peso + 9;
            var lpPesoPos = peso + 13;
            break;
        case (semana == 32):
            var lpPesoAnt = peso + 10;
            var lpPesoPos = peso + 13;
            break;
        case (semana > 32 && semana < 35):
            var lpPesoAnt = peso + 10;
            var lpPesoPos = peso + 14;
            break;
        case (semana > 34 && semana < 39):
            var lpPesoAnt = peso + 11;
            var lpPesoPos = peso + 14;
            break;
        case (semana > 38 && semana < 41):
            var lpPesoAnt = peso + 11;
            var lpPesoPos = peso + 15;
            break;
    }

    if(lpPesoAnt == lpPesoPos){
        var lpResult = 'es de '+lpPesoAnt;
    }else{
        var lpResult = 'está entre '+lpPesoAnt+' y '+lpPesoPos;
    }
    return lpResult;
}