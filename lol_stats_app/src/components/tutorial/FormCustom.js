import React from "react";
import TextField from "../forms/TextField/TextField";

class FormCustom extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value: ""}
        this.fields = [...this.props.fields]
        this.handleFieldChange = this.handleFieldChange.bind(this)

    }

    handleFieldChange(fieldId, value) {
        this.fields.find(x => x.name === fieldId).value = value
    }

    render() {
        return (
            <form>
                {this.fields.map(field => <TextField value="" name={field.name} handleChange={this.handleFieldChange} id={field.name}
                                                     key={field.name}/>)}
            </form>
        )
    }

}

export default FormCustom