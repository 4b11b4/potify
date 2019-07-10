<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>Fetch Songs:</h1>

    <div
      v-for="(song, index) in songs_from_api"
      :key="index">
      <div class="ghettoplayer">
        <p>{{ song.name }}</p>
          <audio controls>
            <source :src='song.audio' type="audio/mp3">
            Your browser does not support the audio element.
          </audio>
      </div>
    </div>

    <button type="button" @click="fetchSongs">
      Fetch Songs
    </button>

    <test-component
      v-for="(song, index) in songs_from_api"
      v-bind:name="song.name"
      v-bind:key="index"
    ></test-component>

    <test-component name="testname"></test-component>

    <div
      v-for="item in groceryList"
      v-bind:name="item"
      v-bind:key="item.id"
    >
      {{ item.text }}
    </div>

    <player-component>
    </player-component>

  </div>
</template>

<script>
import TestComponent from './components/TestComponent.vue'
import PlayerComponent from './components/PlayerComponent.vue'


export default {
  name: 'app',
  components: {
    TestComponent,
    PlayerComponent
  },
  data: function() {
    return {
      songs_from_api: [],
      groceryList: [
        {id: 0, text: 'default_name'},
        {id: 1, text: 'test_name'}
      ]
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
