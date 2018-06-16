$(document).ready(function(){
     //alert("doc ready .. ");

    $("#level1").change(function(){
        alert("Changed Level 1 value to:" + $("#level1").val());
     });

    $("#level2").change(function(){
        //alert("Changed Level 2 value to:" + $("#level2").val());
     });

    $(".sales").change(function(){
        var level1 = $("#level1").val();
        var level2 = $("#level2").val();
        var level3 = $("#level3").val();
        var level4 = $("#level4").val();
        var level5 = $("#level5").val();
        //var hirearchy = level1 + "/" + level2 + "/" + level3 + "/" + level4 + "/" + level5

        var hirearchy = level1;

        //alert("Class SALES changed to:" + hierarchy);

        $.ajax({
                type: "POST",
                url: "/get_levels",
                contentType: "text/json; charset=utf-8",
                data: JSON.stringify({ level1:'APJ'}),
                success: function(data) {
                    var newoptions = "";
                    for (var level of data.levels) {
                        newoptions += '<option value="' + level+ '">' + level + '</option>';
                    }

                    // Load up options and turn element on
                    $("#level2").html(newoptions);
                    $("#level2").prop('disabled', false);

                }
            });
     });
});