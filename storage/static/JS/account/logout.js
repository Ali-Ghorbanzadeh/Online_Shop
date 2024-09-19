function logout() {
    fetch(`/logout/`, {
        method: 'GET',
        credentials: 'include'
    }).then(res => {
        if (res.ok) {
            window.location.reload()
        }
    })
}
