const loadUser=(value)=>{
    document.getElementById("alluser").innerHTML = "";
    document.getElementById("spinner").style.display = "block";
    fetch(`https://fakestoreapi.com/users/${value?  value: " "}`)
    .then((res)=>res.json())
    .then((data)=>{
        console.log(data);
        document.getElementById("spinner").style.display = "none";
        if(Array.isArray(data)){
            if (data?.length > 0 ) {
                document.getElementById("nodata").style.display = "none";
                displayUsers(data);
            } else {
                document.getElementById("nodata").style.display = "block";
            }
        }else{
            displayUser(data);
        }
    })
    .catch((err) => console.log(err));
};
const displayUsers=(users)=>{
    users?.forEach(user => {
        displayUser(user);
    });
}
const displayUser=(user)=>{
    const parent = document.getElementById("alluser");
    const div = document.createElement("div");
    div.classList.add("col-lg-3", "mb-lg-0", "col-md-6","col-12", "card-container");
    div.innerHTML = `
    <div class="card rounded shadow-sm border-0">
        <div class="card-body p-4">
            <p class="small text-muted font-italic">ID: ${user.id} </p>
            <h5>${user.name.firstname} ${user.name.lastname} </h5>
            <p>username: ${user.username} </p>
            <p>phone: ${user.phone} </p>
            <p>Email: ${user.email} </p>
            <p>City: ${user.address.city} </p>
            <p>Zip code: ${user.address.zipcode} </p>
            <p>Street: ${user.address.street} </p>
        </div>
    </div>
    `;
    parent.appendChild(div);
}

const handleSearch=()=>{
    const value = document.getElementById("search").value;
    loadUser(value);
}
loadUser();