var API_URL = 'https://readthedocs.org/api/v2/'
var API_URL = 'http://localhost:8000/api/v2/'


function injectVersionWarningBanner(version) {
    // TODO: make this warning alert configurable from conf.py
    var warning = $(
        '<div class="admonition warning"> ' +
        '<p class="first admonition-title">Note</p> ' +
        '<p class="last"> ' +
        'You are not using the most up to date version of the library. ' +
        '<a href="#"></a> is the newest version.' +
        '</p>' +
        '</div>');

    warning
      .find('a')
      .attr('href', version.url)  // Use the proper URL here
      .text(version.slug);

    var body = $("div.body");
    if (!body.length) {
        body = $("div.document");
    }
    body.prepend(warning);
}

// https://maymay.net/blog/2008/06/15/ridiculously-simple-javascript-version-string-to-object-parser/
function parseVersionString (str) {
    if (typeof(str) != 'string') { return false; }
    var x = str.split('.');
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

    // console.log(versions);
    $.each(versions, function (i, version) {
        if (!highest_version) {
            // console.log(version.slug);
            highest_version = version;
        }
        else if (isHighestVersion(version, highest_version)) {
            console.log('highest: ' + version.slug);
            console.log('old highest: ' + highest_version.slug);
            highest_version = version;
        }
    });
    return highest_version;
}

function isHighestVersion(highest, version) {
    // TODO: fix this logic. I doesn't work!

    // Return TRUE if highest >= version, otherwise return FALSE
    // console.log(version_a.slug);
    // console.log(version_b.slug);
    highest = parseVersionString(highest.slug);
    version = parseVersionString(version.slug);
    if (version.major < highest.major) {
        console.log('major');
        return false;
    } else if (version.minor < highest.minor || version.patch < highest.patch) {
        console.log('minor');
        return false;
    } else {
        return true;
    }
}

function init(project_slug) {
    // TODO: get this data properly
    var running_version = {
        slug: '1.2.3',
        url: 'https://readthedocs.org/',
    };

    var get_data = {
        project__slug: project_slug,
        active: 'true',
        format: 'jsonp',
    };

    $.ajax({
        url: API_URL + "version/",
        crossDomain: true,
        xhrFields: {
            withCredentials: true,
        },
        dataType: "jsonp",
        data: get_data,
        success: function (versions) {
            highest_version = getHighestVersion(versions['results']);
            if (!isHighestVersion(running_version, highest_version)) {
                injectVersionWarningBanner(highest_version);
            }
        },
        error: function () {
            console.error('Error loading Read the Docs active versions.');
        }
    });
}


init('sphinx-version-warning');
