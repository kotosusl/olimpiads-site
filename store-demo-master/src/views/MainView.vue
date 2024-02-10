<template>
   <h1>Main</h1>
   <h3>Finding</h3>
   <el-input v-model="input" placeholder="Please input" clearable class="inputs words"/>
   <el-cascader :options="options" :show-all-levels="false" class="inputs" />
   <el-button type="primary" :icon="Search">Search</el-button>
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
const input = ref('')
const olimps = OlimpList().Olimps

const options = [
    {
      value: 'shcool_class',
      label: 'Class',
      children: [
        {value: '1', label: '1'}, {value: '2', label: '2'}, {value: '3', label: '3'}, {value: '4', label: '4'}, {value: '5', label: '5'},
        {value: '6', label: '6'}, {value: '7', label: '7'}, {value: '8', label: '8'}, {value: '9', label: '9'}, {value: '10', label: '10'},
        {value: '11', label: '11'}]},
    {
        value: 'subjects',
        label: 'Subjects',
        children: [
            {value: 'technical', label: 'Technical', children: [{value: 'math', label: 'Math'}, {value: 'physics', label: 'Physics'}]}, 
            {value: 'lingvist', label: 'Lingvist', children: [{value: 'english', label: 'English'}, {value: 'spanish', label: 'Spanish'}]},
            {value: 'humanitar', label: 'Humanitar', children: [{value: 'literature', label: 'Literature'}, {value: 'history', label: 'History'}]}, 
            {value: 'bio', label: 'Bio', children: [{value: 'biology', label: 'Biology'}, {value: 'geography', label: 'Geography'}]}
          ],
        },
      ]
</script>