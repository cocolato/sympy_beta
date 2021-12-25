import { createApp } from 'vue'
import VueMathjax from 'vue-mathjax-next'
import App from '@/App.vue'
import router from '@/router'

createApp(App)
  .use(router)
  .use(VueMathjax)
  .mount('#app')
