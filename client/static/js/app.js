//Application configuration constants
var config = {
    API_URL: "http://localhost:8080/api/",
    TEMPLATE_PATH: "/templates/"
};


//Gets template and json API data, compiles and loads template onto main page
function templateLoader(templateName, api) {
    //Show spinner while loading template"
    $("#app").html("<div id='spinner'><i class='fa fa-spinner fa-pulse fa-5x'></i></div>");

    //Retreiving template
    var template = "";
    $.get(config.TEMPLATE_PATH + templateName + ".hbs", function (data) {
        template = data;
    })
        .done(function () {
            //Check if API is required
            if (api) {
                //Retreiving context data from API
                var context = {};
                $.getJSON(config.API_URL + api, function (data) {
                    context = data;
                    console.log(data);
                })
                    .done(function () {
                        //compiling and displaying template
                        compiledTemplate = Handlebars.compile(template);
                        $("#app").html(compiledTemplate(context));
                    })
                    .fail(function () {
                        $("#error").html("There was an error getting data from API endpoint: " + api);
                    });
            } else {
                //compiling and displaying template
                compiledTemplate = Handlebars.compile(template);
                $("#app").html(compiledTemplate);
            }
        })
        .fail(function () {
            $("#error").html("There was an error loading template: " + templateName);
        });
}

//Router - Routes to pages
var router = $.sammy("#app", function () {
    this.get("#/", templateLoader("EmployeeList", "employees"));
    this.get("#/employee/:id", function () { templateLoader("EmployeeView", "employees/" + this.params.id); });
});

//Starts the router on page load
$(function () {
    router.raise_errors = true;
    router.run("#/");
});
