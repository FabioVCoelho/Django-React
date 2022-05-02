import React from "react";

class Reservation extends React.Component {
    constructor(props) {
        super(props);
        this.state = {isGoing: false, numberOfGuests: 1}
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleInputChange(event) {
        const name = event.target.name;
        const value = event.target.type === 'checkbox' ? event.target.checked : event.target.value
        this.setState({[name]: value})
    }

    handleSubmit(event) {
        alert("You are" + this.state.isGoing ? "" : " not " + "going with " + this.state.numberOfGuests)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label>Is going:</label>
                <input name="isGoing" type="checkbox" checked={this.state.isGoing} onChange={this.handleInputChange}/>
                <br/>
                <label>How many guests:</label>
                <input name="numberOfGuests" type="number" value={this.state.numberOfGuests} onChange={this.handleInputChange}/>
            </form>
        );
    }

}

export default Reservation