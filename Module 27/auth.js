const handleRegistration =(event)=>{
    event.preventDefault();
    const username = getValue("username");
    const firstname = getValue("first_name");
    const lastname = getValue("last_name");
    const email = getValue("email");
    const pass1 = getValue("password");
    const pass2 = getValue("confirm_password");
    const info = {
        username: username,
        firstname: firstname,
        lastname: lastname,
        email: email,
        pass1: pass1,
        pass2: pass2
    };
    console.log(info);

}
const getValue=(id)=>{
    const value = document.getElementById(id).value;
    return value;
};