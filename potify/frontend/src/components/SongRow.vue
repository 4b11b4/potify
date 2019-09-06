<template>
  <div :class="{'is-green': isActive, 'is-white': !isActive}">
    <b-row>
      <b-col>{{ song.play_count }}</b-col>
      <b-col>{{ song.title }}</b-col>
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
      isActive: false,
    }
  },
  /* Added this in addition to the watcher in order for the "active" song
     styling to be applied when the Songs tab is switched to */
  /* I still do not know the difference between created and mounted... */
  created() {
    if (this.storedSong.audio == this.song.audio) {
      this.isActive = true;
    } else {
      this.isActive = false;
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
    
    /* If the inherited property Song object is the same as the song
       which is stored in the vuex store, then change the CSS class of the
       SongRow */
    this.$watch('storedSong', function() {
    if (this.storedSong.audio == this.song.audio) {
      this.isActive = true;
    } else {
      this.isActive = false;
    }
    })
  },

  computed: {
    storedSong() {
      return this.$store.state.song;
    }
  }
}
</script>

<style>
.is-white {
  background-color: white;
}
.is-green {
  background-color: rgba(0, 150, 0, .25);
  border-radius: 7px;
  font-weight: bold;
}
</style>
