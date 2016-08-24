'use strict';

const path = require('path');

const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');


const babelConfig = {
  presets: ['es2015', 'react'],
  plugins: [
    'syntax-async-functions',
    'transform-async-to-generator',
    'transform-class-properties',
    'transform-object-rest-spread',
  ],
};

const config = {
  bail: true,
  cache: true,
  devtool: 'source-map',

  entry: [
    'normalize.css',
    path.join(__dirname, 'client', 'js', 'index.jsx'),
    path.join(__dirname, 'client', 'index.html'),
  ],

  output: {
    path: path.join(__dirname, 'whodunnit', 'htdocs'),
    publicPath: 'static/',
    filename: path.join('static', 'js', 'whodunnit.min.js'),
    chunkFilename: '[chunkHash].js',
    sourceMapFilenName: '[name].map',
  },

  module: {
    loaders: [
      {
        test: /\.css$/,
        loader: ExtractTextPlugin.extract('style-loader', '!css-loader?sourceMap&importLoaders=1!postcss-loader?'),
      },
      {
        test: /\.html$/,
        loader: 'file-loader',
        query: {
          name: '[name].[ext]',
        },
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: Object.assign({}, babelConfig, {
          cacheDirectory: true,
        }),
      },
      {
        test: /\.jsx$/,
        loader: 'babel-loader',
        query: Object.assign({}, babelConfig, {
          cacheDirectory: true,
          presets: [...babelConfig.presets, 'react'],
        }),
      },
    ],
  },

  plugins: [
    new webpack.DefinePlugin({
      'process.env': {
        'NODE_ENV': JSON.stringify(process.env.NODE_ENV),
      },
    }),
    new ExtractTextPlugin(path.join('static', 'css', 'style.min.css')),
  ],

  postcss(webpack) {
    return {
      defaults: [
        require('stylelint'),
        require('postcss-import')({
          addDependencyTo: webpack,
        }),
        require('postcss-simple-vars'),
        require('postcss-color-function'),
        require('postcss-nested'),
        require('colorguard'),
        require('autoprefixer')({browsers: 'last 2 versions'}),
        require('cssnano'),
        require('postcss-reporter')({clearMessages: true})
      ],
    };
  },

  resolve: {
    extensions: ['', '.js', '.jsx'],
  },
};

if (process.env.NODE_ENV === 'production')
  config.plugins.push(
    new webpack.optimize.DedupePlugin(),
    new webpack.optimize.UglifyJsPlugin({
      compress: {warnings: false},
    })
  );


module.exports = config;
