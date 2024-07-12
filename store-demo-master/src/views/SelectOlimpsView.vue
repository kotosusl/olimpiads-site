<template>
<h1>Select olimps</h1>
   <h3>Finding</h3>
   <el-input v-model="input_serch" placeholder="Please input" clearable class="inputs words"/>
   <el-button type="primary" :icon="Search" @click="onSearch">Search</el-button>
      <div v-for="(olimpiada, index) in olimps" :key="index" class="olimp-card">
         <el-card class="box-card" shadow="hover">
            <template #header>
               <div class="card-header">
                  <span>{{ olimpiada.name }}</span>
                  <el-button class="button" text><router-link to="/one_olimp">Open olimp</router-link></el-button>
                  <el-button class="button" text @click="deleteNotification">Delete olimp notification</el-button>

               </div>
            </template>
            <p>{{ Math.min(...olimpiada.olimp_classes) }}-{{ Math.max(...olimpiada.olimp_classes) }} class</p>
            <div class="subject-box">
            <div v-for="i in olimpiada.subjects" :key="i" class="text-item">{{ i }}</div>
            </div>
            <p>{{ olimpiada.description }}</p>
            
            <template #footer>Footer content</template>
         </el-card>
   </div>
   
</template>

<style>
.subject-box{
   display: flex;
   justify-content: flex-start;
}
.text-item{
   margin: 5px;
}
.olimp-card{
   margin: 1%;
}
.inputs{
   margin: 5px;
}
.words{
   width: 700px;
}
</style>


<script setup>
import { OlimpList } from '@/store/index.js'
import { ref } from 'vue'
const emit = defineEmits(['onsearch', 'ondeletenotification'])
const input_serch = ref('')
// import user olimps
const olimps = OlimpList().Olimps


function onSearch(){
   // input_search 
   emit('onsearch')

}

function deleteNotification()
{
   emit('ondeletenotification')
   // delete olimp_name in user_olimps
}
</script>