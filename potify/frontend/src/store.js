import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    song: ''
  },
  actions: {
    setActiveSong(context, song) {
      context.commit('changeSong', song);
      // eslint-disable-next-line
      console.log(song)
    }
  },
  mutations: {
    changeSong(state, song) {
      state.song = song
    }
  },
  getters: {
    song: state => state.song
  }
})

