const gerParams=()=>{
    const param = new URLSearchParams(window.location.search).get("cardId");
    console.log(param);
    fetch(`https://fakestoreapi.com/products/${param}`)
            .then(res=>res.json())
            .then(data=>displayParam(data))
};
const displayParam=(post)=>{
    console.log(post)
    const parent = document.getElementById("product-details")
    const div = document.createElement("div");
    div.innerHTML =`
    <div class="gray-bg container m-10">
            <div class="row align-items-center m-auto">
                <div class="col-lg-6 m-15">
                    <img class="detailscard-img" src=${post.image}  alt="">
                </div>
                <div class="col-lg-6 m-15">
                  <div class="card-body">
                    <div class="space-y-2">
                        <h2 class="card-title text-3xl font-weight-bold">${post.title}</h2>
                        <p class="card-text">${post.price}</p>
                        <p>${post.category}</p>
                        <p>${post.rating?.rate}</p>
                        <p>${post.description}</p>
                    </div>
                    <a target="_blank" href="cardDetails.html?cardId=${post.id}" class="button-37">Buy Now</a>
                </div>
            </div>
    </div>
    `;
    parent.appendChild(div);
};
gerParams();