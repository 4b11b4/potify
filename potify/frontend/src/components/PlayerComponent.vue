<template>
  <div>
    <audio controls ref="player">
      <source v-bind:src="song" type="audio/mp3">
      Your browser does not support the audio element.
    </audio>
    <p> {{ song }} </p >
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
  /* Actually load the song when the source changes */
  mounted: function() {
    this.$watch('song', function() {
      this.$refs.player.load()
      this.$refs.player.play()
    });
    // eslint-disable-next-line
    console.log(this.$refs)
  },
  computed: {
    song() {
      return this.$store.state.song;
    }
  }
}
</script>

<style>
</style>
