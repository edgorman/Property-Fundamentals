import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/app';

// // Workaround: these 4 lines are to fix issue https://github.com/mapbox/mapbox-gl-js/issues/10565
// // Install packages worker-loader & mapbox-gl
// import mapboxgl from "mapbox-gl";
// mapboxgl.workerClass = require('worker-loader!mapbox-gl/dist/mapbox-gl-csp-worker').default;


ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
