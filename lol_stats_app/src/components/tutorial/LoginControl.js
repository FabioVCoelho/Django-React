import React from "react";
import Greeting from "./Greeting";
import Button from "../Button/Button";

class LoginControl extends React.Component {
    constructor(props) {
        super(props);
        this.handleLoginClick = this.handleLoginClick.bind(this);
        this.handleLogoutClick = this.handleLogoutClick.bind(this);
        this.state = {isLoggedIn: false};
    }

    handleLoginClick() {
        this.setState({isLoggedIn: true});
    }

    handleLogoutClick() {
        this.setState({isLoggedIn: false});
    }

    render() {
        const isLoggedIn = this.state.isLoggedIn;
        let button;
        if (isLoggedIn) {
            button = <Button onClick={this.handleLogoutClick} text={"Logout"}/>;
        } else {
            button = <Button onClick={this.handleLoginClick} text={"Login"}/>;
        }

        return (<div>
            <Greeting isLoggedIn={isLoggedIn}/>
            {button}
        </div>);
    }

    componentDidMount() {
    }

    componentWillUnmount() {
    }
}

export default LoginControl