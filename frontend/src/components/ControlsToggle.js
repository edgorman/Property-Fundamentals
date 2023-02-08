import React from "react";

import { ArrowBarLeft } from "react-bootstrap-icons";

export default class ControlsToggle extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        return (
            <div className="mapbox-controls-toggle">
                <ArrowBarLeft className="align-middle"/>
            </div>
        )
    }
}
