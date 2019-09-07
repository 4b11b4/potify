<template>
  <div>
    <b-row>
      <b-col>{{ artist.name }}</b-col>
      <b-col><a v-bind:href="artist.image">
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
