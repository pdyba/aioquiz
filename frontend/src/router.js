import Vue from 'vue'
import VueRouter from 'vue-router'

import store from './store'

// no_auth
import Home from './components/no_auth/home.vue'
import rules from './components/no_auth/rules.vue'
import privacy_policy from './components/no_auth/privacy_policy.vue'
import program from './components/no_auth/program.vue'
import about from './components/no_auth/about.vue'
import SignupPage from './components/auth/signup.vue'
import SigninPage from './components/auth/signin.vue'
import magic_link_handler from './components/auth/magic_link_handler.vue'


// learning
import exam from './components/learning/exam.vue'
import exams from './components/learning/exams.vue'
import lesson from './components/learning/lesson.vue'
import lessons from './components/learning/lessons.vue'
import live_quiz from './components/learning/live_quiz.vue'
import live_quizzes from './components/learning/live_quizzes.vue'
import quiz from './components/learning/quiz.vue'
import quizzes from './components/learning/quizzes.vue'
// user
import user from './components/user/user.vue'
import userProfile from './components/user/profile.vue'
import userProfileEdit from './components/user/profile_edit.vue'
import userSeat from './components/user/seat.vue'


// mentor
import mentor from './components/mentor/mentor.vue'

import mentorQuizList from './components/mentor/quiz_list.vue'
import mentorQuizDetails from './components/mentor/quiz_details.vue'
import mentorQuizGrade from './components/mentor/quiz_grade.vue'

import mentorLiveQuizList from './components/mentor/live_quiz_list.vue'
import mentorLiveQuizDetails from './components/mentor/live_quiz_details.vue'

import mentorExamList from './components/mentor/exam_list.vue'
import mentorExamDetails from './components/mentor/exam_details.vue'
import mentorExamGrade from './components/mentor/exam_grade.vue'

import mentorUsers from './components/mentor/users.vue'

import mentorLessons from './components/mentor/lessons.vue'
import mentorLesson from './components/mentor/lesson.vue'

// organisator
import organiser from './components/organiser/organiser.vue'

import lessonsMngt from './components/organiser/lessons_mngt.vue'

import quizMngt from './components/organiser/quiz_mngt.vue'
import quizCreate from './components/organiser/quiz_create.vue'
import quizEdit from './components/organiser/quiz_edit.vue'

import liveQuizMngt from './components/organiser/live_quiz_mngt.vue'
import liveQuizCreate from './components/organiser/live_quiz_create.vue'
import liveQuizEdit from './components/organiser/live_quiz_edit.vue'

import examMngt from './components/organiser/exam_mngt.vue'
import examCreate from './components/organiser/exam_create.vue'
import examEdit from './components/organiser/exam_edit.vue'

// admin
import admin_config from './components/admin/config.vue'
import admin_email from './components/admin/email.vue'
import admin_users from './components/admin/users.vue'
import admin from './components/admin/admin.vue'

Vue.use(VueRouter);

const routes = [
    {path: '/', component: Home},
    {path: '/rules', component: rules},
    {path: '/privacy_policy', component: privacy_policy},
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
        path: '/exam',
        component: exams,
        beforeEnter(to, from, next) {
            if (store.getters.isAuthenticated) {
                next()
            } else {
                next('/signin')
            }
        }
    },
    {
        path: '/exam/:id',
        component: exam,
        beforeEnter(to, from, next) {
            if (store.getters.isAuthenticated) {
                next()
            } else {
                next('/signin')
            }
        }
    },
    {
        path: '/quiz',
        component: quizzes,
        beforeEnter(to, from, next) {
            if (store.getters.isAuthenticated) {
                next()
            } else {
                next('/signin')
            }
        }
    },
    {
        path: '/quiz/:id',
        component: quiz,
        beforeEnter(to, from, next) {
            if (store.getters.isAuthenticated) {
                next()
            } else {
                next('/signin')
            }
        }
    },
    {
        path: '/live_quiz',
        component: live_quizzes,
        beforeEnter(to, from, next) {
            if (store.getters.isAuthenticated) {
                next()
            } else {
                next('/signin')
            }
        }
    },
    {
        path: '/live_quiz/:id',
        component: live_quiz,
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

            {path: 'quiz-manage', component: quizMngt},
            {path: 'quiz-create', component: quizCreate},
            {path: 'quiz-edit/:id', component: quizEdit},

            {path: 'live-quiz-manage', component: liveQuizMngt},
            {path: 'live-quiz-create', component: liveQuizCreate},
            {path: 'live-quiz-edit/:id', component: liveQuizEdit},

            {path: 'exam-manage', component: examMngt},
            {path: 'exam-create', component: examCreate},
            {path: 'exam-edit/:id', component: examEdit},
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
            {path: 'exam', component: mentorExamList},
            {path: 'exam/:id', component: mentorExamDetails},
            {path: 'quiz', component: mentorQuizList},
            {path: 'quiz/:id', component: mentorQuizDetails},
            {path: 'live-quiz', component: mentorLiveQuizList},
            {path: 'live-quiz/:id', component: mentorLiveQuizDetails},
            {path: 'grade/exam/:id', component: mentorExamGrade},
            {path: 'grade/quiz/:id', component: mentorQuizGrade},
            {path: 'users', component: mentorUsers},
            {path: 'lessons', component: mentorLessons},
            {path: 'lessons/:id', component: mentorLesson},
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