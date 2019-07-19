<template>
  <div>
    <b-row>
      <b-col>{{ song.name }}</b-col>
      <b-col>{{ artists.name }}</b-col>
      <b-col>{{ albums.name }}</b-col>
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
      artists: Object,
      albums: Object 
    }
  },
  mounted() { //created or mounted, which one?
    // eslint-disable-next-line
    console.log('Song')
    // eslint-disable-next-line
    console.log(this.song)

    // eslint-disable-next-line
    console.log('Song.Artists:')
    // eslint-disable-next-line
    console.log(this.song.artists)

    // eslint-disable-next-line
    console.log('type:')
    // eslint-disable-next-line
    console.log(typeof this.song.artists)

    var artistPrim = this.song.artists[0].valueOf();
    // eslint-disable-next-line
    console.log('ArtistPrim:')
    // eslint-disable-next-line
    console.log(artistPrim)

    var artistIdx = artistPrim.indexOf("api");
    // eslint-disable-next-line
    console.log('ArtistIdx:')
    // eslint-disable-next-line
    console.log(artistIdx)

    var urlSlice = artistPrim.slice(artistIdx, artistPrim.length);
    // eslint-disable-next-line
    console.log('urlSlice:')
    // eslint-disable-next-line
    console.log(urlSlice)

    // eslint-disable-next-line
    console.log('Trying to query artists:')
    axios.get(urlSlice)
      .then((response) => {
        this.artists = response.data
        // eslint-disable-next-line
        console.log('Artists from axios:')
        // eslint-disable-next-line
        console.log(this.artists)
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.log('error:')
        // eslint-disable-next-line
        console.log(error)
        // eslint-disable-next-line
        console.log(error.config)
      })
    // eslint-disable-next-line
    console.log('After artists query.')
    
    /* Some really bad error catching to prevent
       the album from being "Object" if it is not defined */
    try {
      var albumPrim = this.song.albums[0].valueOf();
    } catch (e) {
      this.albums = {
        name: 'n/a'
      }
    }
    // eslint-disable-next-line
    console.log('AlbumPrim:')
    // eslint-disable-next-line
    console.log(albumPrim)

    var albumIdx = albumPrim.indexOf("api");
    // eslint-disable-next-line
    console.log('AlbumIdx:')
    // eslint-disable-next-line
    console.log(albumIdx)

    var albumURLSlice = albumPrim.slice(albumIdx, albumPrim.length);
    // eslint-disable-next-line
    console.log('albumURLSlice:')
    // eslint-disable-next-line
    console.log(albumURLSlice)
    
    axios.get(albumURLSlice).then((response) => {
      this.albums = response.data
      // eslint-disable-next-line
      console.log('Albums from axios:')
      // eslint-disable-next-line
      console.log(this.albums)
    })
  }
}
</script>

<style>
</style>
