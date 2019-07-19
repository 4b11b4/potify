<template>
  <div>
    <b-row>
      <b-col>{{ song.name }}</b-col>
      <b-col>{{ artists }}</b-col>
      <b-col>{{ albums }}</b-col>
    </b-row>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SongRow',
  props: {
    song: Object
  },
  data: function() {
    return {
      artists: [],
      albums: []
    }
  },
  mounted() { //created or mounted, which one?
    // eslint-disable-next-line
    console.log('Song' + this.song)

    // eslint-disable-next-line
    console.log('Song.Artists ' + this.song.artists)

    // eslint-disable-next-line
    console.log('type: ' + typeof this.song.artists)

    var artistPrim = this.song.artists.valueOf();
    // eslint-disable-next-line
    console.log('ArtistPrim:')
    // eslint-disable-next-line
    console.log(artistPrim)

    var artistIdx = artistPrim.indexOf("p");
    // eslint-disable-next-line
    console.log('ArtistIdx:')
    // eslint-disable-next-line
    console.log(artistIdx)

    var urlSlice = artistPrim.slice("0");
    // eslint-disable-next-line
    console.log('urlSlice')
    // eslint-disable-next-line
    console.log(urlSlice)

    axios.get(this.song.artists).then((response) => {
      this.artists = response.data.results
      // eslint-disable-next-line
      console.log('Artists:')
      // eslint-disable-next-line
      console.log(this.artists)
    })

    axios.get(this.song.albums).then((response) => {
      this.albums = response.data.results
      // eslint-disable-next-line
      console.log('Albums:')
      // eslint-disable-next-line
      console.log(this.albums)
    })
  }
}
</script>

<style>
</style>
