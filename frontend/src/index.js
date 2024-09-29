import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
import { resolve, join } from 'path';
import './index.css';

export const entry = './src/index.js';
export const output = {
    filename: 'bundle.js', // Der Name der gebündelten Datei
    path: resolve(__dirname, 'dist'), // Der Ausgabepfad
};
export const module = {
    rules: [
        {
            test: /\.js$/, // Regel für JavaScript-Dateien
            exclude: /node_modules/,
            use: {
                loader: 'babel-loader', // Verwende Babel zum Transpilieren von ES6+ Code
            },
        },
        {
            test: /\.css$/, // Regel für CSS-Dateien
            use: ['style-loader', 'css-loader'], // Verwende Style- und CSS-Loader
        },
    ],
};
export const devServer = {
    contentBase: join(__dirname, 'dist'), // Der Pfad für den Entwicklungsserver
    compress: true,
    port: 9000, // Der Port für den Entwicklungsserver
};
