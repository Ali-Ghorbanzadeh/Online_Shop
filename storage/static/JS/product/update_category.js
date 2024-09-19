document.addEventListener('DOMContentLoaded', function() {
    const categoryEl = document.querySelector('#category-list');

    function updateCategory() {
        fetch(`/product/category/`, {
            method: 'GET'
        }).then(res => res.json())
            .then(data => {
                categoryEl.innerHTML = ``
                data.forEach(category => {
                    categoryEl.innerHTML += `<li class="!w-full"><a href="/product/category/${category.name}">${category.name}</a></li>`
                })
            })
            .catch(error => console.error('Error fetching categories:', error))
    }
    updateCategory();
})
