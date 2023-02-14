import React from "react";
import Badge from 'react-bootstrap/Badge';
import ListGroup from "react-bootstrap/ListGroup";
import { CaretDownFill, XLg } from "react-bootstrap-icons";


export default class Results extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        if (this.props.data.length == 0){
            return <></>;
        }

        let classNames = this.props.className + " collapse ";
        classNames += this.props.show ? "show" : "";

        return (
            <ListGroup className={classNames}>
                {
                    this.props.data.map((d) => 
                        <ListGroup.Item key={d.id}>
                            <Result id={d.id} data={d.data}/>
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
        this.handleRemoveClick = this.handleRemoveClick.bind(this);
    }

    handleCollapseToggle(){
        this.setState({
            show: !this.state.show
        })
    }

    handleRemoveClick(){
        console.log("Remove", this.props.id);
    }

    render() {
        return (
            <div>
                <div className="d-flex">
                    <span className="pt-1 flex-grow-1" role="button" onClick={this.handleCollapseToggle}>
                        {this.props.id}
                        {
                            this.props.data.length > 0 ? (
                                <CaretDownFill style={{color: "#898989", marginLeft: "10px"}}/>
                            ) : null
                        }
                    </span>
                    <div className="location-buttons">
                        {
                            this.props.data.length > 0 ? (
                                <Badge bg="primary" pill>
                                    {this.props.data.length}
                                </Badge>
                            ) : null
                        }
                        <Badge bg="danger" pill role="button" onClick={this.handleRemoveClick}>
                            <XLg />
                        </Badge>
                    </div>
                </div>
                <Results id={this.props.id} data={this.props.data} show={this.state.show} className="mt-2"/>
            </div>
        );
    }
}
