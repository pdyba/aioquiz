import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import swal from 'sweetalert2'
import BootstrapVue from 'bootstrap-vue'
import Vuelidate from 'vuelidate'
import VueMarkdown from 'vue-markdown'
import VueSweetalert2 from 'vue-sweetalert2';
import VueI18n from 'vue-i18n';

import 'bootstrap/dist/css/bootstrap.css'
import 'mdbootstrap/css/mdb.css';
import 'prismjs/themes/prism.css'

import router from './router'
import store from './store'

axios.defaults.baseURL = '/api';
axios.defaults.headers.accepts = 'application/json';

axios.interceptors.response.use(res => {
    return res
}, (error) => {
    if (error.response.status === 401) {
        store.dispatch('logout')
    }
    else {
        swal("Error", error.response.data.msg, "error");
    }
    return error
});

axios.interceptors.request.use(req => {
    req.headers.authorization = store.getters.sessionUUID;
    return req
});

const moment = require('moment');
require('moment/locale/pl');

Vue.use(BootstrapVue);
Vue.use(Vuelidate);
Vue.use(VueMarkdown);
Vue.use(VueSweetalert2);
Vue.use(require('vue-moment'), {
    moment
});
Vue.use(VueI18n);

const i18n = new VueI18n({
    locale: 'pl',
    messages: {
        en: {},
        pl: {}
    }
});

new Vue({
    el: '#app',
    router,
    store,
    i18n,
    render: h => h(App)
});
