<template>
  <div>
    <h2>Artists</h2>
    <b-container fluid>

      <b-row>
        <b-col>Artist</b-col>
        <b-col>Image</b-col>
      </b-row>

      <div
        v-for="(artist, index) in artist_list"
        :key="index">
          <artist-row v-bind:artist="artist"></artist-row>
      </div>

    </b-container>
  </div>
</template>

<script>
import axios from 'axios'
import ArtistRow from './ArtistRow.vue'

export default {
  name: 'Artists',
  data: function() {
    return {
      artist_list: []
    }
  },
  components: {
    ArtistRow 
  },
  mounted() {
    axios.get('api/artists').then((response) => {
      this.artist_list = response.data.results
      /* eslint-disable */
      console.log('Artist List:')
      console.log(this.artist_list)
      /* eslint-enable */
    })
  }
}
</script>

<style>
</style>
