import Vue from 'vue'
import VueRouter from 'vue-router'

import store from './store'

// no_auth
import Home from './components/no_auth_needed/home.vue'
import rules from './components/no_auth_needed/rules.vue'
import program from './components/no_auth_needed/program.vue'
import about from './components/no_auth_needed/about.vue'
// import SignupPage from './components/auth/signup.vue'
import SignupPage from './components/auth/signup.vue'
import SigninPage from './components/auth/signin.vue'
import magic_link_handler from './components/auth/magic_link_handler.vue'


// learning
import lesson from './components/learning/lesson.vue'
import lessons from './components/learning/lessons.vue'
// user
import user from './components/user/user.vue'
import userProfile from './components/user/profile.vue'
import userProfileEdit from './components/user/profile_edit.vue'
import userSeat from './components/user/seat.vue'


// mentor
import mentor from './components/mentor/mentor.vue'

// organisator
import organiser from './components/organiser/organiser.vue'
import lessonsMngt from './components/organiser/lessons_mngt.vue'
// admin
import admin_config from './components/admin/config.vue'
import admin_email from './components/admin/email.vue'
import admin_users from './components/admin/users.vue'
import admin from './components/admin/admin.vue'

Vue.use(VueRouter);

const routes = [
    {path: '/', component: Home},
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
    {path: '/magic_link', component: magic_link_handler},
    {path: '/regconfirm/:code', component: magic_link_handler},
    {path: '/program', component: program},
    {path: '/about', component: about},
    {
        path: '/lessons',
        component: lessons,
        beforeEnter(to, from, next) {
            if (store.getters.isAuthenticated) {
                next()
            } else {
                next('/signin')
            }
        }
    },
    {
        path: '/lessons/:id',
        component: lesson,
        beforeEnter(to, from, next) {
            if (store.getters.isAuthenticated) {
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
    },
    {
        path: '/organiser',
        component: organiser,
        beforeEnter(to, from, next) {
            if (store.getters.isOrganiser) {
                next()
            } else {
                next('/')
            }
        },
        children: [
            {path: 'lessons', component: lessonsMngt},
        ]
    },
    {
        path: '/mentor',
        component: mentor,
        beforeEnter(to, from, next) {
            if (store.getters.isMentor) {
                next()
            } else {
                next('/')
            }
        },
        children: [
        ]
    },
    {
        path: '/user',
        component: user,
        beforeEnter(to, from, next) {
            if (store.getters.isAuthenticated) {
                next()
            } else {
                next('/')
            }
        },
        children: [
            {path: 'profile', component: userProfile},
            {path: 'edit', component: userProfileEdit},
            {path: 'seat', component: userSeat},
        ]
    }
];

export default new VueRouter({routes})