<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>Fetch Songs:</h1>
    <p
      v-for="(song, index) in songs_from_api"
      :key="index"
    >
      {{ song }}
    </p>
    <button type="button" @click="fetchSongs">
      Fetch Songs
    </button>
  </div>
</template>

<script>
export default {
  name: 'app',

  data: function() {
    return {
      songs_from_api: [],
    }
  },

  methods: {
    async fetchSongs() {
      const response = await this.$http.get('/api/songs/')
      this.songs_from_api = response.data
      /* eslint-disable no-console */
      console.log('songs from api: ' + this.songs_from_api)
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
