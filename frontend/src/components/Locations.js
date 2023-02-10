import React from "react";


export default class Locations extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        return (
            <div id="locations">
                <div className="d-flex justify-content-between align-items-center">
                    <h3>Locations</h3>
                    <a href="#">How to use?</a>
                </div>
            </div>
        )
    }
}
