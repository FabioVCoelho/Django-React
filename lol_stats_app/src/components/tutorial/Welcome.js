import React from "react";

class Welcome extends React.Component {
    render() {
        return <h1>Hello, {this.formatName(this.props.user)}</h1>
    }

    formatName(user) {
        return user.firstName + ' ' + user.lastName
    }

}

export default Welcome;