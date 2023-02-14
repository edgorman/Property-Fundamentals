import React from "react";


export default class Outputs extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        return (
            <div id="outputs">
                <div className="d-flex justify-content-between align-items-center">
                    <h3>Outputs</h3>
                    <a href="#">How to use?</a>
                </div>
                <br />
            </div>
        )
    }
}
