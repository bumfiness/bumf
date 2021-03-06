const auth = {
  authToken: localStorage.getItem('authToken'),
  authUser: localStorage.getItem('authUser'),
  authenticated: localStorage.getItem('authToken') !== null,

  authenticate (token, user) {
    localStorage.setItem('authToken', token)
    localStorage.setItem('authUser', user)

    auth.authToken = token
    auth.authUser = user

    auth.authenticated = true
  },

  logout () {
    localStorage.removeItem('authToken')
    localStorage.removeItem('authUser')

    auth.authToken = null
    auth.authUser = null

    auth.authenticated = false
  }

}

export default auth
