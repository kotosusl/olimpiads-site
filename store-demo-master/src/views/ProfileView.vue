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
            <h1>Профиль 1234</h1>
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
         <div class="profile-email-button">
            <h2>Почта: {{ user.email }}</h2>
            <el-button type="primary" color="#626aef">Привязать почту</el-button>
            <el-popover
               placement="top-start"
               title="Зачем привязывать почту?"
               :width="350"
               trigger="hover"
               content="Привяжите почту, чтобы быть уверенным, что уведомления смогут приходить на Вашу электронную почту. (Во избежание неточностей в указании адреса электронной почты)"
            ><template #reference>
               <el-button class="profile-question" color="#626aef" plain>?</el-button>
            </template></el-popover>
         </div>
         <div class="profile-telegram-name">
            <h3>Telegram username (имя пользователя @): {{ user.telegram_name }}</h3>
            <a href="https://t.me/olimpiads_reminder_bot" target="_blank"><el-button type="primary" color="#626aef">Перейти в бот</el-button></a>
            <el-button type="primary" color="#626aef" @click="checkUsername">Проверить username</el-button>
            <el-popover
               placement="top-start"
               title="Что такое username? Подключи уведомления в 3 шага"
               :width="450"
               trigger="hover"
               content='Для отправления уведомлений в Telegram требуется username (Имя пользователя). 
               1. Чтобы его задать зайдите в Telegram, нажмите на три полоски в левом верхнем углу > Настройки > Имя пользователя.
               2. После перейдите в телеграм бот по кнопке "Перейти в бот" и запустите его, нажав "Старт".
               3. Укажите @Username в окне "Изменить" и нажмите кнопку "Проверить username" (Должно прийти сообщение в чате).'
            ><template #reference>
               <el-button class="profile-question" color="#626aef" plain>?</el-button>
            </template></el-popover>

         </div>
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
      <el-button type="danger" plain @click="logOutButton">Выйти из аккаунта</el-button>
   </div>
    </div>
    <div class="footer-div"></div>
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
         <div class="mobile-profile-email-button">
            <h2>Почта: {{ user.email }}</h2>
            <el-button type="primary" color="#626aef">Привязать почту</el-button>
            <el-popover
               placement="top-start"
               title="Зачем привязывать почту?"
               :width="250"
               trigger="hover"
               content="Привяжите почту, чтобы быть уверенным, что уведомления смогут приходить на Вашу электронную почту. (Во избежание неточностей в указании адреса электронной почты)"
            ><template #reference>
               <el-button class="mobile-profile-question" color="#626aef" plain>?</el-button>
            </template></el-popover>
         </div>
         <div class="mobile-profile-telegram-name">
            <h3>Telegram username (имя пользователя @): {{ user.telegram_name }}</h3>
            <a href="https://t.me/olimpiads_reminder_bot" target="_blank"><el-button type="primary" color="#626aef">Перейти в бот</el-button></a>
            <el-button type="primary" color="#626aef" @click="checkUsername">Проверить username</el-button>
            <el-popover
               placement="top-start"
               title="Что такое username? Подключи уведомления в 3 шага"
               :width="300"
               trigger="hover"
               content='Для отправления уведомлений в Telegram требуется username (Имя пользователя). 
               1. Чтобы его задать зайдите в Telegram, нажмите на три полоски в левом верхнем углу > Настройки > Имя пользователя.
               2. После перейдите в телеграм бот по кнопке "Перейти в бот" и запустите его, нажав "Старт".
               3. Укажите @Username в окне "Изменить" и нажмите кнопку "Проверить username" (Должно прийти сообщение в чате).'
            ><template #reference>
               <el-button class="mobile-profile-question" color="#626aef" plain>?</el-button>
            </template></el-popover>

         </div>
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
      <router-link to="/user/select_olimps"><el-button color="#626aef" type="primary" >Мои олимпиады</el-button></router-link>
      <el-button type="danger" plain @click="logOutButton">Выйти из аккаунта</el-button>
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
 import { userToken } from '@/store/tokenData'
 import router from '@/router'
 import { ElMessage } from 'element-plus'

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

let url = '/api/get_profile_info';
let request_options = {
   method: 'POST',
   headers: {
      Accept: '*/*',
   'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
   'Content-Type': 'application/json',
   'x-access-token': userToken.getters.get_token
},
body: userToken.getters.get_request
}

let user = ref({})

fetch(url, request_options)
.then(res => res.json())
.then(json => {
   if (json['success'] != 'OK') {
      router.push('/login');
      
   } else if (json['success'] == 'OK'){
      user.value = json['profile_info'];
      if (user.value.name == null) user.value.name = 'Имя';
      if (user.value.surname == null) user.value.surname = 'Фамилия';
      if (user.value.subjects.length == 0) user.value.subjects = ['Не выбрано'];
      if (user.value.school_class == null) user.value.school_class = 11;
      if (user.value.telegram_name == null) user.value.telegram_name = 'Не задано';
      userToken.commit('set_request', "{}");
   }
})
.catch(err => console.error('error:' + err));



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

 function logOutButton(){
   userToken.commit('set_token', '')
   router.push('/about')
 }

 const successMessage = (mess) => {
  ElMessage({
    showClose: true,
    message: mess,
    type: 'success',
    duration: 10000
  })
}

const infoMessage = (mess) => {
   ElMessage({
    showClose: true,
    message: mess,
    type: 'info',
    duration: 10000
  })
}

 function checkUsername(){
   let url = '/api/check_telegram_name';
   let request_options = {
   method: 'GET',
   headers: {
      Accept: '*/*',
      'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
      'Content-Type': 'application/json',
      'x-access-token': userToken.getters.get_token
      }
   }

   fetch(url, request_options)
   .then(res => res.json())
   .then(json => {
      if (json['success'] != 'OK') {
         router.push('/login')
         
      } else if (json['success'] == 'OK'){
         if (json['info'] != 'Username подтверждён.') infoMessage(json['info']);
         else successMessage(json['info']);
      }
   })
   .catch(err => console.error('error:' + err));
 }
 </script>