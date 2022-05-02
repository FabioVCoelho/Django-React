import React from "react";

class SelectTheFruit extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value: "coconut"}
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }

    handleSubmit(event) {
        alert("You have chosen the fruit " + this.state.value)
        event.preventDefault();
    }

    handleChange(event) {
        this.setState({value: event.target.value})
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label>
                    Choose your fruit:
                </label>
                <select value={this.state.value} onChange={this.handleChange}>
                    <option value="coconut">Coconut</option>
                    <option value="strawberry">Strawberry</option>
                    <option value="pineapple">Pineapple</option>
                    <option value="banana">Banana</option>
                </select>
                <input type="submit" value="Submit"/>
            </form>
        )
    }
}

export default SelectTheFruit;