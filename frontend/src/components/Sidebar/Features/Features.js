import React from "react";


export default class Features extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        return (
            <div id="features">
                <div className="d-flex justify-content-between align-items-center">
                    <h3>Features</h3>
                    <a href="#">How to use?</a>
                </div>
                <br />
            </div>
        )
    }
}
