<template>
  <div>
    <h2>Songs</h2>

    <div
      v-for="(song, index) in song_list"
      :key="index">
      <p>{{ song.name }}</p>
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
  mounted() { //created or mounted, which one?
    axios.get('api/songs').then((response) => {
      this.song_list = response.data.results
      // eslint-disable-next-line
      console.log(this.song_list)
    })
  }
}
</script>

<style>
</style>
