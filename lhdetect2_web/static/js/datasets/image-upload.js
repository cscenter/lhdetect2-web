$(function () {
    $(".modal-content").on('click', 'button[id=uploadImages]', function() {

        $("#fileUpload").fileupload({
            dataType: 'json',
            done: function (e, data) {
                if (data.result.is_valid) {
                    $("#uploadingFiles tbody").prepend(
                        "<tr><td><a href='" + data.result.url + "' id='img" + data.result.id + "'>" + data.result.name +
                        "</a><div class=\"progress\"><div class=\"progress-bar\" role=\"progressbar\" style=\"width: 0%;\">0%</div></div></td></tr>"
                    )
                }
            },
            progress: function (e, data) {
              let progress = parseInt(data.loaded / data.total * 100, 10);
              let strProgress = progress + "%";
              /* TODO handle progress by image id */
              $(".progress-bar").css({"width": strProgress}).text(strProgress);
            }
        }).click();
    });
});