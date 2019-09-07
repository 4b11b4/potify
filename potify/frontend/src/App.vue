<template>
  <div id="app">

    <div id="content">
      <Navigation></Navigation>
      <router-view/>
    </div>

    <div id="player">
      <player-component></player-component>
    </div>

  </div>
</template>

<script>
import Navigation from './components/Navigation.vue'
import PlayerComponent from './components/PlayerComponent.vue'

export default {
  name: 'app',
  components: {
    Navigation,
    PlayerComponent
  },
  data: function() {
    return {
      songs_from_api: [], //this
    }
  },

  methods: {
    async fetchSongs() {
      const response = await this.$http.get('/api/songs/')
      this.songs_from_api = response.data.results
      /* eslint-disable no-console */
      console.log('Songs from API: ' + this.songs_from_api)
      /* eslint-enable no-console */
    }
  }

}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
/* content and player are for setting a fixed footer
   this footer would overlap everything, so I made the background black 
   use "flexbox" instead? */
#content {
  min-height: 100%;
  padding-bottom: 100px;
}
#player {
  height: 100px;
  position: fixed;
  bottom: 0;
  width: 100%;
  background-color: black;
}
</style>
