import React from 'react';
import ReactDOM from 'react-dom';

// // Workaround: these 4 lines are to fix issue https://github.com/mapbox/mapbox-gl-js/issues/10565
// // Install packages worker-loader & mapbox-gl
// import mapboxgl from "mapbox-gl";
// // eslint-disable-next-line import/no-webpack-loader-syntax
// (mapboxgl as any).workerClass = require('worker-loader!mapbox-gl/dist/mapbox-gl-csp-worker').default;


ReactDOM.render(
  <React.StrictMode>
    <p>Hello World!</p>
  </React.StrictMode>,
  document.getElementById('root')
);
