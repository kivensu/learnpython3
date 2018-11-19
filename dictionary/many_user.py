users_infos = {
    'lisa': {
        'first_name': 'lisa',
        'last_name': 'wang',
        'location': 'beijing',
    },
    'tom': {
        'first_name': 'tom',
        'last_name': 'li',
        'location': 'tokyo',
    },
    'kiven': {
        'first_name': 'kiven',
        'last_name': 'su',
        'location': 'newyork'
    }
}
for username, userinfo in users_infos.items():
    print("\nUsername: " + username)
    full_name = userinfo['first_name'].title() + " " + \
        userinfo['last_name'].title()
    location = userinfo['location']
    print("\tFull name: " + full_name)
    print("\tLocation: " + location.title())
