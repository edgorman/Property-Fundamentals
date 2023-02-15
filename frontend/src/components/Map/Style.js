
export const MapStyle = {
    mapboxAccessToken: process.env.REACT_APP_MAPBOX_TOKEN,
    initialViewState: {latitude: 54.8, longitude: -2, zoom: 4},
    interactiveLayerIds: ['FillStyle', 'OutlineHiddenStyle'], //, 'OutlineStyle2', 'FillStyle'],
    doubleClickZoom: false,
    mapStyle: "mapbox://styles/mapbox/streets-v9",
    minZoom: "5",
}

export const OutlineStyle = {
    id: 'OutlineStyle',
    type: 'fill',
    paint: {
      'fill-color': 'transparent',
      'fill-outline-color': '#555',
    }
};

export const OutlineStyle2 = {
  id: 'OutlineStyle2',
  type: 'fill',
  paint: {
    'fill-color': 'transparent',
    'fill-outline-color': 'red',
  }
};

export const OutlineHiddenStyle = {
  id: 'OutlineHiddenStyle',
  type: 'fill',
  paint: {
    'fill-color': 'transparent',
  }
}

export const FillStyle = {
    id: 'FillStyle',
    type: 'fill',
    paint: {
      'fill-opacity': 0.2,
      'fill-color': '#555',
      'fill-outline-color': '#000',
    }
}
