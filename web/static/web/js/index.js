function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId());
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    var id_token = googleUser.getAuthResponse().id_token;
    console.log('ID Token: ' + id_token);
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
}

function onError(error) {
    console.log(error);
}