import React from 'react';
import Map, {NavigationControl, GeolocateControl } from 'react-map-gl';

import Sidebar from './Sidebar/Sidebar';
import SidebarToggle from './Sidebar/Toggle';
import LogoControl from './Controls/LogoControl';
import MapLayers from './Map/Layers';
import { MapStyle } from './Map/Style';
import { ZoomToFeature, ZoomToInitialViewState, GetWDsFromLAD } from './Map/Utils';

import './App.css';


export default class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      sidebarActive: false,
      highlight: {},
      locations: {
        //E05002456: {LADCD: "E060000001", LADNM: "Hartlepool", WDNM: "Hartlepool"}
      }
    }

    this.handleResetViewClick = this.handleResetViewClick.bind(this);
    this.handleSidebarToggle = this.handleSidebarToggle.bind(this);
    this.handleClick = this.handleClick.bind(this);
    this.handleDoubleClick = this.handleDoubleClick.bind(this);
    this.handleRightClick = this.handleRightClick.bind(this);
    this.handleMouseMove = this.handleMouseMove.bind(this);
  }

  handleResetViewClick() {
    this.setState({sidebarActive: false});
    ZoomToInitialViewState(this.map);
  }

  handleSidebarToggle() {
    this.setState({sidebarActive: !this.state.sidebarActive});
  }

  handleClick(e) {
    this.setState({sidebarActive: false});

    if (e.features[0]){
      console.log("add", e.features[0].source, e.features[0].properties);
      
      // GetWDsFromLAD(e.features[0].properties['LAD22CD'])
      //   .then(wards => {
      //     console.log("here")
      //     console.log(wards);
      //   });
    }
  }

  handleDoubleClick(e) {
    this.setState({sidebarActive: false});
    ZoomToFeature(this.map, e);
  }

  handleRightClick(e) {
    this.setState({sidebarActive: false});
    
    if (e.features[0]){
      console.log("remove", e.features[0].source, e.features[0].properties);
    }
  }

  handleMouseMove(e) {
    if (e.features[0]){
      this.setState({highlight: e.features[0].properties});
    }
    else{
      this.setState({highlight: {}});
    }
  }

  render() {
    return (
      <Map
        onClick={this.handleClick}
        onDblClick={this.handleDoubleClick}
        onContextMenu={this.handleRightClick}
        onMouseMove={this.handleMouseMove}
        ref={(e) => { this.map = e; }}
        {...MapStyle}
      >
        <LogoControl position="top-left" onClick={this.handleResetViewClick} />
        <NavigationControl position="top-left" visualizePitch={true} />
        <GeolocateControl position="top-left" />

        <Sidebar active={this.state.sidebarActive} handleToggle={this.handleSidebarToggle} />
        <SidebarToggle open={true} handleToggle={this.handleSidebarToggle} />

        <MapLayers highlight={this.state.highlight} select={this.state.selections} />
      </Map>
    );
  }
}
