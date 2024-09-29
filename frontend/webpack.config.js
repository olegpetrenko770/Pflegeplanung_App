import { resolve, join } from 'path';

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