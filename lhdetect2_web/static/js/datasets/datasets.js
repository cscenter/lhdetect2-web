$(function () {

    let loadForm = function(self) {
        let btn = $(self);
        $.ajax({
            url: btn.attr("data-url"),
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
    };

    let saveForm = function (self) {
        let form = $(self);
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
    };

    $(".js-create-dataset").click(function(event) {
        event.preventDefault();
        loadForm(this);
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

        saveForm(this);
        return false;
    });

    $("#dataset-table").on("click", ".js-delete-dataset", function(event) {
        event.preventDefault();
        loadForm(this);
    });

    $("#modal-dataset").on("submit", ".js-dataset-delete-form", function(event) {
        // TODO: add dataset images deletion
        saveForm(this);
        return false;
    });
});