const path = require("path")

module.exports = {
    entry: './djelmah-client/index.js',
    output: {
        path: path.join(__dirname, '/djelmah/static/djelmah/'),
        filename: 'script.min.js'
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: ['babel-loader']
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            }
        ]
    },
    resolve: {
        extensions: ['*', '.js', '.jsx']
    }
}
