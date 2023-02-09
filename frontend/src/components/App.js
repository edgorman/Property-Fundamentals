import React from 'react';
import Map, {NavigationControl, GeolocateControl, Source, Layer} from 'react-map-gl';
import bbox from '@turf/bbox';

import LogoControl from './LogoControl';
import Sidebar from './Sidebar';
import SidebarToggle from './SidebarToggle';

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
      mapboxAccessToken: process.env.REACT_APP_MAPBOX_TOKEN,
      minZoom: 5,
      maxBounds: [
        [-21, 49],
        [19, 59.7]
      ],
      mapStyle: "mapbox://styles/mapbox/streets-v9",
      sidebarActive: false
    }

    this.handleResetViewClick = this.handleResetViewClick.bind(this);
    this.handleSidebarToggle = this.handleSidebarToggle.bind(this);
    this.handleMapClick = this.handleMapClick.bind(this);
  }

  handleResetViewClick() {
    // let feature = this.map.querySourceFeatures('test');
    // then bbox(feature) to get min/max lng/lat
    
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

  handleSidebarToggle() {
    console.log("here");
    this.setState({sidebarActive: !this.state.sidebarActive});
  }

  handleMapClick(e) {
    let feature = e.features[0];

    if (feature){
      console.log(feature.properties);
      let [minLng, minLat, maxLng, maxLat] = bbox(feature);

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
      }
    };

    return (
      <Map
        initialViewState={this.state.initialViewState}
        mapboxAccessToken={this.state.mapboxAccessToken}
        minZoom={this.state.minZoom}
        mapStyle={this.state.mapStyle}
        interactiveLayerIds={['point']}
        onClick={this.handleMapClick}
        ref={(e) => { this.map = e; }}
      >
        { /* Map controls */}
        <LogoControl position="top-left" onClick={this.handleResetViewClick} />
        <NavigationControl position="top-left" visualizePitch={true} />
        <GeolocateControl position="top-left" />

        { /* Sidebar and toggle */}
        <Sidebar isActive={this.state.sidebarActive} handleToggle={this.handleSidebarToggle} />
        <SidebarToggle open={true} handleToggle={this.handleSidebarToggle} />

        { /*

          https://raw.githubusercontent.com/martinjc/UK-GeoJSON/master/json/administrative/eng/lad.json

          https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Regions_December_2022_EN_BGC/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson
        
        */}
        <Source id="test" type="geojson" data="https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Regions_December_2022_EN_BGC/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson">
          <Layer {...layerStyle} />
        </Source>
      </Map>
    );
  }
}
