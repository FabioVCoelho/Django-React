import './App.css';
import Welcome from "./components/tutorial/Welcome";
import Clock from "./components/tutorial/Clock";
import Toggle from "./components/tutorial/Toggle";
import LoginControl from "./components/tutorial/LoginControl";
import Page from "./components/tutorial/WarningBanner";
import Form from "./components/tutorial/Form";
import FormCustom from "./components/tutorial/FormCustom";
import TextArea from "./components/tutorial/TextArea";
import SelectTheFruit from "./components/tutorial/SelectTheFruit";
import SelectMutipleFruits from "./components/tutorial/SelectMutipleFruits";
import Reservation from "./components/tutorial/Reservation";

// Data
const user = {firstName: "João", lastName: "Alvez"}
const user2 = {firstName: "Maria", lastName: "Pereira"}
const users = [user, user2]

// View
function App() {
    return (<div>
        <h1> Examples from tutorial</h1>
        <h3>User</h3>
        {users.map(user => {
            return <Welcome user={user} key={user.firstName}/>
        })}
        <hr/>
        <h3>Clock states</h3>
        <Clock/>
        <hr/>
        <h3>Toggle component actions</h3>
        <Toggle/>
        <hr/>
        <h3>Login Control conditional component</h3>
        <LoginControl/>
        <hr/>
        <h3>Show and hide a component</h3>
        <Page/>
        <hr/>
        <h3>Form</h3>
        <Form/>
        <hr/>
        <h3>Form custom based on fields props</h3>
        <FormCustom fields={[{"name": "Login", "value": ""}, {"name": "Password", "value": ""}]}/>
        <hr/>
        <h3> Text Area</h3>
        <TextArea></TextArea>
        <hr/>
        <h3>Select with only one option</h3>
        <SelectTheFruit></SelectTheFruit>
        <hr/>
        <h3>Select with multiple options</h3>
        <SelectMutipleFruits></SelectMutipleFruits>
        <hr/>
        <h3>Reservation tutorial</h3>
        <Reservation></Reservation>
    </div>);
}

export default App;
