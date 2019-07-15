import Vue from 'vue'
import App from './App.vue'
import router from './router'

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
  render: h => h(App),
}).$mount('#app')
