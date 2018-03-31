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

Vue.use(VueRouter);

const routes = [
  { path: '/', component: DashboardPage },
  { path: '/rules', component: rules },
  { path: '/signup', component: SignupPage },
  { path: '/signin', component: SigninPage },
  { path: '/program', component: program },
  { path: '/about', component: about },
  {
    path: '/lessons',
    component: WelcomePage,
    beforeEnter (to, from, next) {
      if (store.state.session_uuid) {
        next()
      } else {
        next('/signin')
      }
    }
  }
]

export default new VueRouter({routes})