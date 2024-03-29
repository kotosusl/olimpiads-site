<template>
   <h1>{{ one_olimp.name }}</h1>
   <p>{{ Math.min(...one_olimp.olimp_classes) }}-{{ Math.max(...one_olimp.olimp_classes) }} class</p>
   <div class="subject-box">
        <div v-for="i in one_olimp.subjects" :key="i" class="text-item">{{ i }}</div>
    </div>
   <h3>{{ one_olimp.description }}</h3>
</template>

<style>
.subject-box{
   display: flex;
   justify-content: flex-start;
}
.text-item{
   margin: 5px;
}
</style>

<script setup>
import { OlimpList } from '@/store/index.js'

const one_olimp = OlimpList().olimps[0]
</script>
