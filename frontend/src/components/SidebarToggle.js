import React from "react";

import { ArrowBarLeft, ArrowBarRight } from "react-bootstrap-icons";

export default class ControlsToggle extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        let arrowBar = <ArrowBarRight className="align-middle" />
        if (this.props.open) {
            arrowBar = <ArrowBarLeft className="align-middle" />
        }

        return (
            <div className="mapbox-sidebar-toggle" onClick={this.props.handleToggle}>
                {arrowBar}
            </div>
        )
    }
}
