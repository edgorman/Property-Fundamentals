// import React from 'react';
// import ReactMapGL, {FullscreenControl} from 'react-map-gl';
// import './app.css';


// class App extends React.Component {
//     constructor(props) {
//         super(props);
//     }

//     render() {
//         let viewport = {
//             width: "100vw",
//             height: "100vh",
//             latitude: 38.95863,
//             longitude: -77.357002,
//             zoom: 5
//         }
        
//         return (
//             <ReactMapGL
//                 {...viewport}
//                 mapStyle="mapbox://styles/mapbox/streets-v9"
//                 mapboxApiAccessToken="">
//                     <FullscreenControl/>
//             </ReactMapGL>
//         )
//     }
// }

// export default App;

// import * as React from 'react';
// import ReactMapGL, {Marker} from 'react-map-gl';

// function App() {
//   const [viewState, setViewState] = React.useState({
//     latitude: 37.8,
//     longitude: -122.4,
//     zoom: 14
//   });

//   return (
//     <ReactMapGL
//       {...viewState}
//       onMove={evt => setViewState(evt.viewState)}
//       style={{width: 800, height: 600}}
//       mapStyle="mapbox://styles/mapbox/streets-v9"
//       mapboxAccessToken="">
//       <Marker longitude={-122.4} latitude={37.8} color="red" />
//     </ReactMapGL>
//   );
// }

// export default App;

import * as React from "react";
import { useState } from "react";
import ReactMapGL from "react-map-gl";

export default function App() {
  const [viewport, setViewport] = useState({
    width: 400,
    height: 400,
    latitude: 38.95863,
    longitude: -77.357002,
    zoom: 10
  });

  return (
    <div>
      <ReactMapGL
        {...viewport}
        onMove={evt => setViewport(evt.viewState)}
        mapboxApiAccessToken=""
      />
    </div>
  );
}
