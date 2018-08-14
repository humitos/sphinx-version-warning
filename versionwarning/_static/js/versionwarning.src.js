const semver = require('semver');

function injectVersionWarningBanner(running_version, version, config) {
    var version_url = window.location.pathname.replace(running_version.slug, version.slug);
    var warning = $(config.banner.html);

    warning
      .find("a")
      .attr("href", version_url)
      .text(version.slug);

    var body = $(config.banner.body_default_selector);
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


function checkVersion(config) {
    var running_version = config.version;
    console.debug("Running version: " + running_version.slug);

    var get_data = {
        project__slug: config.project.slug,
        // active is not yet deployed
        // active: "true",
        // format: "jsonp",
    };

    $.ajax({
        url: config.meta.api_url + "version/",
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
                injectVersionWarningBanner(running_version, highest_version, config);
            }
        },
        error: function () {
            console.error("Error loading Read the Docs active versions.");
        }
    });
}

function init() {
    $.ajax({
        url: "_static/data/versionwarning-data.json",
        success: function(config) {
            // Check if there is already a banner added statically
            var banner = document.getElementById(config.banner.id_div);
            if (banner) {
                console.debug("There is already a banner added. No checking versions.")
            }
            else {
                checkVersion(config);
            }
        },
        error: function() {
            console.error("Error loading versionwarning-data.json");
        },
    })
}


$(document).ready(function () {
    init();
});
