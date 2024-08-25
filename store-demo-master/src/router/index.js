import { createRouter, createWebHistory } from 'vue-router'
import MainView from '../views/MainView.vue'
import ListView from '../views/ListView.vue'
import AboutView from '../views/AboutView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import ProfileView from '../views/ProfileView.vue'
import OneOlimpView from '@/views/OneOlimpView.vue'
import SelectOlimpsView from '@/views/SelectOlimpsView.vue'
import NotificationsView from '@/views/NotificationsView.vue'
import ReloadView from '@/views/ReloadView.vue'

const router = createRouter({
   history: createWebHistory(import.meta.env.BASE_URL),
   routes: [
      {
         path: '/',
         name: 'main',
         component: MainView
      },
      {
         path: '/about',
         name: 'about',
         component: AboutView
      },
      {
         path: '/list',
         name: 'list',
         component: ListView
      },
      {
         path: '/login',
         name: 'login',
         component: LoginView
      },
      {
         path: '/register',
         name: 'register',
         component: RegisterView
      },
      {
         path: '/profile',
         name: 'profile',
         component: ProfileView
      },
      {
         path: '/one_olimp',
         name: 'one_olimp',
         component: OneOlimpView
      },
      {
         path: '/user/select_olimps',
         name: 'select_olimps',
         component: SelectOlimpsView
      },
      {
         path: '/user/notifications',
         name: 'notifications',
         component: NotificationsView
      },
      {
         path: '/reload',
         name:'reload',
         component: ReloadView
      }
   ]
})

export default router
