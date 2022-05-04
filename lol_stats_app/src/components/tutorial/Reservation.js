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
        var text = ""
        if (this.state.isGoing) {
            text = "You are going! With " + this.state.numberOfGuests + " guests!"
        } else {
            text = "You are not going! =/"
        }
        alert(text)
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
                <br/>
                <input type="submit" value="Submit"/>

            </form>
        );
    }

}

export default Reservation