function clear(element) {
    document.querySelectorAll('section').forEach(section => section.classList.add('hidden'))
    element.classList.remove('hidden')
}

function closeFrom(form_id) {
    document.querySelector('main').classList.remove('blur-lg', 'z-0')
    document.querySelector('#login-page').classList.add('hidden')
    document.querySelector('#register-page').classList.add('hidden')
}
