<template>
  <div>
    <h2>Songs</h2>
    <b-container fluid>
      <b-row>
        <b-col>Plays</b-col>
        <b-col>Title</b-col>
        <b-col>Artist</b-col>
        <b-col>Album</b-col>
      </b-row>
      <div
        v-for="(song, index) in song_list"
        @click="setActiveSong({song: song.audio, title: song.name, artist: song.artist})"
        :key="index">
          <song-row v-bind:song="song"></song-row>
      </div>
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
import SongRow from './SongRow.vue'

export default {
  name: 'Songs',
  data: function() {
    return {
      song_list: [],
      artist_list: [],
    }
  },
  components: {
    SongRow
  },
  methods: {
    ...mapActions( [
      'setActiveSong'
      // map setActiveSong(song) to this.$store.dispatch('setActiveSong', song, title)
    ] )
  },
  /* Should created() or mounted() be used here? */
  mounted() {
    axios.get('api/songs').then((response) => {
      this.song_list = response.data.results
      /* eslint-disable */
      console.log('Song_List:')
      console.log(this.song_list)
      /* eslint-enable */
    })
  }
}
</script>

<style>
</style>
