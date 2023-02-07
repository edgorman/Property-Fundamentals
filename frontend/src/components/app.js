import React from 'react';
import Map, {NavigationControl, GeolocateControl, AttributionControl} from 'react-map-gl';
import './app.css';

export default class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      initialViewState: {
        latitude: 54.8,
        longitude: -2,
        zoom: 4
      },
      minZoom: 5,
      maxBounds: [
        [-21, 49],
        [19, 59.7]
      ]
    }

    this.handleResetViewState = this.handleResetViewState.bind(this);
  }

  handleResetViewState() {
    this.map.flyTo({
      center: [
        this.state.initialViewState.longitude,
        this.state.initialViewState.latitude
      ],
      zoom: this.state.initialViewState.zoom,
      essential: true,
      duration: 1500
    });
  }

  render() {
    return (
      <Map
        initialViewState={this.state.initialViewState}
        minZoom={this.state.minZoom}
        mapStyle="mapbox://styles/mapbox/streets-v9"
        mapboxAccessToken={process.env.REACT_APP_MAPBOX_TOKEN}
        ref={(e) => { this.map = e; }}
      >
        <button className="mapbox-logo" onClick={this.handleResetViewState}>
          <AttributionControl position="top-left"/>
        </button>
        <NavigationControl position="top-left" visualizePitch={true} />
        <GeolocateControl position="top-left" />
      </Map>
    );
  }
}
