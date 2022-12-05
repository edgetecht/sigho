$(document).ready(function(){
    $('#crmSendButton').click(
        function(){
            $('#crmResultContainer').css('display', 'none');
            $('.crmError').css('display', 'none');
            $('#crmDel').css('font-weight', 'normal');
            $('#crmNorm').css('font-weight', 'normal');
            $('#crmSobre').css('font-weight', 'normal');
            $('#crmObes').css('font-weight', 'normal');
            $('#crmObesM').css('font-weight', 'normal');

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
                var crmTimer;
                crmCounter = 0;
                imc = (300 * lpIMCRound)/50;
                initBar();
            }
        }
    );
});



function initBar(){



    if(crmCounter < imc){

        crmGrafika(crmCounter);

        crmCounter++;



        if(crmCounter < imc){

            crmTimer = setTimeout('initBar()', 5);

        }else{

            $( "#crmResultContainer" ).fadeIn( "slow", function() {});

        }

    }

};



function crmGrafika(nIMC){



    var c = document.getElementById("crmGrafikaCanvas");

    var ctx = c.getContext("2d");



    ctx.clearRect (0 , 0 , c.width, c.height);



    ctx.translate(0, c.height);

    ctx.scale(1, -1);



    if(nIMC <= 110.40){



        ctx.fillStyle = '#6b84bc';

        $('#crmDel').css('font-weight', 'bold');



    }else if(nIMC <= 149.40){



        ctx.fillStyle = '#55A415';

        $('#crmDel').css('font-weight', 'normal');

        $('#crmNorm').css('font-weight', 'bold');



    }else if(nIMC <= 179.40){



        ctx.fillStyle = '#e3c338';

        $('#crmNorm').css('font-weight', 'normal');

        $('#crmSobre').css('font-weight', 'bold');



    }else if(nIMC <= 270){



        ctx.fillStyle = '#df7c20';

        $('#crmSobre').css('font-weight', 'normal');

        $('#crmObes').css('font-weight', 'bold');



    }else if(nIMC <= 300){



        ctx.fillStyle = '#f14c35';

        $('#crmObes').css('font-weight', 'normal');

        $('#crmObesM').css('font-weight', 'bold');



    }



    ctx.fillRect(0, 0, c.width, nIMC);

    ctx.scale(-1, 1);



};



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
