import { createApp } from 'vue';
import { pinia } from './stores';
import App from './App.vue';
import router from './router';
import './style.css';
import '@icon-park/vue-next/styles/index.css';

// 导入v-calendar并注册
import VCalendar from 'v-calendar';
import 'v-calendar/style.css';

const app = createApp(App);

app.use(pinia)
   .use(router)
   .use(VCalendar, {
     componentPrefix: 'v'
   })
   .mount('#app');