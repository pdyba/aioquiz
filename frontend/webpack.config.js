const path = require('path');
const webpack = require('webpack');
const HardSourceWebpackPlugin = require('hard-source-webpack-plugin');
const NODE_ENV = process.env.NODE_ENV;
const buildingForLocal = () => {
    return (NODE_ENV === 'development');
};
let w_plugins = [
    new webpack.DefinePlugin({
        'process.env': {
            isStaging: (NODE_ENV === 'development' || NODE_ENV === 'staging'),
            NODE_ENV: '"' + NODE_ENV + '"'
        }
    }),
];
if (buildingForLocal()) {
    w_plugins.push(new HardSourceWebpackPlugin());
}
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
    mode: buildingForLocal() ? 'development' : 'production',
    devServer: {
        historyApiFallback: true,
        noInfo: false
    },
    plugins: w_plugins,
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                    loaders: {
                        js: 'babel-loader',
                        i18n: '@kazupon/vue-i18n-loader'
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
            },
            {
                test: /\.txt$/,
                use: 'raw-loader'
            }
        ]
    },
};
module.exports = config;