<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>Fetch Songs:</h1>
    <div
     v-for="(song, index) in songs_from_api"
      :key="index">
      <div class="ghettoplayer">
        <p>{{ song.name }}</p>
            <audio ref="player" controls>
            {% verbatim %}
                <source :src='song'>
                Your browser does not support the audio element.
                {% endverbatim %}
            </audio>
        </div>
    </div>
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
      this.songs_from_api = response.data.results
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
