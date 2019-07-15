import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Artists from '@/components/Artists'
import Albums from '@/components/Albums'
import Songs from '@/components/Songs'
import Playlists from '@/components/Playlists'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/artists',
      name: 'Artists',
      component: Artists 
    },
    {
      path: '/albums',
      name: 'Albums',
      component: Albums 
    },
    {
      path: '/songs',
      name: 'Songs',
      component: Songs
    },
    {
      path: '/playlists',
      name: 'Playlists',
      component: Playlists 
    }
  ]
})
