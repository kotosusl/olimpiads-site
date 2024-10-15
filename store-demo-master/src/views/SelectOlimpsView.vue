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
      <div v-if="olimps.length == 0" class="select-no-olimp"><p>Олимпиад не найдено</p></div>
      <el-col v-else v-for="(olimpiada, index) in olimps" :key="index" class="select-olimp-card" :xs="23" :sm="11" :md="11" :lg="7" :xl="5">
         <el-card class="select-box-card" shadow="hover" @click="cardOnClick(olimpiada.id)">
            <template #header>
               <div class="select-card-header">
                  <el-row><h1>{{ olimpiada.name }}</h1></el-row>
               </div>
            </template>
            <div class="select-card-body">
               <div v-if="olimpiada.min_class == olimpiada.max_class"><p>{{olimpiada.min_class }} класс</p></div>
               <div v-else><p>{{olimpiada.min_class }}-{{ olimpiada.max_class }} класс</p></div>
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
               <el-button class="button" type="danger" plain @click="clickRedButton">Убрать уведомления</el-button>
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
import { ref, reactive } from 'vue'
import { userToken } from '@/store/tokenData';
import router from '@/router';
import { ElMessage } from 'element-plus'



const emit = defineEmits(['onsearch', 'ondeletenotification'])
const input_serch = ref('')
// import user olimps

let url = '/api/get_user_olimps';

let request_options = {
   method: 'POST',
   headers: {
   Accept: '*/*',
   'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
   'Content-Type': 'application/json',
   'x-access-token': userToken.getters.get_token
   },
   body: userToken.getters.get_request
};


let olimps = reactive([]);

fetch(url, request_options)
            .then(res => res.json())
            .then(json => {
                if (json['success'] != 'OK') {
                  router.push('/login')
                  
                } else if (json['success'] == 'OK'){
                     for (let i = 0; i < json['olimps'].length; i++){
                        olimps.push(json['olimps'][i]);
                     }
                     userToken.commit('set_request', "{}");
                }
            })
            .catch(err => console.error('error:' + err));


const activeIndex = ref('/user/select_olimps')

function onSearch(){
   let request = JSON.stringify({
      "search_name": input_serch.value
   })
   userToken.commit('set_reload_page', '/user/select_olimps')
   userToken.commit('set_request', request)
   router.push('/reload')
   emit('onsearch')

}

const successMessage1 = (mess) => {
  ElMessage({
    showClose: true,
    message: mess,
    type: 'info',
    duration: 8000
  })
}


const successMessage2 = () => {
  ElMessage({
    showClose: true,
    message: 'Уведомления успешно убраны',
    type: 'success',
    duration: 8000
  })
}

let a = 2;

function clickRedButton(){
   a = 1;
}

function cardOnClick(olimp_id){
   
   function deleteOlimpNotification(olimp_id)
{

   let url = '/api/remove_olimp_user';
   let request= JSON.stringify({'olimp_id': olimp_id})
   let request_options = {
      method: 'POST',
      headers: {
         Accept: '*/*',
      'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
         'Content-Type': 'application/json',
         'x-access-token': userToken.getters.get_token
      },
      body: request
   }

   fetch(url, request_options)
   .then(res => res.json())
   .then(json => {
      if (json['success'] != 'OK') {
         router.push('/login');
      
      } else if (json['success'] == 'OK'){
         if (json['info']) successMessage1(json['info']);
         else successMessage2();
      }
   })
   .catch(err => console.error('error:' + err));

   emit('ondeletenotification')
}

if (a == 1){
   deleteOlimpNotification(olimp_id);
} else if (a == 2){
   let request = JSON.stringify({'olimp_id': olimp_id});
   userToken.commit('set_request', request);
   router.push('/one_olimp');
}
a = 2;
}

</script>