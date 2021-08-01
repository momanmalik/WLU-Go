import axios from 'axios'

const axiosInstance = axios.create({
    baseURL: 'https://wlugoapi.herokuapp.com/api/',
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }
});