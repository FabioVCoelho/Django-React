import React from "react";

class SelectMutipleFruits extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value: ["coconut"]};
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        this.setState({value: Array.from(event.target.selectedOptions, option => option.value)})
    }

    handleSubmit(event) {
        alert("You have chosen the fruit " + this.state.value)
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label>
                    Choose your fruits:
                </label>
                <br/>
                <select multiple={true} value={this.state.value} name="selectOptions" onChange={this.handleChange}>
                    <option value="coconut">Coconut</option>
                    <option value="strawberry">Strawberry</option>
                    <option value="pineapple">Pineapple</option>
                    <option value="banana">Banana</option>
                </select>
                <label>You have selected {this.state.value.length} fruit{this.state.value.length > 1 ? 's' : ''}</label>
                <br/>
                <input type="submit" value="Submit"/>
                <br/>

            </form>
        )
    }
}

export default SelectMutipleFruits;