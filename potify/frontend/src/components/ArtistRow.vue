<template>
  <div>
    <b-row>
      <b-col>{{ artist.name }}</b-col>
      <!-- rel=noopener noreferrer is a security precaution when opening
        links in a new window -->
      <b-col><a v-bind:href="artist.image" rel="noopener noreferrer"
          target="_blank">
          <img v-bind:src="artist.image">
          </a></b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: 'ArtistRow',
  props: {
    artist: Object
  }
}
</script>

<style>
img {height: 1em;

}
</style>
