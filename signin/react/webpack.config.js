path = require('path');

module.exports = {
  entry: './src/js/index.js',
  
  output: {
    filename: 'bundle.js',
    path: path.resolve('../static/signin/')
  },

  module: {
      rules: [
          {
              test: /\.js$/,
              exclude: /node_modules/,
              loader: 'babel-loader' 
          }
      ]
  }  
};