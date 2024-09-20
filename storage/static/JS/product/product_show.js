const productEl = document.querySelector('#products-btn')
const productListEl = document.querySelector('#products-list')
function productShow(pk) {
    fetch(`/product/${pk}`, {
        method: 'GET'
    }).then(res => res.json())
        .then(data => {
            const tempEl = document.querySelector('#product-show')
            const imgEl = document.querySelector(`#img-${pk}`)

            tempEl.innerHTML = ''
            document.querySelector('#product-show').innerHTML += `
                                        <img src="${imgEl.src}" alt="${imgEl.alt}" class="h-full w-[35vh] rounded-lg ">
                                        <div class="w-[80vh]">
                                            <p class="font-bold">${data.name}</p>
                                            <hr>
                                            <div class="mt-5 h-[50%]">
                                                <p class="opacity-[50%]">Discription:</p>
                                                <p class="">${data.description}</p>
                                            </div>
                                            <p>Price: ${data.price}</p>
                                        </div>
                                        <div id="order-section">
                                            <img src="/media/product/images/cart.png" alt="noimage" class="rounded-md">
                                        </div>`
            if (data.quantity !== 0) {
                document.querySelector('#order-section').innerHTML += `
                                            <form class="flex flex-reverse justify-between gap-2 mt-3">
                                                <label for="quantity">
                                                    <input type="number" value="1" min="1" max="${data.quantity}" placeholder="Quantity" name="quantity" class="text-black p-2 h-full w-max bg-green-100 rounded-lg">
                                                </label>
                                                <button onclick="addItem(${pk}, ${data.price})" id="add-items" type="button" class="btn btn-success w-min text-[40px]">+</button>
                                            </form>`
            } else {document.querySelector('#order-section').innerHTML += `
            <p class="text-red-500 mx-auto">non-existent</p>`}

            tempEl.classList.remove('hidden')
        })
}

productEl.addEventListener('click', (e) => {
    e.preventDefault()
    fetch(`/product/`, {
        method: 'GET',
    }).then(res => res.json())
        .then(products => {
            productListEl.innerHTML = ''
            products.forEach( product => {
                if (product.images[0]) {
                    productListEl.innerHTML += `
                                                <button onclick="productShow(${product.id})" type="button" class="border-[3px] border-green-500 rounded-lg text-white">
                                                    <img id="img-${product.id}" src="${product.images[0].image}" alt="${product.images[0].alt}" class='size-full rounded-md'>
                                                    <p class="my-2">${product.name}</p>
                                                    <p>${product.price}</p>
                                                </button>`
                } else (
                    productListEl.innerHTML += `
                                                <button onclick="productShow(${product.id})" type="button" class="border-[3px] border-green-500 rounded-lg text-white">
                                                    <img id="img-${product.id}" src="/media/product/images/noimage.png" alt="noimage" class='size-full rounded-md'>
                                                    <p class="my-2">${product.name}</p>
                                                    <p>${product.price}</p>
                                                </button>`
                )
            })
        })
    clear(document.querySelector('#products-show'))
})