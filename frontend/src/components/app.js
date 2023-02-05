import React from 'react';
import Map, {NavigationControl, GeolocateControl, AttributionControl} from 'react-map-gl';
import './app.css';

export default class App extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Map
        initialViewState={{
          latitude: 54.8,
          longitude: -2,
          zoom: 4
        }}
        minZoom={4}
        maxBounds={[
          [-21, 49],
          [19, 59.7]
        ]}
        mapStyle="mapbox://styles/mapbox/streets-v9"
        mapboxAccessToken={process.env.REACT_APP_MAPBOX_TOKEN}
      >
        <AttributionControl position="top-left" /* logo */ />
        <NavigationControl position="top-left" />
        <GeolocateControl position="top-left" />
      </Map>
    );
  }
}
