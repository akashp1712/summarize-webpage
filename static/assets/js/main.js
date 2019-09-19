$(document).ready(function() {

  $("#btnSubmit").click(function() {

    var mediumURL = $("#inputUrl").val();

    if (0 === mediumURL.length) {
        // Default link for testingó
        mediumURL = "https://medium.com/the-mission/the-5-minute-routine-that-will-10x-your-productivity-1d148c360ea8";
    }

    $.ajax({
        url: baseUrl + "?url=" + mediumURL
    }).then(function(data) {
       processSummary(mediumURL, data.summary);
    });

    function processSummary(urlToPost, summaryData) {

        $('#summary').empty();

        if (summaryData.isArray) {

            var summary = document.createElement('h5');
            summary.innerHTML = "<b>Summary</b>:<br />";
            $('#summary').append(summary);

            var uList = document.createElement('ul');

            for (var index in summaryData) {
                var listElement = document.createElement('li');
                listElement.innerHTML = summaryData[index];
                uList.appendChild(listElement);
            }

            $('#summary').append(uList);

        } else {
            var summary = document.createElement('p');
            summary.innerHTML = "<b>Summary</b>: " + summaryData;
             $('#summary').append(summary);
        }

        $('#summary').hide().fadeIn(1000);
    }

  })});
