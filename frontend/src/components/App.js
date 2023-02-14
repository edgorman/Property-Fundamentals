import React from 'react';
import Map, {NavigationControl, GeolocateControl } from 'react-map-gl';

import Sidebar from './Sidebar/Sidebar';
import SidebarToggle from './Sidebar/Toggle';
import LogoControl from './Controls/LogoControl';
import MapLayers from './Map/Layers';
import { MapStyle } from './Map/Style';
import { ZoomToFeature, ZoomToInitialViewState } from './Map/Utils';

import './App.css';


export default class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      sidebarActive: false
    }

    this.handleResetViewClick = this.handleResetViewClick.bind(this);
    this.handleSidebarToggle = this.handleSidebarToggle.bind(this);
    this.handleMapClick = this.handleMapClick.bind(this);
  }

  handleResetViewClick() {
    this.setState({sidebarActive: false});
    ZoomToInitialViewState(this.map);
  }

  handleSidebarToggle() {
    this.setState({sidebarActive: !this.state.sidebarActive});
  }

  handleMapClick(e) {
    this.setState({sidebarActive: false});
    ZoomToFeature(this.map, e);
  }

  render() {
    return (
      <Map
        onClick={this.handleMapClick}
        ref={(e) => { this.map = e; }}
        {...MapStyle}
      >
        <LogoControl position="top-left" onClick={this.handleResetViewClick} />
        <NavigationControl position="top-left" visualizePitch={true} />
        <GeolocateControl position="top-left" />

        <Sidebar active={this.state.sidebarActive} handleToggle={this.handleSidebarToggle} />
        <SidebarToggle open={true} handleToggle={this.handleSidebarToggle} />

        <MapLayers />
      </Map>
    );
  }
}
