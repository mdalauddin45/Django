const loadProducts = (cat) => {
    document.getElementById("products").innerHTML = "";
    document.getElementById("spinner").style.display = "block";
    let apiUrl = 'https://fakestoreapi.com/products';
    if (cat) {
        const encodedCat = encodeURIComponent(cat);
        apiUrl += `/category/${encodedCat}`;
    }

    fetch(apiUrl)
        .then(res => res.json())
        .then((data) => {
            document.getElementById("spinner").style.display = "none";
            if (data?.length > 0) {
                document.getElementById("nodata").style.display = "none";
                displayProducts(data);
            } else {
                document.getElementById("nodata").style.display = "block";
            }
        })
        .catch((err) => console.log(err));
};


const displayProducts = (products) => {
    console.log(products)
    products.forEach(item => {
        const parent = document.getElementById("products");
        const div = document.createElement("div");
        div.classList.add("col-xl-3", "col-lg-4", "col-md-6", "col-sm-6");
        div.classList.add("card-container");
        div.innerHTML = `
            <div class="card mx-auto mt-4" style="max-width: 18rem;">
                <img class="card-img" src=${item.image} alt="">
                <div class="card-body">
                    <div class="space-y-2">
                        <h2 class="card-title text-3xl font-weight-bold">${item.title.slice(0,10)}</h2>
                        <p class="card-text">${item.price}</p>
                        <p>${item.category}</p>
                        <p>${item.rating?.rate}</p>
                    </div>
                    <a href="#" class="btn btn-primary btn-block font-weight-bold">Read more</a>
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
        buttonElement.textContent = category;
        buttonElement.addEventListener('click', () => {
            loadProducts(category);
        });
        parent.appendChild(buttonElement);
    });
};


loadProducts();
loadCategories();
