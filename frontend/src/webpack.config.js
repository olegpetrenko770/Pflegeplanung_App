const { resolve, join } = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
	filename: 'bundle.js',
	path: resolve(__dirname, 'dist'),
  },
  module: {
	rules: [
	  {
		test: /\.js$/,
		exclude: /node_modules/,
		use: {
		  loader: 'babel-loader',
		},
	  },
	  {
		test: /\.css$/,
		use: ['style-loader', 'css-loader'],
	  },
	],
  },
  devServer: {
	contentBase: join(__dirname, 'dist'),
	compress: true,
	port: 9000,
  },
};