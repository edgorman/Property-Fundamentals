import React from "react";
import Nav from 'react-bootstrap/Nav';
import Tab from 'react-bootstrap/Tab';
import Features from "../Features/Features";

import Locations from "../Locations/Locations";
import Outputs from "../Outputs/Outputs";
import SidebarToggle from './Toggle';


export default class Sidebar extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        let classNames = "mapbox-sidebar";
        if (this.props.isActive){
            classNames += " active";
        }

        return (
            <div className={classNames}>
                <Tab.Container defaultActiveKey="first">
                    <Tab.Content className="content">
                        <Tab.Pane eventKey="first">
                            <Locations />
                        </Tab.Pane>
                        <Tab.Pane eventKey="second">
                            <Features />
                        </Tab.Pane>
                        <Tab.Pane eventKey="third">
                            <Outputs />
                        </Tab.Pane>
                    </Tab.Content>
                    <Nav className="buttons d-flex align-items-center">
                        <Nav.Item>
                            <Nav.Link eventKey="first">Locations</Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                            /
                        </Nav.Item>
                        <Nav.Item>
                            <Nav.Link eventKey="second">Features</Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                            /
                        </Nav.Item>
                        <Nav.Item>
                            <Nav.Link eventKey="third">Explanation</Nav.Link>
                        </Nav.Item>
                        <SidebarToggle open={false} handleToggle={this.props.handleToggle} />
                    </Nav>
                </Tab.Container>
            </div>
        )
    }
}
