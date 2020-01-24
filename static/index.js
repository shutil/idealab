$(document).ready(function () {
    var socket = io();

    socket.emit('gd', {
        name: "connect"
    });

    $('#frm').on('submit', function (e) {
        e.preventDefault();
        var fd = new FormData($('#frm')[0]);
        $.ajax({
            type: "POST",
            url: "/post_idea",
            data: fd,
            processData: false,
            contentType: false,
            success: function (response) {
                $('#frm')[0].reset();
                console.log("done");
                socket.emit('gd', {
                    name: "connect"
                });

                socket.on('gd', (data) => {
                    var ar = data;
                    console.log(ar['pl']);
                    var html = "";
                    for (let index = 0; index < ar['pl'].length; index++) {
                        const pl = ar['pl'][index];
                        const idea = ar['idea'][index];
                        const by = ar['by'][index]
            
                        html += `
                        <div class="card mt-4">
                            <div class="card-header">
                                <h5>${pl}</h5>
                            </div>
                            <div class="card-body">
                                <p class="card-text">${idea}</p>
                                <p>By: ${by}</p>
                            </div>
                        </div>
                        `
                        $("#ideas").html(html);
                    }
                });
            }
        });
    });

    socket.on('gd', (data) => {
        var ar = data;
        console.log(ar['pl']);
        var html = "";
        for (let index = 0; index < ar['pl'].length; index++) {
            const pl = ar['pl'][index];
            const idea = ar['idea'][index];
            const by = ar['by'][index]

            html += `
            <div class="card mt-4">
                <div class="card-header">
                    <h5>${pl}</h5>
                </div>
                <div class="card-body">
                    <p class="card-text">${idea}</p>
                    <p>By: ${by}</p>
                </div>
            </div>
            `
            $("#ideas").html(html);
        }
    }); 
});