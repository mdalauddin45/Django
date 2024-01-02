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
        // div.classList.add("col-xl-3", "col-lg-4", "col-md-6", "col-12");
        div.classList.add("col-lg-3", "col-md-6", "mb-4", "mb-lg-0");
        div.classList.add("card-container");
        div.innerHTML = `
        <div class="card rounded shadow-sm border-0">
            <div class="card-body p-4"><img class="card-img" src=${item.image} alt="" class="img-fluid d-block mx-auto mb-3">
                <h5>${item.title.slice(0,20)}..</h5>
                <p class="small text-muted font-italic">Price: ${item.price}$</p>
                <p>Category: ${item.category}</p>
                <p>${item.rating?.rate}</p>
                <a target="_blank" href="cardDetails.html?cardId=${item.id}" class="button-37">Details</a>
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
        buttonElement.classList.add('button-37','m-3');
        buttonElement.textContent = category;
        buttonElement.addEventListener('click', () => {
            loadProducts(category);
        });
        parent.appendChild(buttonElement);
    });
};


loadProducts();
loadCategories();
