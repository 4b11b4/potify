import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    song: ''
  },
  mutations: {
    change(state, song) {
      state.song = song
    }
  },
  getters: {
    song: state => state.song
  }
})

