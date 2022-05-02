import React from "react";

class TextField extends React.Component {
    constructor(props, handleChange, id) {
        super(props);
        this.state = {value: ""};
        this.handleChange = this.props.handleChange;
        this.id = this.props.id;

        this.onChange = this.onChange.bind(this)
    }

    onChange(event) {
        this.setState({value: event.target.value})
        this.handleChange(this.id, event.target.value);
    }

    render() {
        return (
            <label>{this.props.name} :
                <input type="text" onChange={this.onChange} value={this.state.value}/>
            </label>
        )
    }
}

export default TextField