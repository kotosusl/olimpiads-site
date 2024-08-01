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
            <el-input v-model="input_serch" placeholder="Введите название олимпиады" clearable class="inputs-words" />
         </el-col>
         <el-cascader :options="options1" :show-all-levels="false" class="inputs" placeholder="Предмет" />
         <el-cascader :options="options2" :show-all-levels="false" class="inputs" placeholder="Класс" />
         <el-button color="#626aef" type="primary" :icon="Search" @click="onSearch" class="main-search-button">Поиск</el-button>
   </el-row>
   </div>
   <div class="main-cards-box">
      <el-row :gutter="10" justify="center">
      <el-col v-for="(olimpiada, index) in olimps" :key="index" class="olimp-card" :xs="23" :sm="11" :md="11" :lg="7" :xl="5">
         <el-card class="box-card" shadow="hover" @click="cardOnClick">
            <template #header>
               <div class="card-header">
                  <el-row><h1>{{ olimpiada.name }}</h1></el-row>
               </div>
            </template>
            <div class="main-card-body">
               <p>{{olimpiada.min_class }}-{{ olimpiada.max_class }} класс</p>
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
               <el-button class="button" type="success" @click="addOlimpNotification">Добавить уведомление</el-button>
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
import { ref } from 'vue'
const emit = defineEmits(['onsearch'])

const activeIndex = ref('/')

const input_serch = ref('')


const olimps = OlimpList().olimps



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

const options2 = [
        {value: '1', label: '1'}, {value: '2', label: '2'}, {value: '3', label: '3'}, {value: '4', label: '4'}, {value: '5', label: '5'},
        {value: '6', label: '6'}, {value: '7', label: '7'}, {value: '8', label: '8'}, {value: '9', label: '9'}, {value: '10', label: '10'},
        {value: '11', label: '11'}];


function onSearch(){
   // input_search 
   let request = JSON.stringify({"search": input_serch,
                                 "option": options1})
   emit('onsearch')

}

let a = 1;

function addOlimpNotification(){
   a = 1;
}

function cardOnClick(){
   if (a == 1){
      window.location.href = '/one_olimp'
   }
}
</script>