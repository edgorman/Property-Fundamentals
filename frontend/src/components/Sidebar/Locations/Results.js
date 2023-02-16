import React from "react";
import Badge from "react-bootstrap/Badge";
import ListGroup from "react-bootstrap/ListGroup";
import { CaretDownFill, GeoAltFill, XLg } from "react-bootstrap-icons";

import { ZoomToFeature } from "../../Map/Utils";


export default class Results extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        if (Object.keys(this.props.data).length <= 0 || "LAD22CD" in this.props.data){
            return <></>;
        }

        let classNames = this.props.className + " collapse ";
        classNames += this.props.show ? "show" : "";

        return (
            <ListGroup className={classNames}>
                {
                    Object.entries(this.props.data).map(([k, v]) =>
                        <ListGroup.Item key={k}>
                            <Result 
                                name={k}
                                data={v}
                                map={this.props.map}
                                addWard={this.props.addWard}
                                removeWard={this.props.removeWard} />
                        </ListGroup.Item>
                    )
                }
            </ListGroup>
        )
    }
}


class Result extends React.Component {
    constructor(props){
        super(props);

        this.state = {
            show: true
        }

        this.handleCollapseToggle = this.handleCollapseToggle.bind(this);
        this.handleZoomClick = this.handleZoomClick.bind(this);
        this.handleRemoveClick = this.handleRemoveClick.bind(this);
    }

    handleCollapseToggle() {
        this.setState({
            show: !this.state.show
        })
    }

    handleZoomClick() {
        // TODO: This requires the positional information for LADs and WDs
        // Only wards are available at this time
        if ("WD22CD" in this.props.data) {
            console.log("Zoom to WD", this.props.data);
            // ZoomToFeature(this.props.map, this.props.data);
        }
        else {
            console.log("Zoom to LAD", this.props.data);
            // ZoomToFeature(this.props.map, this.props.data);
        }
    }

    handleRemoveClick() {
        if ("WD22CD" in this.props.data) {
            this.props.removeWard(this.props.data);
        }
        else {
            for (const ward of Object.values(this.props.data)) {
                this.props.removeWard(ward);
            }
        }
    }

    render() {
        const count = "LAD22CD" in this.props.data ? 0 : Object.keys(this.props.data).length

        return (
            <div>
                <div className="d-flex">
                    <span className="pt-1 flex-grow-1" role="button" onClick={this.handleCollapseToggle}>
                        {this.props.name}
                        {
                            count > 0 ? (
                                <CaretDownFill style={{color: "#898989", marginLeft: "10px"}}/>
                            ) : null
                        }
                    </span>
                    <div className="location-buttons">
                        {
                            count > 0 ? (
                                <Badge bg="primary" pill>
                                    {count}
                                </Badge>
                            ) : null
                        }
                        <Badge bg="secondary" pill role="button" onClick={this.handleZoomClick}>
                            <GeoAltFill />
                        </Badge>
                        <Badge bg="danger" pill role="button" onClick={this.handleRemoveClick}>
                            <XLg />
                        </Badge>
                    </div>
                </div>
                <Results 
                    className="mt-2"
                    map={this.props.map}
                    data={this.props.data}
                    show={this.state.show}
                    addWard={this.props.addWard}
                    removeWard={this.props.removeWard} />
            </div>
        );
    }
}
