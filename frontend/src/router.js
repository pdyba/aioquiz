import Vue from 'vue'
import VueRouter from 'vue-router'

import store from './store'

import WelcomePage from './components/welcome/welcome.vue'
import DashboardPage from './components/no_auth_needed/home.vue'
import rules from './components/no_auth_needed/rules.vue'
import program from './components/no_auth_needed/program.vue'
import about from './components/no_auth_needed/about.vue'
import SignupPage from './components/auth/signup.vue'
import SigninPage from './components/auth/signin.vue'

import admin_config from './components/admin/config.vue'
import admin_email from './components/admin/email.vue'
import admin_users from './components/admin/users.vue'
import admin from './components/admin/admin.vue'

Vue.use(VueRouter);

const routes = [
    {path: '/', component: DashboardPage},
    {path: '/rules', component: rules},
    {
        path: '/signup',
        component: SignupPage,
        beforeEnter(to, from, next) {
            if (store.getters.isAuthenticated) {
                next('/')
            } else {
                next()
            }
        },
    },
    {
        path: '/signin',
        component: SigninPage,
        beforeEnter(to, from, next) {
            if (store.getters.isAuthenticated) {
                next('/')
            } else {
                next()
            }
        },
    },
    {path: '/program', component: program},
    {path: '/about', component: about},
    {
        path: '/lessons',
        component: WelcomePage,
        beforeEnter(to, from, next) {
            if (store.state.session_uuid) {
                next()
            } else {
                next('/signin')
            }
        }
    },
    {
        path: '/admin',
        component: admin,
        beforeEnter(to, from, next) {
            if (store.getters.isAdmin) {
                next()
            } else {
                next('/')
            }
        },
        children: [
            {path: 'config', component: admin_config},
            {path: 'email', component: admin_email},
            {path: 'users', component: admin_users}
        ]
    }
];

export default new VueRouter({routes})