<template>
  <div>
    <b-row>
      <b-col>{{ song.play_count }}</b-col>
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
    /* SongRow gets passed a Song object from Songs.vue. It then
       has to query the API again for the artist and album. This method
       results in a crap ton of queries??! 
       Maybe we want to re-structure the Django models */
    
    /* Consider re-implementing as a table so the song list can be sorted? */

    /* This method only grabs the FIRST artist and album, not all of them */

    /* Get the URL to query for the artist */
    var artistPrim = this.song.artists[0].valueOf();
    var sliceIdx = artistPrim.indexOf("api"); // assume idx is same for both
    var artistUrl = artistPrim.slice(sliceIdx, artistPrim.length);
    axios.get(artistUrl)
      .then((response) => {
        this.artists = response.data
      })

    /* Now get the URL for the album. */
    /* Including some really bad error catching to prevent
       the album name from being "Object" if it is not defined */
    try {
      var albumPrim = this.song.albums[0].valueOf();
      var albumUrl = albumPrim.slice(sliceIdx, albumPrim.length);
      axios.get(albumUrl).then((response) => {
        this.albums = response.data
      })
    } catch (e) {
      this.albums = {
        name: 'n/a'
      }
    }
  }
}
</script>

<style>
</style>
