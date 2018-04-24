import axios from 'axios'

const instance = axios.create();
axios.defaults.baseURL = '';

export default instance