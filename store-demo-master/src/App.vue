<template>
   <h1>APP</h1>
   <div class="main-nav">
      <ul>
         <li><router-link to="/">Main page</router-link></li>
         <li><router-link to="/list">List page</router-link></li>
         <li><router-link to="/about">About page</router-link></li>
         <li><router-link to="/login">Login page</router-link></li>

      </ul>
   </div>
   <br />
   <router-view></router-view>
</template>