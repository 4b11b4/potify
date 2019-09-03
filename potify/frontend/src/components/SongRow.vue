<template>
  <div id="rowstyle">
    <b-row>
      <b-col>{{ song.play_count }}</b-col>
      <b-col>{{ song.title}}</b-col>
      <b-col>{{ artists.name }}</b-col>
      <b-col>{{ albums.name }}</b-col>
    </b-row>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SongRow',
  /* This data is passed from song_list in Songs.vue */
  props: {
    song: Object
  },
  /* This data is retrieved on the creationg of each SongRow component */
  data: function() {
    return {
      artists: Object,
      albums: Object,
      bgcolor: '',
    }
  },
  mounted() {
    /* SongRow gets passed a Song object from Songs.vue. It then
       has to query the API again for the artist and album.
       This method results in a crap ton of queries??! 
       > Re-structure the Django models? */
    
    /* Consider re-implementing as a Table so the song list can be sorted? */

    /* This method only grabs the FIRST artist and album, not all of them */
      /* var numArtists = this.song.artists.length;
      /* /* eslint-disable */
      /* console.log("num artists");
      /* console.log(numArtists);
      /* /* eslint-enable */

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
       the album name from displaying "Object" if it is undefined */
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

    this.$watch('storedSong', function() {
      /* eslint-disable */
      console.log("stored")
      console.log(this.storedSong.audio)
      console.log("this")
      console.log(this.song.audio)
      if (this.storedSong.audio == this.song.audio) {
        this.bgcolor = 'green'
        console.log("green")
      } else {
        this.bgcolor = 'white' 
        console.log("white")
      }
      /* eslint-enable */
    })
  },

  computed: {
    storedSong() {
      return this.$store.state.song;
    }
  }
}
</script>

<style lang="scss">
#rowstyle {
  background-color: var(---bgcolor);
}
</style>
