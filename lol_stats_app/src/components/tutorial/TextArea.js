import React from "react";

class TextArea extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value: "Please write an essay about your favorite LoL character."}
        this.handleSubmit = this.handleSubmit.bind(this);
        this.onChange = this.onChange.bind(this);
    }

    onChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        alert('An essay was submitted: ' + this.state.value);
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label>
                    Essay:
                </label>
                <textarea value={this.state.value} onChange={this.onChange}></textarea>
                <input type="submit" value="Submit"/>
            </form>
        );
    }
}

export default TextArea;