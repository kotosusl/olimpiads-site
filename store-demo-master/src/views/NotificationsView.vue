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
                <div v-for="(notif, indx) in notifications" :key="indx" class="notific-message">
                    <div class="notific-date-time">
                        <span>{{ notif.message_date }} {{ notif.message_time }}</span>
                    </div>
                    <div class="notific-text-message">
                        <el-row>
                            <p>{{ notif.message_text }}</p>
                        </el-row>
                        <div class="notific-buttons">
                            <el-row>
                                <el-button color="#626aef">Перейти к олимпиаде</el-button> 
                                <el-button type="danger" plain>Убрать уведомления</el-button>
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
                <div v-for="(notif, indx) in notifications" :key="indx" class="mobile-notific-message">
                    <div class="mobile-notific-date-time">
                        <span>{{ notif.message_date }} {{ notif.message_time }}</span>
                    </div>
                    <div class="mobile-notific-text-message">
                        <el-row>
                            <p>{{ notif.message_text }}</p>
                        </el-row>
                            <div class="mobile-notific-buttons">
                                <el-button color="#626aef">Перейти к олимпиаде</el-button> 
                                <br>
                                <el-button type="danger" plain>Убрать уведомления</el-button>
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
import { ElScrollbar } from 'element-plus'
import { ref } from 'vue'

const calculatePageSize = () => {
    const width = ref(window.innerWidth);
    return width.value;
};

const activeIndex = ref('/user/notifications');

const notifications = NotificationsList()['notifications'];


</script>