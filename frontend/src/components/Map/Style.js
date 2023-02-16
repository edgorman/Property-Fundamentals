
export const MapStyle = {
    mapboxAccessToken: process.env.REACT_APP_MAPBOX_TOKEN,
    initialViewState: {latitude: 54.8, longitude: -2, zoom: 4},
    interactiveLayerIds: [
      'LADHiddenStyle', 'LADHoverStyle', 
      'WDHoverStyle',
      'WDSelectedStyle'
    ],
    doubleClickZoom: false,
    mapStyle: "mapbox://styles/mapbox/streets-v9",
    minZoom: "5",
}

export const LADHiddenStyle = {
  id: 'LADHiddenStyle',
  type: 'fill',
  paint: {
    'fill-opacity': 0.25,
    'fill-color': 'transparent',
    'fill-outline-color': 'black'
  }
}

export const LADHoverStyle = {
  id: 'LADHoverStyle',
  type: 'fill',
  paint: {
    'fill-opacity': 0.1,
    'fill-color': 'black'
  }
}

export const WDHiddenStyle = {
  id: 'WDHiddenStyle',
  type: 'fill',
  paint: {
    'fill-color': 'transparent'
  }
}

export const WDHoverStyle = {
  id: 'WDHoverStyle',
  type: 'fill',
  paint: {
    'fill-opacity': 0.2,
    'fill-color': '#555'
  }
}

export const WDSelectedStyle = {
  id: 'WDSelectedStyle',
  type: 'fill',
  paint: {
    'fill-opacity': 0.2,
    'fill-color': '#555'
  }
}

export const WDOptionalStyle = {
  id: 'WDOptionalStyle',
  type: 'fill',
  paint: {
    'fill-color': 'transparent',
    'fill-outline-color': '#555',
  }
}
