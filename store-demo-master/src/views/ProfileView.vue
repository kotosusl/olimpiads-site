<template>
   <div v-if="calculatePageSize() > 800">
      <div class="profile-body-div">
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
         <div class="profile-information">
         <div class="profile-page-name">
            <h1>Профиль</h1>
         </div>
      <div class="profile-avatar-and-user-info">
         <div class="profile-avatar">
            <el-avatar :size="100" :src="circleUrl" />
         </div>
         <div class="profile-user-info">
               <h1>{{ user.surname }}</h1>
               <h1>{{ user.name }}</h1>
               <h2>{{ user.school_class }} класс</h2>

               <el-radio-group v-model="user.male">
            <el-radio label="M" disabled>Мужской</el-radio>
            <el-radio label="F" disabled>Женский</el-radio>
         </el-radio-group>
         <br>
         <div class="profile-special-div">
            <h3>Интересующие предметы:</h3>
            <div class="profile-user-subjects">
               <el-row>
                  <p v-for="(subject, index) in user.subjects" :key="index" class="profile-subjects">{{ subject }}</p>
               </el-row>
            </div>
         </div>
      <el-checkbox-group v-model="user.messages_places">
            <el-checkbox value="Mail" label="Mail" name="message_places" disabled/>
            <el-checkbox value="VK" label="VK" name="message_places" disabled />
            <el-checkbox value="Telegram" label="Telegram" name="message_places" disabled />
         </el-checkbox-group>
      </div>
      </div>
      <br>
      <div class="profile-buttons">
      <el-button type="primary" color="#626aef" @click="myClickHandler">Изменить</el-button>
      <el-dialog v-model="dialogVisible" title="Изменить профиль" width="60%" modal>
         <div class="profile-edit-profile">
         <EditProfileForm @onupdate="onFormUpdate" @oncancel="onFormCancel" />
      </div>
      </el-dialog>
      <router-link to="/user/select_olimps"><el-button color="#626aef" type="primary">Мои олимпиады</el-button></router-link>
      <el-button type="danger" plain>Выйти из аккаунта</el-button>
   </div>
    </div>
   </div>
   </div>

   <!-----------------Mobile-version--------------------->

    <div v-else>
      <div class="mobile-profile-body-div">
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
         <div class="mobile-profile-information">
         <div class="mobile-profile-page-name">
            <h1>Профиль</h1>
         </div>
      <div class="mobile-profile-avatar-and-user-info">
         <div class="mobile-profile-avatar">
            <el-avatar :size="80" :src="circleUrl" />
         </div>
         <div class="mobile-profile-user-info">
               <h1>{{ user.surname }}</h1>
               <h1>{{ user.name }}</h1>
               <h2>{{ user.school_class }} класс</h2>

               <el-radio-group v-model="user.male">
            <el-radio label="M" disabled>Мужской</el-radio>
            <el-radio label="F" disabled>Женский</el-radio>
         </el-radio-group>
         <br>
         <div class="profile-special-div">
            <h3>Интересующие предметы:</h3>
            <div class="mobile-profile-user-subjects">
               <el-row>
                  <p v-for="(subject, index) in user.subjects" :key="index" class="mobile-profile-subjects">{{ subject }}</p>
               </el-row>
            </div>
         </div>
      <el-checkbox-group v-model="user.messages_places" class="profile-message-places">
            <el-checkbox value="Mail" label="Mail" name="message_places" disabled/>
            <el-checkbox value="VK" label="VK" name="message_places" disabled />
            <el-checkbox value="Telegram" label="Telegram" name="message_places" disabled />
         </el-checkbox-group>
      </div>
      </div>
      <br>
      <div class="mobile-profile-buttons">
      <el-button type="primary" color="#626aef" @click="myClickHandler">Изменить</el-button>
      <el-dialog v-model="dialogVisible" title="Изменить профиль" width="85%" modal>
         <div class="mobile-profile-edit-profile">
         <EditProfileForm @onupdate="onFormUpdate" @oncancel="onFormCancel" />
      </div>
      </el-dialog>
      <router-link to="/user/select_olimps"><el-button color="#626aef" type="primary">Мои олимпиады</el-button></router-link>
      <el-button type="danger" plain>Выйти из аккаунта</el-button>
   </div>
    </div>
   </div>
    </div>
 </template>

 <style src="/src/views/ProfileView.css"></style>
 
 <script setup>
 import { ref, reactive } from 'vue'
 import EditProfileForm from '@/forms/EditProfileFrom.vue'
 import { UserList } from '@/store/UsersData.js'
 import { UserFilled } from '@element-plus/icons-vue'
 import { toRefs } from 'vue'

const activeIndex = ref('/profile')

 const state = reactive({
  circleUrl:
    'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
})

const { circleUrl } = toRefs(state)
 
 const calculatePageSize = () => {
    const width = ref(window.innerWidth);
    return width.value;
};


 let user = reactive(UserList().users[0])
 const dialogVisible = ref(false)
 

 function myClickHandler()
 {
    dialogVisible.value = true
 }
 
 function onFormUpdate(data)
 {
    console.log(JSON.stringify(data))
    onFormCancel()
 }
 
 function onFormCancel()
 {
    dialogVisible.value = false
 }
 </script>