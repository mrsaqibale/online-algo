$(document).ready(function() {
    $('#searchBar').on('input', function() {
        var searchText = $(this).val().toLowerCase(); // Get the value of the search bar and convert to lowercase
        $('#algorithmList li').each(function() {
            var algorithmName = $(this).text().toLowerCase(); // Get the text of each algorithm and convert to lowercase
            // If the algorithm name contains the search text, show it; otherwise, hide it
            if (algorithmName.includes(searchText)) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });
});
$(document).ready(function() {
    $('#input-value').on('input', function() {

        var target = 'a';
        var inputValue = $(this).val();
        if (target.includes(inputValue)) {
            alert("good bhai jany dy ")
        } else {
            alert("ruk ja na bhai ")
        }
    });
})