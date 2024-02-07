import { createRouter, createWebHistory } from 'vue-router'
import MainView from '../views/MainView.vue'
import ListView from '../views/ListView.vue'
import AboutView from '../views/AboutView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import ProfileView from '../views/ProfileView.vue'

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
      }
   ]
})

export default router
