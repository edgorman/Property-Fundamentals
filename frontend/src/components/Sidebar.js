import React from "react";
import Breadcrumb from 'react-bootstrap/Breadcrumb';

import Locations from "./Locations";
import SidebarToggle from './SidebarToggle';

import Col from 'react-bootstrap/Col';
import Nav from 'react-bootstrap/Nav';
import Row from 'react-bootstrap/Row';
import Tab from 'react-bootstrap/Tab';


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
                            <p>second</p>
                        </Tab.Pane>
                        <Tab.Pane eventKey="third">
                            <p>third</p>
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
                {/* <div className="content">
                    <Locations />
                </div>
                <div className="buttons d-flex align-items-center">
                    <Breadcrumb>
                        <Breadcrumb.Item active>Locations</Breadcrumb.Item>
                        <Breadcrumb.Item>Features</Breadcrumb.Item>
                        <Breadcrumb.Item>Explanation</Breadcrumb.Item>
                    </Breadcrumb>
                    <SidebarToggle open={false} handleToggle={this.props.handleToggle} />
                </div> */}
            </div>
        )
    }
}
