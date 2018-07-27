var API_URL = "https://readthedocs.org/api/v2/"
// var API_URL = "http://localhost:8000/api/v2/"


function injectVersionWarningBanner(running_version, version) {
    var version_url = window.location.pathname.replace(running_version.slug, version.slug);

    // TODO: make this warning alert configurable from conf.py
    var warning = $(
        '<div class="admonition warning"> ' +
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

// TODO: use something like https://www.npmjs.com/package/semver-parser
// https://maymay.net/blog/2008/06/15/ridiculously-simple-javascript-version-string-to-object-parser/
function parseVersionString (str) {
    if (typeof(str) != "string") { return false; }
    var x = str.split(".");
    // parse from string or default to 0 if can't parse
    var maj = parseInt(x[0]) || 0;
    var min = parseInt(x[1]) || 0;
    var pat = parseInt(x[2]) || 0;
    return {
        major: maj,
        minor: min,
        patch: pat
    }
}

function getHighestVersion(versions) {
    var highest_version;

    $.each(versions, function (i, version) {
        if (version.slug == "latest") {
            return version;
        }
        else if (version.slug.indexOf(".") == -1) {
            // Skip it since it's not a semver
        }
        else if (!highest_version) {
            highest_version = version;
        }
        else if (isHighestVersion(version, highest_version)) {
            highest_version = version;
        }
    });
    return highest_version;
}

function isHighestVersion(highest, version) {
    // Return TRUE if highest >= version, otherwise return FALSE

    // FIXME: fix this logic. It doesn't work! Also, it doesn't
    // support versions with "v" like "v3.4.1" and does not skip named
    // versions ("master", "release-x", "fix-docs", etc)
    highest = parseVersionString(highest.slug);
    version = parseVersionString(version.slug);
    if (version.major < highest.major) {
        return false;
    } else if (version.minor < highest.minor || version.patch < highest.patch) {
        return false;
    } else {
        return true;
    }
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
            highest_version = getHighestVersion(versions["results"]);
            if (!isHighestVersion(running_version, highest_version)) {
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

init();
