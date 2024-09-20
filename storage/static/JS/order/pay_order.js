function payOrder(pk) {
    fetch(`/api/order/${pk}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector(`input[name="csrfmiddlewaretoken"]`).value,
            'Authorization': 'Bearer '
        },
        body: JSON.stringify({
            'status': false,
        })
    }).then(res => {
        if (res.status === 202) {
            alert('Payment has been made successfully')
            orderHistory()
        }
    }).catch(() => {alert('Unknown Error')})
}