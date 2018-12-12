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

    $("#modal-dataset").on("submit", ".js-dataset-create-form", function(event) {
        let images_ids = [];

        $("#modal-dataset tr a").each(function() {
            images_ids.push($(this).attr('id').slice(3))
        });

        console.log(images_ids.toString());

        let image_input = $("<input>")
            .attr("type", "hidden")
            .attr("name", "images").val(images_ids.toString());

        $(this).append(image_input);

        let form = $(this);

        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#dataset-table tbody").html(data.html_dataset_list);
                    $("#dataset-counter").html(data.html_dataset_counter);
                    $("#modal-dataset").modal("hide");
                }
                else {
                    $("#modal-dataset .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });
});