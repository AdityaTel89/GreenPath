$(document).ready(function() {
    $("form[name=signup_form]").submit(function(e) {
        var $form = $(this);
        var data = $form.serialize();

        $.ajax({
            url: "/signup",
            type: "POST",
            data: data,
            success: function(resp) {
                sessionStorage.setItem('status', 'True');
                window.location.href = "/home";
            },
            error: function(resp) {
                console.log(resp);
                if (resp.responseJSON && resp.responseJSON.error) {
                    alert(resp.responseJSON.error);
                } else {
                    alert("An unexpected error occurred. Please try again.");
                }
            }
        });

        e.preventDefault();
    });

    $("form[name=login_form]").submit(function(e) {
        var $form = $(this);
        var data = $form.serialize();

        $.ajax({
            url: "/login",
            type: "POST",
            data: data,
            success: function(resp) {
                sessionStorage.setItem('status', 'True');
                window.location.href = "/home";
            },
            error: function(resp) {
                console.log(resp);
                if (resp.responseJSON && resp.responseJSON.error) {
                    alert(resp.responseJSON.error);
                } else {
                    alert("Invalid login credentials. Please try again.");
                }
            }
        });

        e.preventDefault();
    });
});
