<template>
   <div class="main-body-div">
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
   <h1>Найти олимпиаду</h1>
   <div class="main-search-div">
      <el-row>
         <el-col :xs="23" :sm="14" :md="11" :lg="11" :xl="6">
            <el-input v-model="input_search" placeholder="Введите название олимпиады" clearable class="inputs-words" />
         </el-col>
         <el-cascader v-model="value_options1" :options="options1" :show-all-levels="false" class="inputs" placeholder="Предмет" />
         <el-cascader v-model="value_options2" :options="options2" :show-all-levels="false" class="inputs" placeholder="Класс" />
         <el-button color="#626aef" type="primary" :icon="Search" @click="onSearch" class="main-search-button">Поиск</el-button>
   </el-row>
   </div>
   <div class="main-cards-box">
      <el-row :gutter="10" justify="center">
      <div v-if="olimps.length == 0" class="main-no-olimp"><p>Олимпиад не найдено</p></div>
      <el-col v-else v-for="(olimpiada, index) in olimps" :key="index" class="olimp-card" :xs="23" :sm="11" :md="11" :lg="7" :xl="5">
         <el-card class="box-card" shadow="hover" @click="cardOnClick(olimpiada.id)">
            <template #header>
               <div class="card-header">
                  <el-row><h1>{{ olimpiada.name }}</h1></el-row>
               </div>
            </template>
            <div class="main-card-body">
               <div v-if="olimpiada.min_class == olimpiada.max_class"><p>{{olimpiada.min_class }} класс</p></div>
               <div v-else><p>{{olimpiada.min_class }}-{{ olimpiada.max_class }} класс</p></div>
               <div class="main-subject-box">
                  <el-row>
                     <div class="main-text-item">По предметам:</div>
                     <div v-for="(i, indx) in olimpiada.subjects" :key="indx" class="main-text-item">
                        <div v-if="indx == olimpiada.subjects.length - 1">{{ i }}</div>
                        <div v-else>{{ i }},</div></div>
                  </el-row>
               </div>
            </div>
            
            <template #footer>
               <el-button v-show="olimpiada.user_have == 'False'" class="button" type="success" @click="clickGreenButton">Добавить уведомление</el-button>
               <el-button v-show="olimpiada.user_have == 'True'" class="button" type="danger" plain @click="clickRedButton">Не показывать уведомления</el-button>
            </template>
         </el-card>
      
      </el-col>
   </el-row>
   </div>
   </div>
</template>

<style src="/src/views/MainView.css"></style>


<script setup>
import { OlimpList } from '@/store/index.js'
import { ref, reactive, computed, toRefs } from 'vue'
import { userToken } from '@/store/tokenData';
import { storeToRefs } from 'pinia';
import { defineComponent } from 'vue';
import router from '@/router';
import { ElMessage } from 'element-plus'


let url = '/api/get_searching_olimpiads';

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
                  router.push('/login');
                  
                } else if (json['success'] == 'OK'){
                     for (let i = 0; i < json['olimps'].length; i++){
                        olimps.push(json['olimps'][i]);
                     }
                     userToken.commit('set_request', "{}");
                }
            })
            .catch(err => console.error('error:' + err));



const emit = defineEmits(['onsearch'])

const activeIndex = ref('/')

const input_search = ref('')

const value_options1 = ref([])


