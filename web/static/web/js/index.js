function onSuccess(googleUser) {
    var profile = googleUser.getBasicProfile();
    var id_token = googleUser.getAuthResponse().id_token;

    var access_token = gapi.auth2.getAuthInstance().currentUser.Nb.wc.access_token;
    //make post request to login user

    var post_data = { "access_token": access_token };

    $.ajax({
        type: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie('csrftoken'),
        },
        url: "/api/accounts/dj-rest-auth/google/",
        data: JSON.stringify(post_data),
        success: function(res) {
            console.log(res);
            window.location.replace("/dashboard/");
        },
        error: function(xhr, status, error) {
            // var err = eval("(" + xhr.responseText + ")");
            // alert(err.Message);
            console.log(xhr, status, error);

            var error_status = (xhr.responseJSON.status);
            console.log(error_status);
            // adderror(error_status);
        },
        dataType: "json",
        contentType: "application/json",
    });

}

function onFailure(error) {
    console.log(error);
}

function renderButton() {
    gapi.signin2.render('my-signin2', {
        'scope': 'profile email https://www.googleapis.com/auth/spreadsheets',
        'width': 240,
        'height': 50,
        'longtitle': true,
        'theme': 'dark',
        'onsuccess': onSuccess,
        'onfailure': onFailure
    });
}


function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    var id_token = googleUser.getAuthResponse().id_token;

    var access_token = gapi.auth2.getAuthInstance().currentUser.Nb.wc.access_token;
    //make post request to login user

    var post_data = { "access_token": access_token };

    $.ajax({
        type: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie('csrftoken'),
        },
        url: "/api/accounts/dj-rest-auth/google/",
        data: JSON.stringify(post_data),
        success: function(res) {
            console.log(res);
            window.location.replace("/dashboard/");
        },
        error: function(xhr, status, error) {
            // var err = eval("(" + xhr.responseText + ")");
            // alert(err.Message);
            console.log(xhr, status, error);

            var error_status = (xhr.responseJSON.status);
            console.log(error_status);
            // adderror(error_status);
        },
        dataType: "json",
        contentType: "application/json",
    });

}