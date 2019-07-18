<template>
  <div>
    <h2>Songs</h2>
    <b-container fluid>
      <b-row>
        <b-col>Title</b-col>
        <b-col>Artist</b-col>
        <b-col>Album</b-col>
      </b-row>
      <b-row
        v-for="(song, index) in song_list"
        @click="setActiveSong(song.audio)"
        :key="index">
          <b-col>{{ song.name }}</b-col>
          <b-col>
            <div
              v-for="(artist, index) in artist_list"
              :key="index">
              <p>{{ artist }}</p>
            </div>
          </b-col>
          <b-col>{{ song.albums }}</b-col>
      </b-row>
    </b-container>
    <!--
    <div
      v-for="(song, index) in song_list"
      @click="setActiveSong(song.audio)"
      :key="index">
      <p>{{ song.name }}</p>
    </div>
    -->
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'

export default {
  name: 'Songs',
  data: function() {
    return {
      song_list: [],
      artist_list: []
    }
  },
  methods: {
    ...mapActions( [
      'setActiveSong'
      // map setActiveSong(song) to this.$store.dispatch('setActiveSong', song)
    ] ),
    getArtists: function(artistURL) {
      axios.get(artistURL).then((response) => {
        this.artists_list = response.data.results 
      })
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
