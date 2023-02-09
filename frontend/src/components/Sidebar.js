import React from "react";

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
                <SidebarToggle open={false} handleToggle={this.props.handleToggle} />
            </div>
        )
    }
}
