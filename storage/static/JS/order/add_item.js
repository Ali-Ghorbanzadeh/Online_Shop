function addItem(pk, price) {
    fetch(`/api/order-item/${pk}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector(`input[name="csrfmiddlewaretoken"]`).value,
            'Authorization': 'Bearer '
        },
        body: JSON.stringify({
            'price': price,
            'quantity': document.querySelector('input[name="quantity"]').value,
        })
    }).then(async res =>
        {
            await res.json()
            if (res.status === 201) {
                alert('Successfully added to cart')
                productShow(pk)
            }
        }).catch(() => alert('Unknown Error'))

    }