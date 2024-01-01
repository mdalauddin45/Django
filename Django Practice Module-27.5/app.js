const loadProducts=()=>{
    fetch('https://fakestoreapi.com/products')
    .then(res=>res.json())
    .then(json=>displayProducts(json))
}
const displayProducts=(products)=>{
    products.forEach(product=>{
        const parent = document.getElementById("products");
        console.log(product);
        const div = document.createElement("div");
        div.classList.add("col-xl-3", "col-lg-4", "col-md-6", "col-sm-6")
        div.classList.add("card-container")
        div.innerHTML=`
            <div class="card  text-center" style="width: 18rem;">
                <img class="img-card" src="${product?.image}" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${product?.title}</h5>
                    <h5 >Price: ${product?.price}</h5>
                    <p class="card-text">Category: ${product?.category}</p>
                    <p class="card-text">Ratting: ${product?.rating?.rate}</p>
                    <a href="#" class="btn btn-primary">Details</a>
                </div>
            </div>
        `;
        parent.appendChild(div);
    });
};
const loadCategories=()=>{
    fetch('https://fakestoreapi.com/products/categories')
    .then(res=>res.json())
    .then(json=>displayCategories(json))
}
const displayCategories=(categories)=>{
    categories.forEach(category=>{
        const parent = document.getElementById("category")
        const buttonElement = document.createElement('button');
        buttonElement.classList.add('btn', 'btn-primary','m-3');
        buttonElement.textContent = category;
        parent.appendChild(buttonElement);
    });
}

loadProducts();
loadCategories();