const options1 = [{label: 'Технические науки', children: [{value: 'математика', label: 'Математика'}, {value: 'физика', label: 'Физика'}, 
                                                          {value: "информатика", label: 'Информатика'}, {value: "робототехника", label: 'Робототехника'},
                                                          {value: "черчение", label: 'Черчение'}]}, 
                  {label: 'Языковедение', children: [{value: 'английский язык', label: 'Английский язык'}, {value: 'русский язык', label: 'Русский язык'}, 
                                                     {value: 'немецкий язык', label: 'Немецкий язык'}, {value: 'французский язык', label: 'Французский язык'}, 
                                                     {value: 'лингвистика', label: 'Лингвистика'}, {value: 'испанский язык', label: 'Испанский язык'}, 
                                                     {value: 'латинский язык', label: 'Латинский язык'}, {value: 'китайский язык', label: 'Китайский язык'},
                                                     {value: 'итальянский язык', label: 'Итальянский язык'}, {value: 'арабский язык', label: 'Арабский язык'},
                                                     {value: 'японский язык', label: 'Японский язык'}, {value: 'корейский язык', label: 'Корейский язык'}]},
                  {label: 'Социально-гуманитарные', children: [{value: 'литература', label: 'Литература'}, {value: 'история', label: 'История'},
                                                               {value: 'обществознание', label: 'Обществознание'}, {value: 'экономика', label: 'Экономика'},
                                                               {value: 'право', label: 'Право'}, {value: 'обществознание', label: 'Обществознание'},
                                                               {value: 'основы предпринимательства', label: 'Основы предпринимательства'},
                                                               {value: 'психология', label: 'Психология'}, {value: 'менеджмент', label: 'Менеджмент'}]}, 
                  {label: 'Естественные науки', children: [{value: 'биология', label: 'Биология'}, {value: 'география', label: 'География'}, 
                                                           {value: "химия", label: 'Химия'}, {value: 'экология', label: 'Экология'}, {value: 'астрономия', label: 'Астрономия'},
                                                           {value: 'обществознание', label: 'Обществознание'},]},
                  {label: "Искусство, физкультура, ОБЖ", children: [{value: 'обж', label: 'ОБЖ'}, {value: 'технология', label: 'Технология'},
                                                                    {value: 'искусство', label: 'Искусство'}, {value: 'физкультура', label: 'Физкультура'},
                                                                    {value: 'изо', label: 'ИЗО'}]}
               ];

const value_options2 = ref([]);

const options2 = [
        {value: '1', label: '1'}, {value: '2', label: '2'}, {value: '3', label: '3'}, {value: '4', label: '4'}, {value: '5', label: '5'},
        {value: '6', label: '6'}, {value: '7', label: '7'}, {value: '8', label: '8'}, {value: '9', label: '9'}, {value: '10', label: '10'},
        {value: '11', label: '11'}];


function onSearch(){
   // input_search 
   let request = JSON.stringify({"name_olimp": input_search.value,
                                 "subjects": value_options1.value[1],
                                 "search_class": value_options2.value[0]})

   userToken.commit('set_request', request);
   userToken.commit('set_reload_page', '/')
   router.push('/reload');
   
   
   emit('onsearch')
}

const successMessage1 = () => {
  ElMessage({
    showClose: true,
    message: 'Олимпиада успешно добавлена',
    type: 'success',
    duration: 12000
  })
}

const successMessage2 = () => {
  ElMessage({
    showClose: true,
    message: 'Уведомления успешно убраны',
    type: 'success',
    duration: 12000
  })
}

const successMessage3 = (mess) => {
  ElMessage({
    showClose: true,
    message: mess,
    type: 'info',
    duration: 8000
  })
}

let a = 2;

function clickGreenButton(){
   a = 0;
}

function clickRedButton(){
   a = 1;
}


function cardOnClick(olimp_id){
   function addOlimpNotification(olimp_id){
      let url = '/api/add_olimp_to_user';
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
            if (json['info']) successMessage3(json['info']);
            else successMessage1();
         }
      })
      .catch(err => console.error('error:' + err));
   }
   
   function deleteOlimpNotification(olimp_id){
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
            if (json['info']) successMessage3(json['info']);
            else successMessage2();
         }
      })
      .catch(err => console.error('error:' + err));
   }

   if (a == 0){
      addOlimpNotification(olimp_id);
   } else if (a == 1){
      deleteOlimpNotification(olimp_id);
   } else if (a == 2){
      let request = JSON.stringify({'olimp_id': olimp_id});
      userToken.commit('set_request', request);
      router.push('/one_olimp');
   }
   a = 2;
}
</script>