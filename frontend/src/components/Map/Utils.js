import bbox from '@turf/bbox';
import { MapStyle } from './Style';

export function EncodeGetParams(params) {
    return Object.entries(params).map(kv => kv.map(encodeURIComponent).join("=").replace(/'/g, "%27")).join("&");
}

export function ZoomToFeature(map, event) {
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

export function ZoomToInitialViewState(map) {
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

export function GetWDsFromLAD(lad) {
    const params = {
        "where": "LAD22CD like '" + lad + "'",
        "outfields": "WD22CD, WD22NM, LAD22CD, LAD22NM, LAT, LONG",
        "returnGeometry": false,
        "f": "pgeojson"
    };

    return new Promise(
        resolve => {
            fetch("https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Wards_December_2022_Boundaries_GB_BGC/FeatureServer/0/query" + "?" + EncodeGetParams(params))
                .then(response => response.json())
                .then(response => {
                    resolve(response.features);
                })
                .catch(error => console.log(error));
        }
    );
}
