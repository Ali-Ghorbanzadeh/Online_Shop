function showProfile() {
    document.querySelector('main').innerHTML = `<section id="profile-section" class="flex flex-col p-5 mt-[10vh] rounded-2xl items-center w-[50%] mx-auto content-center bg-blue-200 h-full hidden"><section>`
    fetch(`/profile/`, {
        method: 'GET'
    }).then(res => res.json())
        .then(data => {
            document.querySelector('#profile-section').innerHTML = `
            <form id="update-profile" class="flex flex-col h-full justify-center gap-4">
                <label for="username" class="flex gap-10 items-center">
                    <p class="text-black">Username</p><input disabled name="username" type="text" placeholder="Username" value="${data.username}" class="input input-bordered input-secondary w-full max-w-xs"/>
                </label>
                <label for="first_name" class="flex gap-10 items-center">
                    <p class="text-black">Firstname</p><input name="first_name" type="text" placeholder="First-name" value="${data.first_name}" class="input input-bordered input-secondary w-full max-w-xs"/>
                </label>
                <label for="last_name" class="flex gap-10 items-center">
                    <p class="text-black">Lastname</p><input name="last_name" type="text" placeholder="Last-name" value="${data.last_name}" class="input input-bordered input-secondary w-full max-w-xs"/>
                </label>
                <button onclick="updateProfile()" type="submit" class="btn btn-active btn-primary my-4 mx-auto">Update Profile</button>
            </form>`
        })
    clear(document.querySelector('#profile-section'))
}

function updateProfile() {
    const data = new FormData(document.querySelector('#update-profile'))
    fetch(`/profile/`, {
        method: 'PUT',
        headers: {
            'X-CSRFToken': document.querySelector(`input[name="csrfmiddlewaretoken"]`).value,
        },
        body: data
    }).then(res => {
        if (res.status === 202) {
            alert('Profile successfully updated')
        }
    }).catch(() => {alert('Unknown Error')})
}