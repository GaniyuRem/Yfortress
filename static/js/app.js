$(document).ready(function () {
    $successful = $("#success-box")
    input_field = $(" #form-container").find("input,textarea")
    $(this).parent().css('display', "hide")
    $("#form-container").on('submit', (e) => {
        let value_pro = []
        e.preventDefault();
        $.each(input_field, (index, value) => {
            value_pro.push($(value).val())
        });
        $.ajax({

            type: "POST",
            data: { csrfmiddlewaretoken: value_pro[0], name: value_pro[1], email: value_pro[2], message_box: value_pro[3] },
            success: (data, responseText, request) => {
                if (request.status == 200) {
                    console.log(request.status, data)
                }
            },
            error: () => {
                console.log("error")
            }
        });
        $successful.css({ "display": "flex" })
        $successful.toggle(1000, () => {
            $successful.css({ "display": "flex", "transition": "0.5" })
        })
        $("#image-close").on('click', function (event) {
            $(this).parent().css('display', "none")
        })
    });


    var liTag = $(".top-links li")
    console.log(liTag.length)
    for (var i = 0; i < liTag.length; i++) {
        if (liTag[i].tagName == "LI" || liTag[i].tagName == "li") {
            if (liTag[i].addEventListener) {
                liTag[i].addEventListener('click', callback, false);
            }
            else if (liTag[i].attachEvent) {
                liTag[i].attachEvent('on' + 'click', callback);
            }
        }
    }
    var prevDiv = null;
    function callback(event) {
        if ($(this).attr("id") == "vision") {
            $("html,body").animate({
                scrollTop: $("#main-case").offset().top - 160, scroll: "smooth"
            }, 200)
        }
        else if ($(this).attr("id") == "road-about") {
            $("html,body").animate({
                scrollTop: $("#key-style").offset().top - 160, scroll: "smooth"
            }, 500)
        }
        else if ($(this).attr("id") == "road-map-link") {
            $("html,body").animate({
                scrollTop: $("#road-map").offset().top - 90, scroll: "smooth"
            }, 600)
        }
        else if ($(this).attr("id") == "contact-map") {
            $("html,body").animate({
                scrollTop: $("#contact").offset().top
                , scroll: "smooth"
            }, 800)
        }
        var target = event.target
        if (prevDiv) {
            prevDiv.style.color = "";
            console.log(prevDiv)

        }
        target.style.color = "#00A86B";
        prevDiv = target;
        console.log(prevDiv)
    }
    // if (window.screenY >= 20) {
    //     console.log(true)
    //     $("header").addClass("scrolling-active");
    // }
})

//     .on("load", function () {
//     if (window.screenY >= 20) {
//         console.log(true)
//         $("header").addClass("scrolling-active");
//     }
// })


