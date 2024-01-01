const loadProducts = (cat) => {
    document.getElementById("products").innerHTML = "";
    console.log(cat);
    fetch(`https://fakestoreapi.com/products/?category=${cat ? cat : ""}`)
        .then(res => res.json())
        .then((data) => {
            if (data?.length > 0) {
                document.getElementById("nodata").style.display = "none";
                document.getElementById("spinner").style.display = "none";
                displayProducts(data);
            } else {
                document.getElementById("nodata").style.display = "block";
                document.getElementById("spinner").style.display = "none";
            }
        })
        .catch((err) => console.log(err));
};


const displayProducts = (products) => {
    const parent = document.getElementById("products");
    parent.innerHTML = ""; 

    products.forEach(product => {
        const div = document.createElement("div");
        div.classList.add("col-xl-3", "col-lg-4", "col-md-6", "col-sm-6");
        div.classList.add("card-container");
        div.innerHTML = `
            <div class="card  text-center" style="width: 18rem;">
                <img class="img-card" src="${product?.image}" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${product?.title}</h5>
                    <h5>Price: ${product?.price}</h5>
                    <p class="card-text">Category: ${product?.category}</p>
                    <p class="card-text">Rating: ${product?.rating?.rate}</p>
                    <a href="#" class="btn btn-primary">Details</a>
                </div>
            </div>
        `;
        parent.appendChild(div);
    });
};

const loadCategories = () => {
    fetch('https://fakestoreapi.com/products/categories')
        .then(res => res.json())
        .then(json => displayCategories(json));
};

const displayCategories = (categories) => {
    const parent = document.getElementById("category");
    categories.forEach(category => {
        const buttonElement = document.createElement('button');
        buttonElement.classList.add('btn', 'btn-primary', 'm-3');
        buttonElement.innerHTML = `
            <li onclick="loadProducts('${category}')">${category}</li>
        `;
        parent.appendChild(buttonElement);
    });
};

loadProducts();
loadCategories();
