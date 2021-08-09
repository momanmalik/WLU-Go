import axios from "axios";

const API_URL = "http://localhost:8000/api/";

class AuthService {
  login(username, password) {
    return axios
      .post(API_URL + "token/", {
        username,
        password
      })
      .then(response => {
        if (response.data.access) {
          localStorage.setItem("user", JSON.stringify(response.data));
          localStorage.setItem("username", username);
        }

        return response.data;
      });
  }

  //logout() {
    //localStorage.removeItem("user");
//  }

  register(username, email, password1, password2) {
    return axios.post(API_URL + "rest-auth/registration/", {
      username,
      email,
      password1,
      password2,
    });
  }

  getCurrentUser() {
    return JSON.parse(localStorage.getItem('user'));;
  }
}

export default new AuthService();