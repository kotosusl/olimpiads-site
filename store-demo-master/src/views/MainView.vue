<template>
   <h1>Main</h1>
   <h3>User list</h3>
   <ul>
      <li v-for="(user, index) in users" :key="index">
         {{ user.name }}
      </li>
   </ul>
</template>

<script setup>
import { UserList } from '@/store/index.js'

const users = UserList().Users
</script>