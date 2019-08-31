<template>
  <div>
    <audio controls ref="player">
      <source v-bind:src="song" type="audio/mp3">
      Your browser does not support the audio element.
    </audio>
    <p> {{ title }} </p >
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      name: '',
      artist: '',
      album: '',
      path: '',
      current_time: 0,
      total_time: 0
    } 
  },
  
  /* This is a workaround... creating a function that gets mounted?
     Isn't there a specific watcher "lifecycle" function? */
  /* An error gets logged to the console on startup
     that the media player can't load unsupported text/html type.
     I believe this is because the "song" variable is empty at startup? */
  mounted: 
  /* The HTML player does not recognize when the source changes. */
  function() {
    this.$watch('song', function() {
      this.$refs.player.load()
      this.$refs.player.play()
    });
    /* eslint-disable */
    console.log("refs")
    console.log(this.$refs)
    /* eslint-enable */
  },
  computed: {
    /* Consider renaming to URL or something else */
    song() {
      return this.$store.state.song;
    },
    title() {
      return this.$store.state.title;
    }
  }
}
</script>

<style>
</style>
