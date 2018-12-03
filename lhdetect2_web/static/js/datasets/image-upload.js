$(function () {
    $(".modal-content").on('click', 'button[id=uploadImages]', function() {

        $("#fileUpload").fileupload({
            dataType: 'json',
            done: function (e, data) {
                if (data.result.is_valid) {
                    $("#uploadingFiles tbody").prepend(
                        "<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>"
                    )
                }
            }
        }).click();
    });
});