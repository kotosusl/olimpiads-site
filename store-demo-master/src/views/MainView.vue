<template>
   <h1>Main</h1>
   <h3>Olimps recomendations</h3>
      <div v-for="(olimpiada, index) in olimps" :key="index" class="olimp-card">
         <el-card class="box-card" shadow="hover">
            <template #header>
               <div class="card-header">
                  <span>{{ olimpiada.name }}</span>
                  <el-button class="button" text>Open olimp</el-button>
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
</style>


<script setup>
import { OlimpList } from '@/store/index.js'

const olimps = OlimpList().Olimps
</script>