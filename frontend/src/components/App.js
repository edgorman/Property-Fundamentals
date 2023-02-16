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
      mouseHoverElement: {},
      wards: {}
    }

    this.handleResetViewClick = this.handleResetViewClick.bind(this);
    this.handleSidebarToggle = this.handleSidebarToggle.bind(this);
    this.handleClick = this.handleClick.bind(this);
    this.handleDoubleClick = this.handleDoubleClick.bind(this);
    this.handleRightClick = this.handleRightClick.bind(this);
    this.handleMouseMove = this.handleMouseMove.bind(this);

    this.addWard = this.addWard.bind(this);
    this.removeWard = this.removeWard.bind(this);
  }

  handleResetViewClick() {
    this.setState({sidebarActive: false});
    ZoomToInitialViewState(this.map);
  }

  handleSidebarToggle() {
    this.setState({sidebarActive: !this.state.sidebarActive});
  }

  handleClick(e) {
    const feature = e.features[0];

    if (feature) {
      if (feature.source == 'LADOptions') {
        GetWDsFromLAD(feature.properties['LAD22CD'])
          .then(wards => {
            for (const ward of wards){
              this.addWard(ward.properties);
            }
          });
      }
      else if (feature.source == 'WDOptions') {
        this.addWard(feature.properties)
      }
      else {
        console.log("Info: no event configured for event from source: '" + feature.source + "'.");
      }
    }
  }

  handleDoubleClick(e) {
    ZoomToFeature(this.map, e);
  }

  handleRightClick(e) {
    const feature = e.features[0];

    if (feature){
      if (feature.source == 'WDSelections') {
        this.removeWard(feature.properties)
      }
      else {
        console.log("Info: no event configured for event from source: '" + feature.source + "'.");
      }
    }
  }

  handleMouseMove(e) {
    const feature = e.features[0];

    if (feature){
      this.setState({mouseHoverElement: feature.properties});
    }
    else{
      this.setState({mouseHoverElement: {}});
    }
  }

  addWard(ward) {
    if (!(ward['WD22CD'] in this.state.wards)) {
      this.setState(prevState => ({wards: {...prevState.wards, [ward['WD22CD']]: ward}}))
    }
    else{
      console.log("Info: this map already has ward '" + ward['WD22CD'] + "' in it's list of wards, not adding this.");
    }
  }

  removeWard(ward) {
    if (ward['WD22CD'] in this.state.wards) {
      let new_wards = this.state.wards;
      delete new_wards[ward['WD22CD']];
      this.setState({wards: new_wards});
    }
    else{
      console.log("Info: this map does not have ward '" + ward['WD22CD'] + "' in it's list of wards, not removing this.");
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

        <Sidebar
          active={this.state.sidebarActive}
          handleToggle={this.handleSidebarToggle}
          map={this.map}
          wards={this.state.wards} 
          addWard={this.addWard}
          removeWard={this.removeWard} />
        <SidebarToggle open={true} handleToggle={this.handleSidebarToggle} />

        <MapLayers hover={this.state.mouseHoverElement} wards={this.state.wards} />
      </Map>
    );
  }
}
