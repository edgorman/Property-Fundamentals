import React from "react";
import ReactSearchBox from "react-search-box";

import LocationResults from "./LocationResults";


export default class Locations extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        const data = [
            {id: "Southampton", data:[{id: "Basset", data:[]}, {id:"Portswood", data:[]}]},
            {id: "Southampton1", data:[{id: "Basset", data:[]}, {id:"Portswood", data:[]}]},
            {id: "Southampton2", data:[{id: "Basset", data:[]}, {id:"Portswood", data:[]}]},
            {id: "Southampton3", data:[{id: "Basset", data:[]}, {id:"Portswood", data:[]}]},
            {id: "Southampton4", data:[{id: "Basset", data:[]}, {id:"Portswood", data:[]}]},
        ];
        const count = 2;

        return (
            <div id="locations">
                <div className="d-flex justify-content-between align-items-center">
                    <h3>Locations</h3>
                    <a href="#">How to use?</a>
                </div>
                <br />
                <span>Search for a location in the England...</span>
                <ReactSearchBox placeholder="e.g. London" />
                <br />
                <span>Total number of wards selected: <b>{count}</b></span>
                <LocationResults className="" data={data} show={true}/>
            </div>
        )
    }
}
