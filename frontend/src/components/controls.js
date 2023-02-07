import React from "react";
import ListGroup from 'react-bootstrap/ListGroup';

import 'bootstrap/dist/css/bootstrap.min.css';


export default class Controls extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        return (
            <div className="mapbox-controls">
                <ListGroup>
                    <ListGroup.Item>
                        <b>1. Choose your locations:</b>
                    </ListGroup.Item>
                    <ListGroup.Item>
                        <b>2. Choose your indicator:</b>
                    </ListGroup.Item>
                    <ListGroup.Item>
                        <b>3. Choose your outputs:</b>
                    </ListGroup.Item>
                </ListGroup>
            </div>
        )
    }
}
