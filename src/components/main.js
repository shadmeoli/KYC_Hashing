import Vue from 'vue';
import VueRouter from 'vue-router';

import App from './App';

import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';

import Login from './components/Login';
import Main  from './components/Main';

Vue.use(VueRouter);
Vue.use(Vuetify, {
   theme: {
      primary: '#7957d5',
   },
});

const router = new VueRouter({
   routes: [
      {
         path: '/login',
         component: Login,
      },
      {
         path: '/main',
         component: Main,
      }
   ],
});

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
   router: router,
   el: '#app',
   components: { App },
   template: '<App/>',
});

router.replace('/login');
