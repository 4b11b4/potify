import Vue from 'vue'
import App from './App.vue'
import router from './router'

import BootstrapVue from 'bootstrap-vue'
Vue.use(BootstrapVue)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import { store } from './store'

/* Currently, axios is loaded directly by the Songs
 * component. Loading it here did not allow the
 * component to utilize it.
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)
*/

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
