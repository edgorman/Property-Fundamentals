import React from 'react';
import Map, {NavigationControl, GeolocateControl, Source, Layer} from 'react-map-gl';
import bbox from '@turf/bbox';

import LogoControl from './LogoControl';

import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';


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
      ],
      mapStyle: "mapbox://styles/mapbox/streets-v9",
      mapboxAccessToken: process.env.REACT_APP_MAPBOX_TOKEN
    }

    this.handleResetViewState = this.handleResetViewState.bind(this);
    this.handleClick = this.handleClick.bind(this);
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

  handleClick(e) {
    let feature = e.features[0];

    if (feature){
      let [minLng, minLat, maxLng, maxLat] = bbox(e.features[0]);

      this.map.fitBounds(
        [
          [minLng, minLat],
          [maxLng, maxLat]
        ],
        {padding: 40, duration: 1000}
      );
    }
  }

  render() {
    let layerStyle = {
      id: 'point',
      type: 'fill',
      paint: {
        'fill-color': '#222222',
        'fill-opacity': 0.2,
        'fill-outline-color': '#000000'
      }
    };

    return (
      <Map
        initialViewState={this.state.initialViewState}
        minZoom={this.state.minZoom}
        mapStyle={this.state.mapStyle}
        mapboxAccessToken={this.state.mapboxAccessToken}
        ref={(e) => { this.map = e; }}
        onClick={this.handleClick}
        interactiveLayerIds={['point']}
      >
        <LogoControl position="top-left" onClick={this.handleResetViewState} />
        <NavigationControl position="top-left" visualizePitch={true} />
        <GeolocateControl position="top-left" />

        <Source type="geojson" data={"https://raw.githubusercontent.com/martinjc/UK-GeoJSON/master/json/administrative/eng/lad.json"}>
          <Layer {...layerStyle} />
        </Source>
      </Map>
    );
  }
}
