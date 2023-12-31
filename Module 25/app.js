const loadServices = ()=>{
    fetch("https://testing-8az5.onrender.com/services/")
        .then((res)=>res.json())
        .then((data)=>displayService(data))
        .catch((err)=>console.log(err));
};
const displayService=(services)=>{

    services.forEach(service => {
        // console.log(service)
        const parent = document.getElementById("all-service");
        const li = document.createElement("li");
        li.classList.add("slide-visible");
        li.innerHTML=
        `
        <div class="card shadow h-100">
            <div class="ratio ratio-16x9">
                <img src=${service?.image} class="card-img-top" loading="lazy" alt="...">
            </div>
            <div class="card-body  p-3 p-xl-5">
                <h3 class="card-title h5">${service?.name}</h3>
                <p class="card-text">${service?.description.slice(0,100)}</p>
                <a href="#" class="btn btn-primary">Details</a>
            </div>
        </div>
        `;
        parent.appendChild(li)
    });
};
const loadDoctors=()=>{
    fetch("https://testing-8az5.onrender.com/doctor/list/")
        .then((res)=>res.json())
        .then((data)=>displayDoctors(data?.results))
        .catch((err)=>console.log(err));
};
const displayDoctors=(doctors)=>{
    doctors?.forEach((doctor)=>{
        // console.log(doctor);
        const parent = document.getElementById("doctors");
        const div = document.createElement("div");
        div.classList.add("doc-card");
        div.innerHTML=
        `
        <img class="doc-img" src=${doctor.image} alt="">
        <h4>${doctor.full_name}</h4>
        <h6>${doctor.designation[0]}</h6>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Vitae, cupiditate?</p>
        ${
            doctor?.specialization.map((s)=>`<button>${s}</button>`).join('')}
         <button>Details</button>
        `;
        parent.appendChild(div);
    });
};
const loadDesignation=()=>{
    fetch("https://testing-8az5.onrender.com/doctor/designation/")
        .then((res)=>res.json())
        .then((data)=>displayDesiginaton(data))
        .catch((err)=>console.log(err));
};
const displayDesiginaton=(designations)=>{
    // console.log(designations);
    designations.forEach((designation)=>{
        const parent= document.getElementById("designation");
        const li = document.createElement("li");
        li.classList.add("dropdown-item");
        li.innerText = designation.name;
        parent.appendChild(li);

    });
};
const loadSpecialization=()=>{
    fetch("https://testing-8az5.onrender.com/doctor/specialization/")
        .then((res)=>res.json())
        .then((data)=>displaySpecialization(data))
        .catch((err)=>console.log(err));
};
const displaySpecialization=(specializations)=>{
    console.log(specializations);
    specializations.forEach((specialization)=>{
        const parent= document.getElementById("Specialization");
        const li = document.createElement("li");
        li.classList.add("dropdown-item");
        li.innerText = specialization.name;
        parent.appendChild(li);

    });
};


loadServices();
loadDoctors();
loadDesignation();
loadSpecialization();