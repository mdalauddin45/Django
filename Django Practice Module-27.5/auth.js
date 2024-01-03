const createNewUser = (event) => {
    event.preventDefault();
    const newUserName = getValue("newUserName");
    const newUserEmail = getValue("newUserEmail");
    const newUserPassword = getValue("newUserPassword");
    const newUserPhone = getValue("newUserPhone");
    const newUserCity = getValue("newUserCity");
    const newUserZipcode = getValue("newUserZipcode");
    const newUserStreet = getValue("newUserStreet");
  
    const newUser = {
      name: {
        firstname: newUserName,
        lastname: "", // You may modify this based on your data structure
      },
      username: newUserName,
      password: newUserPassword,
      email: newUserEmail,
      phone: newUserPhone,
      address: {
        city: newUserCity,
        zipcode: newUserZipcode,
        street: newUserStreet,
      },
    };
    console.log(newUser);
  
    // Send the new user data to the server for creation
    fetch('https://fakestoreapi.com/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newUser),
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
    if (data.id) {
      saveUserToLocalstorage(newUser);

        // If the user was created successfully, navigate to the user list page
      window.location.href = "alluser.html";
    } else {
        console.error("User creation failed");
    }
    })
    .catch(error => console.error('Error:', error));
};
const saveUserToLocalstorage = (user) => {
    // Get existing users from local storage or initialize an empty array
    const existingUsers = JSON.parse(localStorage.getItem("users")) || [];

    // Add the new user to the array
    existingUsers.push(user);

    // Save the updated array back to local storage
    localStorage.setItem("users", JSON.stringify(existingUsers));
};
const getValue = (id) => {
    const value = document.getElementById(id).value;
    return value;
};

const handleLogin = (event) => {
    event.preventDefault();
    const username = getValue("exampleInputEmail1");
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
            if (data.success) {
                window.location.href = "index.html";
            } else {
                console.error("Login failed");
            }
        })
        .catch(error => console.error('Error:', error));
    } else {
        console.error("Username and password are required");
    }
};
