import React from "react";
import Badge from 'react-bootstrap/Badge';
import ListGroup from "react-bootstrap/ListGroup";
import { CaretDownFill, XLg } from "react-bootstrap-icons";


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
                            <Result name={k} data={v}/>
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
                        <Badge bg="danger" pill role="button" onClick={this.handleRemoveClick}>
                            <XLg />
                        </Badge>
                    </div>
                </div>
                <Results data={this.props.data} show={this.state.show} className="mt-2"/>
            </div>
        );
    }
}
