const path = require('path');

module.exports = {
    mode: 'production',
    entry: './versionwarning/_static/js/versionwarning.src.js',
    output: {
        path: path.resolve(__dirname, 'versionwarning/_static/js/'),
        filename: 'versionwarning.js'
    }
};
