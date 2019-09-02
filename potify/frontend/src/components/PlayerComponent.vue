<template>
  <div>
    <audio controls ref="player">
    <source v-bind:src="audio" type="audio/mp3">
    Your browser does not support the audio element.
    </audio>
    <p><i>Vibrating your eardrums... </i>
    <b>{{title}}</b>
    </p>
  </div>
</template>

<script>
  export default {
    /* This is a workaround... creating a function that gets mounted?
       Isn't there a specific watcher "lifecycle" function? */
    /* An error gets logged to the console on startup
       that the media player can't load unsupported text/html type.
       I believe this is because the "song" variable is empty at startup? */
    mounted:
    /* The HTML player does not recognize when the source changes. */
    function() {
      this.$watch('audio', function() {
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
      audio() {
        return this.$store.state.audio;
      },
      title() {
        return this.$store.state.title;
      }
    }
  }
</script>

<style>
</style>
