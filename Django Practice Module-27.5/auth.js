const createNewUser = (event) => {
    event.preventDefault();
    const newUserEmail = getValue("newUserEmail");
    const newUserName = getValue("newUserName");
    const newUserPassword = getValue("newUserPassword");
    const firstname = getValue("firstname");
    const lastname = getValue("lastname");
    const newUserCity = getValue("newUserCity");
    const newUserStreet = getValue("newUserStreet");
    const number = getValue("num");
    const newUserZipcode = getValue("newUserZipcode");
    const lat = getValue("lat");
    const long = getValue("long");
    const newUserPhone = getValue("newUserPhone");
  
    const newUser = {
      email: newUserEmail,
      username: newUserName,
      password: newUserPassword,
      name: {
        firstname: firstname,
        lastname: lastname,
      },
      address: {
        city: newUserCity,
        street: newUserStreet,
        number: number,
        zipcode: newUserZipcode,
        geolocation:{
          lat,
          long,
        },
      },
      phone: newUserPhone,
    };
    console.log(newUser);
    fetch('https://fakestoreapi.com/users',{
      method:"POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body:JSON.stringify(newUser),
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      // window.location.href = "alluser.html";
    })
    .catch(error => console.error('Error:', error));
};
const getValue = (id) => {
    const value = document.getElementById(id).value;
    return value;
};

const handleLogin = (event) => {
    event.preventDefault();
    const username = getValue("username");
    const password = getValue("exampleInputPassword1");
    
    if (username && password) {
        fetch('https://fakestoreapi.com/auth/login', {
            method: 'POST',
            headers: { "content-type": "application/json" },
            body: JSON.stringify({ username, password })
        })
        .then(res => res.json())
        .then(data => {
            console.log(data);
            if (data.token ) {
              localStorage.setItem("token", data.token);
              window.location.href = "index.html";
            }
        })
        .catch(error => console.error('Error:', error));
    } else {
        console.error("Username and password are required");
    }
};
