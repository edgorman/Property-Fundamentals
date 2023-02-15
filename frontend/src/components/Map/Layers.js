import React from "react";
import { Source, Layer } from 'react-map-gl';

import { EncodeGetParams } from "./Utils";
import { LADHiddenStyle, LADHoverStyle, WDHiddenStyle, WDHoverStyle, WDSelectedStyle, WDOptionalStyle } from "./Style";


export default class MapLayers extends React.Component {
    constructor(props){
        super(props);

        this.state = {
            LADUrl: "https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Local_Authority_Districts_December_2022_Boundaries_UK_BGC/FeatureServer/0/query",
            WDUrl: "https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Wards_December_2022_Boundaries_GB_BGC/FeatureServer/0/query"
        }

        this.requestLADOptions = this.requestLADOptions.bind(this);
        this.requestWDOptions = this.requestWDOptions.bind(this);
    }

    requestLADOptions() {
        // LAD Options are every LAD in England
        const params = {
            "where": "LAD22CD like 'E%'",
            "outfields": "LAD22CD, LAD22NM",
            "f": "pgeojson"
        }
        return this.state.LADUrl + "?" + EncodeGetParams(params);
    }

    requestWDOptions() {
        // WD options are neighbouring WDs to those already selected
        const params = {
            "where": "LAD22CD like 'E06000045'",
            "outfields": "WD22CD, WD22NM, LAD22CD, LAD22NM, LAT, LONG",
            "f": "pgeojson"
        }
        return this.state.WDUrl + "?" + EncodeGetParams(params);
    }

    requestWDSelections() {
        // WD selections are wards that have been selected by the user
    }

    render() {
        // Logic for displaying a LAD or WD on hover
        // WD takes priority over LAD
        let WDHoverFilter = ['==', '', ''];
        let LADHoverFilter = ['==', '', ''];
        if ("WD22CD" in this.props.highlight){
            WDHoverFilter = ['==', 'WD22CD', this.props.highlight['WD22CD']];
        }
        else if ("LAD22CD" in this.props.highlight) {
            LADHoverFilter = ['==', 'LAD22CD', this.props.highlight['LAD22CD']];
        }

        return (
            <>
                <Source id="LADOptions" type="geojson" data={this.requestLADOptions()}>
                    <Layer {...LADHiddenStyle} />
                    <Layer {...LADHoverStyle} filter={LADHoverFilter} />
                </Source>
                <Source id="WDOptions" type="geojson" data={this.requestWDOptions()}>
                    <Layer {...WDHiddenStyle} />
                    <Layer {...WDHoverStyle} filter={WDHoverFilter} />
                </Source>
            </>
        )

        // let filter = ['==', '', ''];
        // if ("WD22CD" in this.props.highlight) {
        //     filter = ['==', 'WD22CD', this.props.highlight['WD22CD']]
        // }
        // else if ("LAD22CD" in this.props.highlight) {
        //     filter = ['==', 'LAD22CD', this.props.highlight['LAD22CD']]
        // }

        // return (
        //     <>
        //         <Source id="LADSource" type="geojson" data="https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Local_Authority_Districts_December_2022_Boundaries_UK_BGC/FeatureServer/0/query?where=LAD22CD+like+%27E%25%27&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&relationParam=&returnGeodetic=false&outFields=LAD22CD%2C+LAD22NM&returnGeometry=true&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&defaultSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pgeojson&token=">
        //             <Layer {...OutlineHiddenStyle} />
        //             <Layer {...FillStyle} filter={filter} />
        //         </Source>
        //         <Source id="WDSource" type="geojson" data="https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Wards_December_2022_Boundaries_GB_BGC/FeatureServer/0/query?where=%28LONG+BETWEEN+-1.5+AND+-1.3%29+AND+%28LAT+BETWEEN+50.85+AND+50.95%29&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=&units=esriSRUnit_Meter&relationParam=&returnGeodetic=false&outFields=*&returnGeometry=true&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&defaultSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=0&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pgeojson&token=">
        //             <Layer {...OutlineStyle2} />
        //         </Source>
        //         <Source id="WDSelection" type="geojson" data="https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Wards_December_2022_Boundaries_GB_BGC/FeatureServer/0/query?where=WD22CD+IN+%28%27E05002455%27%2C+%27E05002457%27%2C+%27E05002461%27%29&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&relationParam=&returnGeodetic=false&outFields=WD22CD%2C+WD22NM%2C+LAD22CD%2C+LAD22NM&returnGeometry=true&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&defaultSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pgeojson&token=">
        //             <Layer {...FillStyle2} />
        //         </Source>
        //     </>
        // )
    }
}
