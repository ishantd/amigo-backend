function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId());
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    var id_token = googleUser.getAuthResponse().id_token;
    console.log(googleUser.getAuthResponse());
    console.log('ID Token: ' + id_token);
    console.log('Email: ' + profile.getEmail());

    var access_token = gapi.auth2.getAuthInstance().currentUser.Nb.wc.access_token;
    //make post request to login user

    var post_data = { "access_token": access_token };

    $.ajax({
        type: "POST",
        headers: { "Content-Type": "application/json" },
        url: "/accounts/dj-rest-auth/google/",
        data: JSON.stringify(post_data),
        success: function(res) {
            console.log(res);
            // window.location.replace("/");
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

function onError(error) {
    console.log(error);
}