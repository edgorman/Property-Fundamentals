import React from 'react';
import Map from 'react-map-gl';
import './app.css';


export default class App extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Map
        initialViewState={{
          latitude: 54.7,
          longitude: -2.5,
          zoom: 5.2
        }}
        mapStyle="mapbox://styles/mapbox/streets-v9"
        mapboxAccessToken={process.env.REACT_APP_MAPBOX_TOKEN}
      >
      </Map>
    );
  }
}
