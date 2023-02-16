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
        this.requestWDSelections = this.requestWDSelections.bind(this);
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
        const wardKeys = Object.keys(this.props.wards);

        if (wardKeys == 0) {
            return null;
        }

        const params = {
            "where": "WD22CD in ('" + wardKeys.join("', '") + "')",
            "outfields": "WD22CD, WD22NM, LAD22CD, LAD22NM, LAT, LONG",
            "f": "pgeojson"
        }
        return this.state.WDUrl + "?" + EncodeGetParams(params);
    }

    render() {
        // Logic for displaying a LAD or WD on hover
        // WD takes priority over LAD
        let WDHoverFilter = ['==', '', ''];
        let LADHoverFilter = ['==', '', ''];
        if ("WD22CD" in this.props.hover){
            WDHoverFilter = ['==', 'WD22CD', this.props.hover['WD22CD']];
        }
        else if ("LAD22CD" in this.props.hover) {
            LADHoverFilter = ['==', 'LAD22CD', this.props.hover['LAD22CD']];
        }

        return (
            <>
                <Source id="LADOptions" type="geojson" data={this.requestLADOptions()}>
                    <Layer {...LADHiddenStyle} />
                    <Layer {...LADHoverStyle} filter={LADHoverFilter} />
                </Source>
                {/* <Source id="WDOptions" type="geojson" data={this.requestWDOptions()}>
                    <Layer {...WDHiddenStyle} />
                    <Layer {...WDHoverStyle} filter={WDHoverFilter} />
                </Source> */}
                <Source id="WDSelections" type="geojson" data={this.requestWDSelections()}>
                    <Layer {...WDSelectedStyle} />
                    <Layer {...WDHoverStyle} filter={WDHoverFilter} />
                </Source>
            </>
        )
    }
}
