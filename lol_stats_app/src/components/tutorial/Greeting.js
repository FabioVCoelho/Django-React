import React from "react";

function UserGreeting() {
    return <h1>Welcome back!</h1>;
}

function GuestGreeting() {
    return <h1>Please sign up.</h1>;
}

class Greeting extends React.Component {
    render() {
        if (this.props.isLoggedIn) {
            return <UserGreeting/>;
        } else {
            return <GuestGreeting/>;
        }
    }
}

export default Greeting