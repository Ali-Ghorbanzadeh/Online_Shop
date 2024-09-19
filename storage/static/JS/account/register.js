function registerFrom() {
    document.querySelector('#login-page').classList.add('hidden')
    document.querySelector('#register-page').classList.remove('hidden')
    document.querySelector('#register-form').addEventListener('submit', (e) => {
        e.preventDefault()
        const data = new FormData(e.target)
        fetch(`/register/`, {
            method: 'POST',
            body: data
        }).then(res => {
            if (res.status === 202) {
                alert('Registration was successful')
                window.location.reload()
            } else {alert('Wrong username or password !!!')}
        })
    })
}
