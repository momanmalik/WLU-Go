export default function authHeader() {

    const token = JSON.parse(localStorage.getItem('user')).access;
    console.log(localStorage.getItem('user'))
    if (user && user.accessToken) {
      return { Authorization: 'Bearer ' + {token}};
    } else {
      return {};
    }
  }