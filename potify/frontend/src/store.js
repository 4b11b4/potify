import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    song: Object
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
      state.song = song;
    }
  },
  getters: {
    song: state => state.song,
  }
})

