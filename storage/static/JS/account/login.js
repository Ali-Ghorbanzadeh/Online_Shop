function loginFrom() {
    document.querySelector('main').classList.add('blur-lg', 'z-0')
    // document.querySelector('#profile').innerHTML = document.querySelector('#login-html').innerHTML
    document.querySelector('#login-page').classList.remove('hidden')
    document.querySelector('#login-form').addEventListener('submit', (e) => {
        e.preventDefault()
        const data = new FormData(e.target)
        fetch(`/login/`, {
            method: 'POST',
            body: data
        }).then(res => {
            if (res.status === 202) {
                alert('Welcome')
                window.location.reload()
            } else {alert('Incorrect Username or Password !!!')}
        })
    })
}
