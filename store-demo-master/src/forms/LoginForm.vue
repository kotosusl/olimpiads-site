<template>
    <el-form
      ref="ruleFormRef"
      :model="ruleForm"
      status-icon
      :rules="rules"
      label-width="120px"
      class="demo-ruleForm"
    >
    <el-form-item label="Login" prop="login">
        <el-input v-model.number="ruleForm.login" />
      </el-form-item>
      <el-form-item label="Password" prop="pass">
        <el-input v-model="ruleForm.pass" type="password" autocomplete="off" />
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
    pass: '',
    login: '',
  })
  
  const rules = reactive<FormRules<typeof ruleForm>>({
    pass: [{ validator: validatePass, trigger: 'blur' }],
    login: [{ validator: checkLogin, trigger: 'blur' }],
  })
  
  const submitForm = (formEl: FormInstance | undefined) => {
    if (!formEl) return
    formEl.validate((valid) => {
      if (valid) {
        console.log('submit!')
      } else {
        console.log('error submit!')
        return false
      }
    })
  }
  </script>
  