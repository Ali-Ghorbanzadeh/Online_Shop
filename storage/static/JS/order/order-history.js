function orderHistory () {
    fetch(`/api/order/`, {
        method: 'GET'
    }).then(res => res.json())
        .then(data => {
            document.querySelector('main').innerHTML = `<section id="order-list" class="grid p-5 w-[80vh] rounded-2xl bg-blue-300 m-8 gap-3 mx-auto h-full hidden"></section>`
            data.forEach(order => {
                let totalPrice = 0
                order.items.forEach(item => {
                    totalPrice += parseFloat(item.total_price)
                })
                document.querySelector('#order-list').innerHTML += `<div id="order-${order.id}" class="flex justify-between items-center"></div>`
                document.querySelector('#order-' + order.id).innerHTML += `
                        <div class="grid gap-2">
                            <div class="text-black">Order ID: ${order.id}</div>
                            <div class="text-black">Total Price: $${totalPrice}</div>
                        </div>`

                if (order.expired) {
                    document.querySelector('#order-' + order.id).innerHTML += `
                        <i class="fa-solid fa-ban text-red-700 text-[5vh] p-2"></i>`
                } else if (order.status) {
                    document.querySelector('#order-' + order.id).innerHTML += `
                        <button onclick="payOrder(${order.id})" class="text-yellow-100 hover:bg-yellow-50 hover:bg-opacity-[50%] p-2 rounded-lg" ><i class="fa-regular fa-money-bill-1 text-[5vh]"></i></button>`
                } else {
                    document.querySelector('#order-' + order.id).innerHTML += `
                        <i class="fa-solid fa-check text-green-700 text-[5vh] p-2"></i>`
                }
            })
            clear(document.querySelector('#order-list'))
        })
    }