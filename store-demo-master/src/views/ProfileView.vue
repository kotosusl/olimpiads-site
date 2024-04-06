<template>
    <h1>Profile</h1>
    <el-input v-model="user.name" disabled></el-input>
    <el-input v-model="user.surname" disabled></el-input>
    <el-input v-model="user.school_class" disabled></el-input>
    <el-radio-group v-model="user.male">
          <el-radio value="M" label="M" disabled />
          <el-radio value="F" label="F" disabled />
        </el-radio-group>
    <p v-for="(subject, index) in user.subjects" :key="index" class="profile_subjects">{{ subject }}</p>
    <el-checkbox-group v-model="user.messages_places">
          <el-checkbox value="Mail" label="Mail" name="message_places" disabled/>
          <el-checkbox value="VK" label="VK" name="message_places" disabled />
          <el-checkbox value="Telegram" label="Telegram" name="message_places" disabled />
        </el-checkbox-group>
    <el-button type="primary" @click="myClickHandler">Edit</el-button>
    <el-dialog v-model="dialogVisible" title="Edit profile" width="60%" modal>
       <EditProfileForm @onupdate="onFormUpdate" @oncancel="onFormCancel" />
    </el-dialog>
 </template>
 
 <script setup>
 import { ref, reactive } from 'vue'
 import EditProfileForm from '@/forms/EditProfileFrom.vue'
 import { UserList } from '@/store/UsersData.js'
 
 const user = reactive(UserList().users[0])
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