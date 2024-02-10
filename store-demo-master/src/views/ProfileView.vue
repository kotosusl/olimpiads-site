<template>
    <h1>Profile</h1>
    
    <el-button type="primary" @click="myClickHandler">Edit</el-button>
    <el-dialog v-model="dialogVisible" title="Edit profile" width="60%" modal>
       <EditProfileForm @onupdate="onFormUpdate" @oncancel="onFormCancel" />
    </el-dialog>
 </template>
 
 <script setup>
 import { ref } from 'vue'
 import EditProfileForm from '@/forms/EditProfileFrom.vue'
 
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