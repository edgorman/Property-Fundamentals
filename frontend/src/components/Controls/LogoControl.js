import React from "react";
import { AttributionControl } from "react-map-gl";


export default class LogoControl extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        return (
            <>
                <AttributionControl position={this.props.position}/>
                <button className="mapbox-logo" onClick={this.props.onClick}></button>
            </>
        )
    }
}
