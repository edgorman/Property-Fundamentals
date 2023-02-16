import React from "react";
import ReactSearchBox from "react-search-box";

import Results from "./Results";


export default class Locations extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        // Create nested dictionary of LAD22CD to WD22CD
        let data = {};
        for (const value of Object.values(this.props.wards)) {
            const ladName = value['LAD22NM'];
            const wardName = value['WD22NM'];
            data[ladName] = ladName in data ? {...data[ladName], [wardName]: value} : {[wardName]: value}
        }

        return (
            <div id="locations">
                <div className="d-flex justify-content-between align-items-center">
                    <h3>Locations</h3>
                    <a href="#">How to use?</a>
                </div>
                <br />
                <span>Search for a location in the England...</span>
                <ReactSearchBox 
                    placeholder="e.g. London" />
                <br />
                <span>Total number of wards selected: <b>{Object.keys(this.props.wards).length}</b></span>
                <Results 
                    className=""
                    data={data}
                    show={true}
                    addWard={this.props.addWard}
                    removeWard={this.props.removeWard} />
            </div>
        )
    }
}
