<template>
   <div v-if="calculatePageSize() > 800">
      <div class="one-olimp-body-div">
         <el-menu
        class="main-el-menu"
        mode="horizontal"
        active-text-color="#626aef"
        :router="true"
    >
        <el-menu-item index="/" :route="{ name: 'main' }">Главная</el-menu-item>
        <el-menu-item index="/profile" :route="{ name: 'profile' }">Профиль</el-menu-item>
        <el-menu-item index="/user/notifications" :route="{ name: 'notifications' }">Уведомления</el-menu-item>
        <el-menu-item index="/user/select_olimps" :route="{ name: 'select_olimps' }">Мои олимпиады</el-menu-item></el-menu>
         <div class="start-div"></div>
         <div class="one-olimp-name">
            <h1>{{ one_olimp['name'] }}</h1>
         </div>
         <div v-if="button_type == 'add_button'">
            <el-button type="success" class="add-olimp-button">Присылать уведомления</el-button>
         </div>
         <div v-else>
            <el-button type="danger" plain class="delete-olimp-button">Не присылать уведомления</el-button>
         </div>
         <div class="one-olimp-information">
            
            <div class="one-olimp-classes-and-subjects">
               <h6 class="one-olimp-classes"> {{ one_olimp['min_class'] }}-{{ one_olimp['max_class'] }} класс</h6>
               <div class="subject-box">
                  <div class="text-item"><p class="one-olimp-subjects">Предметы: </p></div>
                  <div v-for="(i, indx) in one_olimp['subjects']" :key="indx" class="text-item">
                     <div v-if="indx == one_olimp['subjects'].length - 1">{{ i }}</div>
                     <div v-else>{{ i }},</div>
                     </div>
               </div>
            </div>
            <h3 class="one-olimp-description">{{ one_olimp['desc'] }}</h3>
            <div class="one-olimp-href">
               Для того, чтобы узнать об олимпиаде, её организаторах, этапах и заданиях подробнее, перейдите по ссылке ниже. <br>
               Ссылка на подробную информацию: <a href="https://olimpiada.ru" onclick="location.href=this.href+ one_olimp['href']; return false;">{{ olimp_href }}</a>
            </div>
         </div>
      </div> 
   </div>

   <!-------------------Mobile-version------------------->

   <div v-else>
      <div class="mobile-one-olimp-body-div">
         <el-menu
        class="main-el-menu"
        mode="horizontal"
        active-text-color="#626aef"
        :router="true"
    >
        <el-menu-item index="/" :route="{ name: 'main' }">Главная</el-menu-item>
        <el-menu-item index="/profile" :route="{ name: 'profile' }">Профиль</el-menu-item>
        <el-menu-item index="/user/notifications" :route="{ name: 'notifications' }">Уведомления</el-menu-item>
        <el-menu-item index="/user/select_olimps" :route="{ name: 'select_olimps' }">Мои олимпиады</el-menu-item></el-menu>
         <div class="mobile-start-div"></div>
         <div class="mobile-one-olimp-name">
            <el-row>
               <h1>{{ one_olimp['name'] }}</h1>
            </el-row>
         </div>
         <div v-if="button_type == 'add_button'">
            <el-button type="success" class="mobile-add-olimp-button">Присылать уведомления</el-button>
         </div>
         <div v-else>
            <el-button type="danger" plain class="mobile-delete-olimp-button">Не присылать уведомления</el-button>
         </div>
         <div class="mobile-one-olimp-information">
            
            <div class="mobile-one-olimp-classes-and-subjects">
               <h6 class="mobile-one-olimp-classes"> {{ one_olimp['min_class'] }}-{{ one_olimp['max_class'] }} класс</h6>
               <div class="mobile-subject-box">
                  <el-row>
                     <div class="mobile-text-item"><p class="mobile-one-olimp-subjects">Предметы: </p></div>
                     <div v-for="i in one_olimp['subjects']" :key="i" class="mobile-text-item">{{ i }}</div>
                  </el-row>
               </div>
            </div>
            <h3 class="mobile-one-olimp-description">{{ one_olimp['desc'] }}</h3>
            <div class="mobile-one-olimp-href">
               Для того, чтобы узнать об олимпиаде, её организаторах, этапах и заданиях подробнее, перейдите по ссылке ниже. <br>
               Ссылка на подробную информацию: <a href="https://olimpiada.ru" onclick="location.href=this.href+ one_olimp['href']; return false;">{{ olimp_href }}</a>
            </div>
         </div>
      </div> 
      
   </div>
</template>

<style src="/src/views/OneOlimpView.css" />

<script setup>
import { ref, reactive } from 'vue'
import { OlimpList } from '@/store/OlimpData.js'

const calculatePageSize = () => {
    const width = ref(window.innerWidth);
    return width.value;
};

const one_olimp = OlimpList()['olimp'];
const olimp_href = 'https://olimpiada.ru' + one_olimp['href'];


const button_type = 'add_button';
</script>
