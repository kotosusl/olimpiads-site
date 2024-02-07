<template>
    <el-form :model="form" label-width="120px">
      <el-form-item label="Name">
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item label="Surname">
        <el-input v-model="form.surname" />
      </el-form-item>
      <el-form-item label="Otchestvo">
        <el-input v-model="form.otchestvo" />
      </el-form-item>
      <el-form-item label="shcool_class">
        <el-select v-model="form.shcool_class" placeholder="">
          <el-option label="1" value="1" />
          <el-option label="2" value="2" />
          <el-option label="3" value="3" />
          <el-option label="4" value="4" />
          <el-option label="5" value="5" />
          <el-option label="6" value="6" />
          <el-option label="7" value="7" />
          <el-option label="8" value="8" />
          <el-option label="9" value="9" />
          <el-option label="10" value="10" />
          <el-option label="11" value="11" />
        </el-select>
        </el-form-item>
        <el-form-item label="male/female">
        <el-radio-group v-model="form.resource">
          <el-radio label="M" />
          <el-radio label="F" />
        </el-radio-group>
      </el-form-item>
      <el-form-item label="Message places">
        <el-checkbox-group v-model="form.type">
          <el-checkbox label="Mail" name="message_places" />
          <el-checkbox label="VK" name="message_places" />
          <el-checkbox label="Telegram" name="message_places" />
        </el-checkbox-group>
      </el-form-item>
      
      <el-form-item>
    <el-select
      v-model="value4"
      multiple
      collapse-tags
      collapse-tags-tooltip
      :max-collapse-tags="3"
      placeholder="Subjects"
      style="width: 240px"
    >
    
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value"
      />
    </el-select>
  </el-form-item>
      <el-form-item>
        <br>
        <el-button type="primary" @click="onSubmit">Create</el-button>
        <el-button>Cancel</el-button>
      </el-form-item>
    </el-form>
  </template>
  
  <script lang="ts" setup>
  import { reactive } from 'vue'
  import { ref } from 'vue'
  
  // do not use same name with ref
  const form = reactive({
    name: '',
    shcool_class: '',
    date1: '',
    date2: '',
    delivery: false,
    type: [],
    resource: '',
    desc: '',
    otchestvo: '',
    surname: '',
  })
  
  const onSubmit = () => {
    console.log('submit!')
  }
  const value4 = ref([])
  const options = [
  {
    value: 'Math',
    label: 'Math',
  },
  {
    value: 'Physics',
    label: 'Physics',
  },
  {
    value: 'English',
    label: 'English',
  },
  {
    value: 'Informatics',
    label: 'Informatics',
  },
  {
    value: 'Spanish',
    label: 'Spanish',
  },
]
  </script>
  