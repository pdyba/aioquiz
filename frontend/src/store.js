import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

import router from './router'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        session_uuid: null,
        language: 'pl',
        user: null
    },
    plugins: [createPersistedState()],
    mutations: {
        authUser(state, session_uuid) {
            state.session_uuid = session_uuid;
        },
        storeUser(state, user) {
            state.user = user;
        },
        clearAuthData(state) {
            state.session_uuid = null;
            state.user = null;
        }
    },
    actions: {
        signup({commit, dispatch}, data) {
            axios.post('/users', data)
                .then(res => {
                    commit('authUser', {
                        session_uuid: res.data.session_uuid,
                    });
                    const now = new Date()
                    const expirationDate = new Date(now.getTime() + res.data.expiresIn * 1000)
                    localStorage.setItem('session_uuid', res.data.session_uuid)
                    localStorage.setItem('expirationDate', expirationDate)
                    dispatch('storeUser', authData)
                })
                .catch(error => console.log(error))
        },
        login({commit, dispatch}, authData) {
            axios.post('/auth/login', {
                email: authData.email,
                password: authData.password,
            }).then((response) => {
                    dispatch('loginUser', response.data)
                });
        },
        loginUser({commit, dispatch}, authData) {
            const now = new Date();
            const expirationDate = new Date(now.getTime() + 10000000 * 1000);
            localStorage.setItem('session_uuid', authData.session_uuid);
            localStorage.setItem('expirationDate', expirationDate);
            localStorage.setItem('user',  JSON.stringify(authData));
            commit('storeUser', authData);
            commit('authUser', authData.session_uuid);
            router.replace('/lessons');
        },
        tryAutoLogin({commit}) {
            const session_uuid = localStorage.getItem('session_uuid');
            if (!session_uuid) {
                return
            }
            const expirationDate = localStorage.getItem('expirationDate');
            const user = JSON.parse(localStorage.getItem('user'));
            const now = new Date()
            if (now >= expirationDate) {
                return
            }
            commit('authUser', session_uuid);
            commit('storeUser', user);
            router.replace('/lessons');
        },
        logout({commit}) {
            axios.get('/auth/logout').then((resp) => {
                commit('clearAuthData');
                localStorage.removeItem('expirationDate');
                localStorage.removeItem('session_uuid');
                localStorage.removeItem('user');
                router.replace('/signin');
            })
        },
        storeUser({commit, state}, userData) {
            if (!state.session_uuid) {
                return
            }
            axios.post('/users', userData)
                .then(res => console.log(res))
                .catch(error => console.log(error))
        },
        fetchUser({commit, state}) {
            if (!state.session_uuid) {
                return
            }
            axios.get('/users')
                .then(res => {
                    console.log(res);
                    const data = res.data;
                    const users = [];
                    for (let key in data) {
                        const user = data[key];
                        user.id = key;
                        users.push(user)
                    }
                    console.log(users);
                    commit('storeUser', users[0]);
                })
                .catch(error => console.log(error))
        }
    },
    getters: {
        user(state) {
            return state.user
        },
        isAuthenticated(state) {
            return state.session_uuid !== null
        },
        isSeated(state) {
            return state.user.seat !== null
        },
        sessionUUID(state) {
            return state.session_uuid
        },
        isAdmin(state) {
            if (state.user) {
                return state.user.admin
            }
            return false
        },
        isOrganiser(state) {
            if (state.user) {
                return state.user.organiser
            }
            return false
        },
        isMentor(state) {
            if (state.user) {
                return state.user.mentor
            }
            return false
        },
        userName(state) {
            if (state.user) {
                return state.user.name + ' ' + state.user.surname
            }
            return ''
        }
    }
})