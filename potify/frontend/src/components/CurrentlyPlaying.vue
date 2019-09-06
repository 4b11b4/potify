<template>
  <div>
    {{details.title}} --- by <b>{{details.artist}}</b> --- from <i>{{details.album}}</i>
  </div>
</template>

<script>

export default {
  props: {
    details: {
      title: String,
      artist: String,
      album: String 
    }
  },
  data: function() {
    return {
      currentText: '...nothing yet!'
    }
  },
}
</script>

<style>
</style>
