const semver = require('semver');

var API_URL = "https://readthedocs.org/api/v2/";
// var API_URL = "http://localhost:8000/api/v2/";


function injectVersionWarningBanner(running_version, version) {
    var version_url = window.location.pathname.replace(running_version.slug, version.slug);

    // TODO: make this warning alert configurable from conf.py
    var warning = $(
        '<div id="version-warning-banner" class="admonition warning"> ' +
        '<p class="first admonition-title">Warning</p> ' +
        '<p class="last"> ' +
        'You are not using the most up to date version of the library. ' +
        '<a href="#"></a> is the newest version.' +
        '</p>' +
        '</div>');

    warning
      .find("a")
      .attr("href", version_url)
      .text(version.slug);

    // TODO: make the way of finding the element configurable
    var body = $("div.body");
    if (!body.length) {
        body = $("div.document");
    }
    body.prepend(warning);
}


function getHighestVersion(versions) {
    var highest_version;

    $.each(versions, function (i, version) {
        if (!semver.valid(version.slug)) {
            // Skip versions that are not valid
        }
        else if (!highest_version) {
            highest_version = version;
        }
        else if (
            semver.valid(version.slug) && semver.valid(highest_version.slug) &&
                semver.gt(version.slug, highest_version.slug)) {
            highest_version = version;
        }
    });
    return highest_version;
}


function checkVersion(project_data) {
    var running_version = project_data.version;
    console.debug("Running version: " + running_version.slug);

    var get_data = {
        project__slug: project_data.project.slug,
        // active is not yet deployed
        // active: "true",
        // format: "jsonp",
    };

    $.ajax({
        url: API_URL + "version/",
        // Used when working locally for development
        // crossDomain: true,
        // xhrFields: {
        //     withCredentials: true,
        // },
        // dataType: "jsonp",
        data: get_data,
        success: function (versions) {
            // TODO: fetch more versions if there are more pages (next)
            highest_version = getHighestVersion(versions["results"]);
            if (
                semver.valid(running_version.slug) && semver.valid(highest_version.slug) &&
                    semver.lt(running_version.slug, highest_version.slug)) {
                console.debug("Highest version: " + highest_version.slug);
                injectVersionWarningBanner(running_version, highest_version);
            }
        },
        error: function () {
            console.error("Error loading Read the Docs active versions.");
        }
    });
}

function init() {
    // Check if there is already a banner added statically
    var banner = document.getElementById("version-warning-banner");
    if (!banner) {
        $.ajax({
            url: "_static/data/data.json",
            success: function(data) {
                checkVersion(data);
            },
            error: function() {
                console.error("Error loading data.json");
            },
        })
    }
}


$(document).ready(function () {
    init();
});
