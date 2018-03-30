import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueSwal from 'vue-swal'
import BootstrapVue from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'mdbootstrap/css/mdb.css';

import router from './router'
import store from './store'

axios.defaults.baseURL = 'http://127.0.0.1:5000/api';
axios.interceptors.response.use(res => {
    return res
}, (error) => {
    console.log(error);
    swal("Error", error.response.data.msg, "error");
    return error
});

Vue.use(BootstrapVue);
Vue.use(VueSwal);

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App)
});
