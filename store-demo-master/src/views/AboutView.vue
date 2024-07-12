<template>
  <div class="about-body-div"> 
    <nav class="about-nav"> 
        <img src="" alt="Logo">
        <div class="about-nav-buttons">
          <router-link to="/login"><el-button color="#626aef">Войти</el-button></router-link>
          <router-link to="/register"><el-button color="#626aef">Зарегистрироваться</el-button></router-link>
        </div>
    </nav>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const activeIndex = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<style>

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Monsterrat', sans-serif;
    
}

.about-body-div{
    background-color: #c9d6ff;
    background: linear-gradient(to right, #e2e2e2, #c9d6ff);
    height: 100vh;
}

.about-nav-buttons{
    display: inline-flex;
    justify-content: space-between;
    min-width: 250px;
    justify-self: end;
    padding: 5px;
    
}

.about-nav{
    display: inline-flex;
    padding: 20px;
    background-color: #fff;
    width: 100%;
    height: 10%;
    min-height: 70px;
    max-height: 90px;
    align-items: center;
    justify-content: space-between;
    border-radius: 0 0 15px 15px;
    position: fixed;
    top: 0;
    border: 10px;
}


</style>