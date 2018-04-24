const path = require('path');
const webpack = require('webpack');
// const HtmlWebpackPlugin = require('html-webpack-plugin');
const NODE_ENV = process.env.NODE_ENV;
const buildingForLocal = () => {
    return (NODE_ENV === 'development');
};


// const extractHTML = new HtmlWebpackPlugin({
//     title: 'History Search',
//     filename: 'index.html',
//     inject: true,
//     environment: process.env.NODE_ENV,
//     isLocalBuild: buildingForLocal(),
//     imgPath: (!buildingForLocal()) ? 'assets' : 'src/assets'
// });
const config = {
    entry: {
      build: './src/main.js'
    },
    output: {
      path: path.resolve(__dirname, './dist'),
      publicPath: '/dist/',
      filename: 'build.js',
    },

    // optimization: {
    //     runtimeChunk: false,
    //     splitChunks: {
    //         chunks: "all"
    //     }
    // },
    // resolveLoader: {
    //     modules: [setPath('node_modules')]
    // },
    mode: 'production', // buildingForLocal() ? 'development' : 'production',
    devServer: {
        historyApiFallback: true,
        noInfo: false
    },
    plugins: [
        // extractHTML,
        new webpack.DefinePlugin({
            'process.env': {
                isStaging: (NODE_ENV === 'development' || NODE_ENV === 'staging'),
                NODE_ENV: '"' + NODE_ENV + '"'
            }
        })
    ],
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                    loaders: {
                        js: 'babel-loader'
                    }
                }
            },
            {
                test: /\.js$/,
                exclude: /(node_modules|bower_components)/,
                use: [{
                    loader: "babel-loader",
                    options: {presets: ['es2015']}
                }]
            },
            {
                test: /\.(png|jpg|gif|svg)$/,
                loader: 'file-loader',
                query: {
                    name: '[name].[ext]?[hash]',
                    useRelativePath: buildingForLocal()
                }
            },
            {
                test: /\.css$/,
                use: [
                    'style-loader',
                    'css-loader'
                ]
            },
            {
                test: /\.(woff|woff2|eot|ttf|otf)$/,
                loader: 'url-loader',
                options: {
                    limit: 10000,
                    name: 'fonts/[name].[hash:7].[ext]'
                }
            }
        ]
    },
};
module.exports = config;