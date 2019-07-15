<template>
  <div>
    <h1>Potify</h1>
    <nav>
      <router-link class="spacing" v-for="routes in links" 
      v-bind:key="routes.id"
      :to="`${routes.page}`">{{routes.text}}</router-link>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'Navigation',
  data() {
    return {
      links: [
        {
          id: 1,
          text: 'Home',
          page:'/Home'
        },
        {
          id: 2,
          text: 'Artists',
          page:'/Artists'
        },
        {
          id: 3,
          text: 'Albums',
          page:'/Albums'
        },
        {
          id: 4,
          text: 'Songs',
          page:'/Songs'
        },
        {
          id: 5,
          text: 'Playlists',
          page:'/Playlists'
        }
      ]
    }
  }
}
</script>

<style>
.spacing {
  margin-right: 10px;
}
</style>
