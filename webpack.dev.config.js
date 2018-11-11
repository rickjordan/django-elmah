var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    entry: './djelmah-client/index.js',
    output: {
        path: path.join(__dirname, '/djelmah-client/bundles'),
        filename: '[name]-[hash].js',
        publicPath: 'http://localhost:8080/djelmah-client/bundles/'
    },
    module: {
        rules: [{
            test: /\.(js|jsx)$/,
            exclude: /node_modules/,
            use: ['babel-loader']
        }]
    },
    resolve: {
        extensions: ['*', '.js', '.jsx']
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new BundleTracker({filename: './webpack-stats.json'})
    ],
    devServer: {
        headers: { "Access-Control-Allow-Origin": "*" },
        hot: true
    }
}
