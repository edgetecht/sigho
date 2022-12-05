$(document).ready(function() {
    $('#example').DataTable( {
        "language": {
            buttons: {
                copyTitle: 'Copiar datos',
            },
            "url": "//cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json"
        },
        dom: 'Bfrtip',
        buttons: [
            'copyHtml5',
            'excelHtml5',
            'csvHtml5',
            'pdfHtml5'
        ]
    } );
} );