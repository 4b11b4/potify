<template>
  <div>
    <audio controls ref="player">
    <source v-bind:src="song.audio" type="audio/mp3">
    Your browser does not support the audio element.
    </audio>
    <p id="player-text">Vibrating your eardrums...<br>
    <b>{{song.title}}</b> --- by {{artists.name}} --- from <i>{{albums.name}}</i>
    </p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data: function() {
    return {
      artists: Object,
      albums: Object 
    }
  },
  /* This is a workaround: mount a watcher function.
     Isn't there a specific watcher "lifecycle" function?
     "lifecycle" refers to the types of built in functions in Vue
     such as mounted, created, computed, etc. */
  /* An error gets logged to the console on startup
     that the media player can't load unsupported text/html type.
     I believe this is because the "song" variable is empty at startup? */
  mounted:
  /* The HTML player does not recognize when the source changes. */
    function() {
      this.$watch('song', function() {
        this.$refs.player.load()
        this.$refs.player.play()
        /* Query artist in the same way that SongRow does */
        var artistPrim = this.song.artists[0].valueOf();
        var sliceIdx = artistPrim.indexOf("api"); // assume idx is same for both
        var artistUrl = artistPrim.slice(sliceIdx, artistPrim.length);
        axios.get(artistUrl)
          .then((response) => {
            this.artists = response.data
          })
        /* Also copied and pasted this from SongRow to get album... */
        try {
          var albumPrim = this.song.albums[0].valueOf();
          var albumUrl = albumPrim.slice(sliceIdx, albumPrim.length);
          axios.get(albumUrl).then((response) => {
            this.albums = response.data
          })
        } catch (e) {
          this.albums = {
            name: 'unknown album'
          }
        }
      });
      /* eslint-disable */
      console.log("refs")
      console.log(this.$refs)
      /* eslint-enable */
    },
  // },
  computed: {
    song() { /* song object */
      return this.$store.state.song;
    }
  }
}
</script>

<style>
#player-text {
  color: white;
}
</style>
