<template>
  <div id="app">
    <Navigation></Navigation>
    <router-view/>
    <player-component></player-component>
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
</style>
