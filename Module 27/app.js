const loadServices = ()=>{
    fetch("https://testing-8az5.onrender.com/services/")
        .then((res)=>res.json())
        .then((data)=>displayService(data))
        .catch((err)=>console.log(err));
};
const displayService=(services)=>{

    services.forEach(service => {
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
const loadDoctors=(search)=>{
    document.getElementById("doctors").innerHTML="";
    document.getElementById("spinner").style.display="block";
    fetch(`https://testing-8az5.onrender.com/doctor/list/?search=${search?  search: " "}`)
        .then((res)=>res.json())
        .then((data)=>{
            if (data?.results.length>0){
                document.getElementById("nodata").style.display="none";
                document.getElementById("spinner").style.display="none";
                displayDoctors(data?.results)
            }else{
                document.getElementById("doctors").innerHTML="";
                document.getElementById("nodata").style.display="block";
                document.getElementById("spinner").style.display="none";
            }
        })
        .catch((err)=>console.log(err));
};
const displayDoctors=(doctors)=>{
    doctors?.forEach((doctor)=>{
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
         <button><a target="_blank" href="docDetails.html?doctorId=${doctor.id}">Details</a></button>
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
    designations.forEach((designation)=>{
        const parent= document.getElementById("designation");
        const li = document.createElement("li");
        li.classList.add("dropdown-item");
        // li.innerText = designation.name;
        li.innerHTML=`
        <li onclick="loadDoctors('${designation.name}')">${designation.name}</li>
        `;
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
    specializations.forEach((specialization)=>{
        const parent= document.getElementById("Specialization");
        const li = document.createElement("li");
        li.classList.add("dropdown-item");
        // li.innerText = specialization.name;
        li.innerHTML=`
        <li onclick="loadDoctors('${specialization.name}')">${specialization.name}</li>
        `;
        parent.appendChild(li);

    });
};
const handleSearch=()=>{
    const value = document.getElementById("search").value;
    loadDoctors(value)
}
const loadReview=()=>{
    fetch("https://testing-8az5.onrender.com/doctor/review/")
    .then((res)=>res.json())
    .then((data)=>displayReview(data))
    .catch((err)=>console.log(err));
}
const displayReview=(reviews)=>{
    reviews.forEach((review)=>{
        const parent = document.getElementById("all-review");
        const div = document.createElement("div");
        div.classList.add("review-card");
        div.classList.add("slide-visible");
        div.innerHTML = `
            <img src="./Images/girl.png" alt="" />
            <h4>${review.reviewer}</h4>
            <p>
             ${review.body.slice(0, 100)}
            </p>
            <h6>${review.rating}</h6>
        `;
        parent.appendChild(div);
    });
};

loadServices();
loadDoctors();
loadDesignation();
loadSpecialization();
loadReview();