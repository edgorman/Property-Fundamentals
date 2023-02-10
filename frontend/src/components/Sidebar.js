import React from "react";
import Breadcrumb from 'react-bootstrap/Breadcrumb';

import Locations from "./Locations";
import SidebarToggle from './SidebarToggle';


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
                <div className="content">
                    <Locations />
                </div>
                <div className="buttons d-flex align-items-center">
                    <Breadcrumb>
                        <Breadcrumb.Item active>Locations</Breadcrumb.Item>
                        <Breadcrumb.Item>Features</Breadcrumb.Item>
                        <Breadcrumb.Item>Explanation</Breadcrumb.Item>
                    </Breadcrumb>
                    <SidebarToggle open={false} handleToggle={this.props.handleToggle} />
                </div>
            </div>
        )
    }
}
