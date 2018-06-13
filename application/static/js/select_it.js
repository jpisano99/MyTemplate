var state_select = document.getElementById("state");
var city_select = document.getElementById("city");

state_select.onchange = function()  {

    state = state_select.value;

    fetch('/city/' + state).then(function(response) {

        response.json().then(function(data) {

            var optionHTML = '';
            for (var city of data.cities) {
                optionHTML += '<option value="' + city+ '">' + city + '</option>';
                //optionHTML += '<option value="' + city.id + '">' + city.name + '</option>';
            }
        city_select.innerHTML = optionHTML;
    })

    })
};