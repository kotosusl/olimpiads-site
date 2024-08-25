<template>
    <div v-if="calculatePageSize() > 760">
        <div class="notific-body-div">
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
            <h1>Уведомления</h1>
            <el-scrollbar ref="scrollbarRef" always class="notific-messages-window" height="80vh">
                <div v-if="notifications.length == 0" class="no-notific"><p>Уведомлений нет</p></div>
                <div v-else v-for="(notif, indx) in notifications" :key="indx" class="notific-message">
                    <div class="notific-date-time">
                        <span>{{ notif.message_date }} {{ notif.message_time }}</span>
                    </div>
                    <div class="notific-text-message">
                        <el-row>
                            <p>{{ notif.message_text }}</p>
                        </el-row>
                        <div class="notific-buttons">
                            <el-row>
                                <el-button color="#626aef" @click="toOneOlimp(notif.olimp_id)">Перейти к олимпиаде</el-button> 
                                <el-button type="danger" plain @click="deleteNotifications(notif.olimp_id)">Убрать уведомления</el-button>
                            </el-row>
                        </div>
                    </div>
                </div>
            </el-scrollbar>
        </div>
    </div>

<!-------------------Mobile-version---------------------->

    <div v-else>
        <div class="mobile-notific-body-div">
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
            <h1>Уведомления</h1>
            <el-scrollbar ref="scrollbarRef" always class="mobile-notific-messages-window" height="80vh">
                <div v-if="notifications.length == 0" class="mobile-no-notific"><p>Уведомлений нет</p></div>
                <div v-else v-for="(notif, indx) in notifications" :key="indx" class="mobile-notific-message">
                    <div class="mobile-notific-date-time">
                        <span>{{ notif.message_date }} {{ notif.message_time }}</span>
                    </div>
                    <div class="mobile-notific-text-message">
                        <el-row>
                            <p>{{ notif.message_text }}</p>
                        </el-row>
                            <div class="mobile-notific-buttons">
                                <el-button color="#626aef" @click="toOneOlimp(notif.olimp_id)">Перейти к олимпиаде</el-button> 
                                <br>
                                <el-button type="danger" plain @click="deleteNotifications(notif.olimp_id)">Убрать уведомления</el-button>
                            </div>
                    </div>
                </div>
            </el-scrollbar>
        </div>
    </div>
</template>

<style src="/src/views/NotificationsView.css"></style>

<script lang="ts" setup>
import { NotificationsList } from '@/store/Notific'
import { ElScrollbar, ElMessage } from 'element-plus'
import { reactive, ref } from 'vue'
import { userToken } from '@/store/tokenData';
import router from '@/router';

const calculatePageSize = () => {
    const width = ref(window.innerWidth);
    return width.value;
};

const activeIndex = ref('/user/notifications');

const notifications = reactive([]);

let url = '/api/get_notifications'
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

        for (let i = 0; i < json['notifications'].length; i++){
            notifications.push(json['notifications'][i]);
        }
   }
})
.catch(err => console.error('error:' + err));


function toOneOlimp(olimp_id){
    let request = JSON.stringify({
        olimp_id: olimp_id
    })
    userToken.commit('set_request', request)
    router.push("/one_olimp")
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

function deleteNotifications(olimp_id){
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
}

</script>