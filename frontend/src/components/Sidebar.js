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
                <div className="content">
                </div>
                <div className="buttons">
                    <SidebarToggle open={false} handleToggle={this.props.handleToggle} />
                </div>
            </div>
        )
    }
}
