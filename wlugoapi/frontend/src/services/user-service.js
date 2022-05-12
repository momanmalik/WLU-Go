import axios from 'axios';


const API_URL = 'http://localhost:8000/api/';

class UserService {
  getPublicContent() {
    return axios.get(API_URL);
  }

  getUser() {
    return axios.get(API_URL + 'users/', { headers: { Authorization: 'Bearer ' + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI5NjE1NTc0LCJqdGkiOiJiNmE2NGFkZmYxMWE0YThmYTQzMjk2MjhmYjY4MzA5NCIsInVzZXJfaWQiOjF9.GsEuZhK8sSzTZmj3T3DpIt5tc11vLyIyPOWr7HAex0g"} });
  }

  getCourses() {
    return axios.get(API_URL + 'courses/', { headers:  { Authorization: 'Bearer ' + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI5NjE1NTc0LCJqdGkiOiJiNmE2NGFkZmYxMWE0YThmYTQzMjk2MjhmYjY4MzA5NCIsInVzZXJfaWQiOjF9.GsEuZhK8sSzTZmj3T3DpIt5tc11vLyIyPOWr7HAex0g"} });
  }

  getProfessor() {
    return axios.get(API_URL + 'professors/', { headers:  { Authorization: 'Bearer ' + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI5NjE1NTc0LCJqdGkiOiJiNmE2NGFkZmYxMWE0YThmYTQzMjk2MjhmYjY4MzA5NCIsInVzZXJfaWQiOjF9.GsEuZhK8sSzTZmj3T3DpIt5tc11vLyIyPOWr7HAex0g"} });
  }
}

export default new UserService();