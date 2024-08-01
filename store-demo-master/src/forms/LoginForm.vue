<template>
    
    <el-form
      ref="ruleFormRef"
      :model="ruleForm"
      status-icon
      :rules="rules"
      label-width="120px"
      class="demo-ruleForm"
    >
    <el-form-item label="Почта" prop="email">
        <el-input v-model.number="ruleForm.email" />
      </el-form-item>
      <el-form-item label="Пароль" prop="password">
        <el-input v-model="ruleForm.password" type="password" autocomplete="off" />
      </el-form-item>
      
      <el-form-item>
        <el-button type="primary" @click="submitForm(ruleFormRef)">Submit</el-button>
      </el-form-item>
    </el-form>
  </template>
  
  <script lang="ts" setup>
  import { reactive, ref } from 'vue'
  import type { FormInstance, FormRules } from 'element-plus'
  
  const ruleFormRef = ref<FormInstance>()
  
  const checkLogin = (rule: any, value: any, callback: any) => {
    if (!value) {
      return callback(new Error('Please input the mail'))
    }
    setTimeout(() => {
      if (value === 0) {
        callback(new Error('Please input latters'))
      } else {
        callback()
      }
    }, 1000)
  }
  
  const validatePass = (rule: any, value: any, callback: any) => {
    if (value === '') {
      callback(new Error('Please input the password'))
    } else {
      callback()
    }
  }
  
  const ruleForm = reactive({
    password: '',
    email: '',
  })
  
  const rules = reactive<FormRules<typeof ruleForm>>({
    password: [{ validator: validatePass, trigger: 'blur' }],
    email: [{ validator: checkLogin, trigger: 'blur' }],
  })
  
  const submitForm = (formEl: FormInstance | undefined) => {
    if (!formEl) return
    formEl.validate((valid) => {
      if (valid) {
        console.log('submit!')
        let reqest = JSON.stringify(ruleForm)
        var axios = require("axios").default;

        var options = {
          method: 'POST',
          url: 'http://localhost:8888/api/login',
          headers: {
            Accept: '*/*',
            'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
            'Content-Type': 'application/json'
          },
          data: {email: ruleForm['email'], password: ruleForm['password']}
        };

        axios.request(options).then(function (response) {
          console.log(response.data);
        }).catch(function (error) {
          console.error(error);
        });
      } else {
        console.log('error submit!')
        return false
      }
    })
  }
  </script>
  