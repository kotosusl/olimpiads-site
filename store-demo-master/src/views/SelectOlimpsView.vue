<template>
   <div class="select-body-div">
      <el-menu
        :default-active="activeIndex"
        class="main-el-menu"
        mode="horizontal"
        active-text-color="#626aef"
        :router="true"
    >
        <el-menu-item index="/" :route="{ name: 'main' }">Главная</el-menu-item>
        <el-menu-item index="/profile" :route="{ name: 'profile' }">Профиль</el-menu-item>
        <el-menu-item index="/user/notifications" :route="{ name: 'notifications' }">Уведомления</el-menu-item>
        <el-menu-item index="/user/select_olimps" :route="{ name: 'select_olimps' }">Мои олимпиады</el-menu-item></el-menu>
      <h1>Мои олимпиады</h1>
      <div class="select-search-div">
      <el-row>
         <el-col :xs="23" :sm="14" :md="11" :lg="11" :xl="6">
            <el-input v-model="input_serch" placeholder="Введите название олимпиады" clearable class="select-inputs-words" />
         </el-col>
         <el-button type="primary" color="#626aef" :icon="Search" @click="onSearch" class="select-search-button">Поиск</el-button>
      </el-row></div>
   
   <div class="select-cards-box">
      <el-row :gutter="10" justify="center">
      <el-col v-for="(olimpiada, index) in olimps" :key="index" class="select-olimp-card" :xs="23" :sm="11" :md="11" :lg="7" :xl="5">
         <el-card class="select-box-card" shadow="hover" @click="cardOnClick">
            <template #header>
               <div class="select-card-header">
                  <el-row><h1>{{ olimpiada.name }}</h1></el-row>
               </div>
            </template>
            <div class="select-card-body">
               <p>{{olimpiada.min_class }}-{{ olimpiada.max_class }} класс</p>
               <div class="select-subject-box">
                  <el-row>
                     <div class="select-text-item">По предметам:</div>
                     <div v-for="(i, indx) in olimpiada.subjects" :key="indx" class="select-text-item">
                        <div v-if="indx == olimpiada.subjects.length - 1">{{ i }}</div>
                        <div v-else>{{ i }},</div></div>
                  </el-row>
               </div>
            </div>
            
            <template #footer>
               <el-button class="button" type="danger" plain @click="addOlimpNotification">Убрать уведомления</el-button>
            </template>
         </el-card>
      
      </el-col>
   </el-row>
   </div>
</div>
</template>

<style src="/src/views/SelectOlimpsView.css"></style>


<script setup>
import { OlimpList } from '@/store/index.js'
import { ref } from 'vue'
const emit = defineEmits(['onsearch', 'ondeletenotification'])
const input_serch = ref('')
// import user olimps
const olimps = OlimpList().Olimps

const activeIndex = ref('/user/select_olimps')

function onSearch(){
   // input_search 
   emit('onsearch')

}

function deleteNotification()
{
   emit('ondeletenotification')
   // delete olimp_name in user_olimps
}
</script>