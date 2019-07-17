<template>
  <div class="player">
    <audio controls>
      <source :src='song' type="audio/mp3">
      Your browser does not support the audio element.
    </audio>
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
  computed: {
    song() {
      return this.store.state.song;
    }
  }
}
</script>

<style>
</style>
