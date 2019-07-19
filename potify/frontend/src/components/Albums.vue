<template>
  <div>
    <h2>Albums</h2>
    <p>This is a list of albums.</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Albums',
  data: function() {
    return {
      album_list: [],
    }
  },
  mounted() { //created or mounted, which one?
    axios.get('api/songs').then((response) => {
      this.album_list = response.data.results
      // eslint-disable-next-line
      console.log('Album_List:')
      // eslint-disable-next-line
      console.log(this.album_list)
    })
  }
}
</script>

<style>
</style>
