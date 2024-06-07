<template>
   <h3>me</h3>
   <nav class="main-nav">
         <router-link to="/"><button>Main page</button></router-link>
         <router-link to="/list"><button>List page</button></router-link>
         <router-link to="/about"><button>About page</button></router-link>
         <router-link to="/login"><button>Login page</button></router-link>
         <router-link to="/register"><button>Register page</button></router-link>
         <router-link to="/profile"><button>Profile page</button></router-link>
   </nav>
   <br />
   <router-view></router-view>
</template>

<style>
.main-nav{
   display: flex;
   justify-content: space-around;

}
</style>