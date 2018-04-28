import axios from 'axios'

const alt_axios = axios.create();
alt_axios.defaults.baseURL = '';

export default alt_axios