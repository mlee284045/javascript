$.ajax({
    url: '/all_pokemon',
    type: "GET",
    success: function(data) {
        console.log(data);
    }
})