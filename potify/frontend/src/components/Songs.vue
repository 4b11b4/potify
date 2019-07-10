<template>
  <div>
    <h2>Songs</h2>

    <div
      v-for="(song, index) in song_list"
      :key="index">
      <div class="ghettoplayer">
        <p>{{ song.name }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Songs',
  data: function() {
    return {
      song_list: []
    }
  },
  created() {
      axios.get('api/songs').then((response) => {
      this.song_list = response.data.results
    })
  }
}
</script>

<style>
</style>
