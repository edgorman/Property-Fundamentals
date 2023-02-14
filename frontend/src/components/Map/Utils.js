import bbox from '@turf/bbox';
import { MapStyle } from './Style';

export function ZoomToFeature(map, event){
    let feature = event.features[0]

    if (feature) {
        let [minLng, minLat, maxLng, maxLat] = bbox(feature);

        map.fitBounds(
            [
              [minLng, minLat],
              [maxLng, maxLat]
            ],
            {padding: 40, duration: 1000}
        );
    }
}

export function ZoomToInitialViewState(map){
    map.flyTo({
        center: [
          MapStyle.initialViewState.longitude,
          MapStyle.initialViewState.latitude
        ],
        zoom: MapStyle.initialViewState.zoom,
        essential: true,
        duration: 1500
    });
}
