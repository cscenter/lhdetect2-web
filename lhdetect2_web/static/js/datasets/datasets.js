$(function () {

    $(".js-create-dataset").click(function(event) {
        event.preventDefault();
        $.ajax({
            /*TODO remove url hardcode*/
            url: '/datasets/create/',
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-dataset").modal("show");
            },
            success: function (data) {
                $("#modal-dataset .modal-content").html(data.html_form);
            },
            error: function (data) {
                console.log(data)
            }
        });
    });

});