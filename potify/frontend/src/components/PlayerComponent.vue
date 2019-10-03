<template>
  <div>
    <audio controls ref="player">
    <source v-bind:src="song.audio" type="audio/mp3">
    Your browser does not support the audio element.
    </audio>
    <div id="player-text">
      Vibrating your eardrums...
      <p v-html="details"></p>
    </div>
  </div>
</template>

<script>
//i cant comment this in HTML
//{{song.title}} --- by <b>{{artists.name}}</b> --- from <i>{{albums.name}}</i>  

import axios from 'axios'
//import CurrentlyPlaying from './CurrentlyPlaying.vue'

export default {
  data: function() {
    return {
      artists: Object,
      albums: Object,
    }
  },
  //components: {
  //  CurrentlyPlaying
  //},
  /* This is a workaround: mount a watcher function.
     Isn't there a specific watcher "lifecycle" function?
     "lifecycle" refers to the types of built in functions in Vue
     such as mounted, created, computed, etc. */
  /* An error gets logged to the console on startup
     that the media player can't load unsupported text/html type.
     I believe this is because the "song" variable is empty at startup? */
  methods: {
    //async getAsync(url) {
    //  let json = await axios.get(url); 
    //  return json;
    //},
    //updateDetails() {
    //  this.details = ''.concat('{{ ', this.song.title, '}} --- by <b>{{ ',
    //    this.artists.name, ' }}</b> --- from <i>{{ ',
    //    this.albums.name, ' }}</i>')
      //this.details = {
      //  title: this.song.title,
      //  artist: this.artists.name,
      //  album: this.albums.name
      //}
    //}
  },
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
        //this.getAsync(artistUrl)
        //  .then((response) => {
        //    this.artists = response.data 
        //  })
        /* Also copied and pasted this from SongRow to get album... */
        /* eslint-disable */
        try {
          var albumPrim = this.song.albums[0].valueOf();
          var albumUrl = albumPrim.slice(sliceIdx, albumPrim.length);
          axios.get(albumUrl)
          .then((response) => {
            this.albums= response.data
          })
          //this.getAsync(albumUrl)
          //  .then((response) => {
          //    this.albums = response.data
          //    //console.log("got album")
          //})
        } catch (e) {
          console.log("e")
          this.albums = {
            name: 'unknown album'
          }
        }
        //setTimeout(this.updateDetails(), 9999999); 
        //console.log("details")
        //console.log(this.details)
        /* eslint-enable */
        });
        /* eslint-disable */
        //console.log("refs")
        //console.log(this.$refs)
        /* eslint-enable */
    },
  // },
  computed: {
    song() { /* song object */
      return this.$store.state.song;
    },
    details() {
      /* eslint-disable */
      console.log("song")
      console.log(this.song)
      if (this.song.length === 1) {
        //Object.entries(obj).length === 0 && obj.constructor === Object
        return '...nothing yet!'
      }
      else {
        console.log("else")
        /* eslint-enable */
        return ''.concat(this.song.title, ' --- by <b>',
          this.artists.name, '</b> --- from <i>',
          this.albums.name, '<i>')
      }
    }
  }
}
</script>

<style>
#player-text {
  color: white;
}
</style>
