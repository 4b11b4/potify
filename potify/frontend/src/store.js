import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    audio: '',
    title: ''
  },
  actions: {
    setActiveSong(context, song) {
      context.commit('changeSong', song);
      /* eslint-disable */
      /*
      console.log("song changed to: (inside vuex store)")
      console.log(song.audio)
      console.log("title changed to: (inside vuex store)")
      console.log(song.title)
      */
      /* eslint-enable */
    }
  },
  mutations: {
    changeSong(state, song) {
      state.audio = song.audio;
      state.title = song.title;
    }
  },
  getters: {
    audio: state => state.audio,
    title: state => state.title
  }
})

