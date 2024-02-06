<template>
   <h1>About</h1>
   <el-button type="primary" @click="myClickHandler">About</el-button>
   <el-dialog v-model="dialogVisible" title="Tips" width="60%" modal>
      <TestForm @onupdate="onFormUpdate" @oncancel="onFormCancel" />
   </el-dialog>
</template>

<script setup>
import { ref } from 'vue'
import TestForm from '@/forms/TestForm.vue'

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