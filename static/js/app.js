window.addEventListener("load", function () {
    const loader = document.querySelector(".loader");
    loader.className += " hidden";
});
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
                    $successful.css({ "display": "flex" })
                    $successful.toggle(1000, () => {
                        $successful.css({ "display": "flex", "transition": "0.5" })
                    })
                    $("#image-close").on('click', function (event) {
                        $(this).parent().css('display', "none")
                    })
                }
            },
        });
    });
    $("#toogle-nav").on('click', function () {
        if ($("#Top-Nav-Link").hasClass("top-link-url")) {
            $(".top-link-url").toggleClass("active", function () {
                $(".main-crypto").css({ "padding": "em 0em 1em" })
            });
        }
    })

    const openModalButtons = document.querySelectorAll('[data-modal-target]')
    const closeModalButtons = document.querySelectorAll('[data-close-button]')
    const overlay = document.getElementById('overlay')

    openModalButtons.forEach(button => {
        button.addEventListener('click', () => {
            const modal = document.querySelector(button.dataset.modalTarget)
            openModal(modal)
        })
    })

    overlay.addEventListener('click', () => {
        const modals = document.querySelectorAll('.modal.active')
        modals.forEach(modal => {
            closeModal(modal)
        })
    })

    closeModalButtons.forEach(button => {
        button.addEventListener('click', () => {
            const modal = button.closest('.modal')
            closeModal(modal)
        })
    })

    function openModal(modal) {
        if (modal == null) return
        modal.classList.add('active')
        overlay.classList.add('active')
    }

    function closeModal(modal) {
        if (modal == null) return
        modal.classList.remove('active')
        overlay.classList.remove('active')
    }

    $(".key-style-title-img").on("click", 'img', function () {
        openModal(modal)
    })

    $("#lnh").on("click", function () {
        openModal(modal)
    })
    $(".buy-defi-title").on("click", function (event) {
        event.preventDefault()
        openModal(modal)
    })

    var liTag = $(".top-links li")
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
                scrollTop: $("#key-style").offset().top, scroll: "smooth"
            }, 500)
        }
        else if ($(this).attr("id") == "road-map-link") {
            $("html,body").animate({
                scrollTop: $("#road-map").offset().top - -90, scroll: "smooth"
            }, 600)
        }
        else if ($(this).attr("id") == "contact-map") {
            $("html,body").animate({
                scrollTop: $("#contact").offset().top - -30
                , scroll: "smooth"
            }, 800)
        }
        var target = event.target
        if (prevDiv) {
            prevDiv.style.color = "";

        }
        target.style.color = "#00A86B";
        prevDiv = target;

    }
})


