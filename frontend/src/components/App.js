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
        'fill-outline-color': '#000000'
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

          https://geoportal.statistics.gov.uk/datasets/ons::ward-to-local-authority-district-to-county-to-region-to-country-december-2022-lookup-in-united-kingdom/explore?filters=eyJSR04yMk5NIjpbIlNvdXRoIEVhc3QiXX0%3D
          https://geoportal.statistics.gov.uk/datasets/ons::ward-to-local-authority-district-to-county-to-region-to-country-december-2022-lookup-in-united-kingdom/api
          https://geoportal.statistics.gov.uk/datasets/ons::regions-december-2022-en-bgc/explore?location=52.174606%2C-0.835117%2C7.02
          https://geoportal.statistics.gov.uk/datasets/ons::counties-and-unitary-authorities-december-2022-uk-bgc/explore?location=52.254844%2C1.463085%2C6.90
          https://geoportal.statistics.gov.uk/datasets/ons::local-authority-districts-december-2022-boundaries-uk-bgc/explore?location=53.025276%2C-1.569960%2C6.90
          
          https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Regions_December_2022_EN_BGC/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson
          https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Local_Authority_Districts_December_2022_Boundaries_UK_BGC/FeatureServer/0/query?outFields=*&where=1%3D1
          https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Local_Authority_Districts_December_2022_Boundaries_UK_BGC/FeatureServer/0/query?where=LAD22CD+like+%27E%25%27&objectIds=&time=&geometry=&geometryType=esriGeometryPolygon&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&relationParam=&returnGeodetic=false&outFields=*&returnGeometry=true&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&defaultSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pgeojson&token=
          https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Wards_December_2022_Boundaries_GB_BGC/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&relationParam=&returnGeodetic=false&outFields=&returnGeometry=true&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&defaultSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pgeojson&token=
        */}
        <Source id="test" type="geojson" data="https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Regions_December_2022_EN_BGC/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson">
          <Layer {...layerStyle} />
        </Source>
      </Map>
    );
  }
}
