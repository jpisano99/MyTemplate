var sales_level1 = document.getElementById("level1");
var sales_level2 = document.getElementById("level2");

sales_level1.onchange = function()  {
    level1 = sales_level1.value;

    fetch('/level1/' + level1).then(function(response) {

        response.json().then(function(data) {

            var optionHTML = '';
            for (var level of data.levels) {
                optionHTML += '<option value="' + level+ '">' + level + '</option>';
            }
        sales_level2.innerHTML = optionHTML;
    })

    })
};