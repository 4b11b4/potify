<template>
  <div>
    <b-navbar toggleable="md" type="light" variant="light">
      <b-navbar-brand href="#">Potify</b-navbar-brand> 
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item active v-for="routes in links" 
          v-bind:key="routes.id"
          :to="`${routes.page}`">{{routes.text}}</b-nav-item>
   
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input class="mr-sm-2" placeholder="Search (not implemented)">
            </b-form-input>
            <b-button variant="outline-success" class="my-2 my-sm-0" type="submit">
              Search
            </b-button>
          </b-nav-form>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
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
/* Vue automatically sets the active
router link for you! */
nav a.router-link-active {
    font-weight: 700;
}
</style>
