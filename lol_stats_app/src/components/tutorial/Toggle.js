import React from "react";

class Toggle extends React.Component {
    constructor(props) {
        super(props);
        this.state = {isToggleOn: true};
        //This binding is necessary to make 'this' work in the callback
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick() {
        this.setState(prevState => ({
            isToggleOn: !prevState.isToggleOn
        }));
    }

    render() {
        return (
            <button onClick={this.handleClick}>
                {this.state.isToggleOn ? 'On' : 'Off'}
            </button>
        );
        // This syntax ensures `this` is bound within handleClick
        // return (
        //     <button onClick={() => this.handleClick()}>
        //         Click me
        //     </button>
        // );
    }

    componentDidMount() {
    }

    componentWillUnmount() {
    }
}

export default Toggle;