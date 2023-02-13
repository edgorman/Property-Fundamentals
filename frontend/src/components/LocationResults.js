import React from "react";
import Badge from 'react-bootstrap/Badge';
import ListGroup from "react-bootstrap/ListGroup";
import { XLg } from "react-bootstrap-icons";


export default class LocationResults extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        if (this.props.data.length == 0){
            return <></>;
        }

        console.log(this.props);
        
        const id = "lr-" + this.props.id;
        const classNames = "collapse show " + this.props.className;
        return (
            <ListGroup id={id} className={classNames}>
                {
                    this.props.data.map((d) => 
                        <ListGroup.Item key={d.id}>
                            <LocationResult id={d.id} data={d.data} />
                            <LocationResults id={d.id} data={d.data} className="mt-2"/>
                        </ListGroup.Item>
                    )
                }
            </ListGroup>
        )
    }
}


class LocationResult extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        const target = "#lr-" + this.props.id;

        return (
            <div 
                className="d-flex justify-content-between align-items-start"
                data-toggle="collapse" 
                data-target={target}
                role="button"
                aria-expanded="false"
                aria-controls={target}
            >
                <span className="pt-1">{this.props.id}</span>
                <div className="location-buttons">
                    {
                        this.props.data.length > 0 ? (
                            <Badge bg="primary" pill>
                                {this.props.data.length}
                            </Badge>
                        ) : null
                    }
                    <Badge bg="danger" pill>
                        <XLg />
                    </Badge>
                </div>
            </div>
        );
    }
}
