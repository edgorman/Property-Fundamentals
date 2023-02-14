
export const MapStyle = {
    mapboxAccessToken: process.env.REACT_APP_MAPBOX_TOKEN,
    initialViewState: {latitude: 54.8, longitude: -2, zoom: 4},
    interactiveLayerIds: ['OutlineStyle', 'FillStyle'],
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

export const FillStyle = {
    id: 'FillStyle',
    type: 'fill',
    paint: {
      'fill-opacity': 0.2,
      'fill-color': '#555',
      'fill-outline-color': '#000',
    }
}
