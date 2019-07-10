import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import App from './App.vue'
import router from './router'

Vue.use(VueAxios, axios)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')

Vue.axios.get('api/songs').then((response) => {
    /* eslint-disable no-console */
	console.log(response.data);
    /* eslint-enable no-console */
})
