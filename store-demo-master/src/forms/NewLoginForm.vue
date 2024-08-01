<template>
    <div v-if="calculatePageSize() > 800">
    <div class="body-div">
      <router-link to="/about"><div class="login-back-button-div"><img src="/src/views/imges/arrow_left.png" alt="" class="login-back-button"></div></router-link>
        <div class="container" id="container">
        <div class="form-container sign-in">
            <el-form
                ref="ruleFormRef"
                :model="ruleForm"
                status-icon
                :rules="rules"
                class="demo-ruleForm"
            >
                <h1>Вход</h1>
                <el-form-item prop="email">
                    <el-input v-model.number="ruleForm.email" type="email" placeholder="Email" />
                </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password" placeholder="Пароль" v-model="ruleForm.password" autocomplete="off" />
                </el-form-item>
                <el-form-item>
                    <el-button @click="submitForm(ruleFormRef)">Войти</el-button>
                </el-form-item>
                </el-form>
        </div>
        <div class="toggle-container2">
            <div class="toggle2">
                <div class="toggle-panel2 toggle-left">
                    <h1>На сайте впервые?</h1>
                    <router-link to="/register"><el-button color="#626aef" class="hidden" id="register">Зарегистрироваться</el-button></router-link>
                </div>
            </div>
        </div>
    </div>
    </div>
</div>

<!-----------------Mobile-version---------------------->

<div v-else>
    <div class="mobile-body-div">
      <router-link to="/about"><div class="mobile-login-back-button-div"><img src="/src/views/imges/arrow_left.png" alt="" class="mobile-login-back-button"></div></router-link>
            <div class="mobile-container">
            <div class="mobile-form-container mobile-sign-in">
                <el-form
                ref="ruleFormRef"
                :model="ruleForm"
                status-icon
                :rules="rules"
                class="demo-ruleForm">
                    <h1>Вход</h1>
                    <br>
                    <el-form-item prop="email">
                        <el-input v-model.number="ruleForm.email" type="email" placeholder="Email" />
                    </el-form-item>
                    <el-form-item prop="password">
                    <el-input type="password" placeholder="Пароль" v-model="ruleForm.password" autocomplete="off" />
                    </el-form-item>
                    <el-form-item>
                        <el-button color="#626aef" @click="submitForm(ruleFormRef)">Войти</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </div>
        <div class="mobile-to-register">
            <span><b>Впервые на сайте?</b></span>
                <router-link to="/register"><el-button color="#626aef">Зарегистрироваться</el-button></router-link>
        </div>
    </div>
</div>
</template>

<style src="/src/forms/NewLoginForm.css"></style>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import type { FormInstance, FormRules } from 'element-plus'

const calculatePageSize = () => {
    const width = ref(window.innerWidth);
    return width.value;
};

const ruleFormRef = ref<FormInstance>()
  
  const checkLogin = (rule: any, value: any, callback: any) => {
    if (!value) {
      return callback(new Error('Укажите email'))
    } else {
        callback()
    }
  }
  
  const validatePass = (rule: any, value: any, callback: any) => {
    if (value === '') {
      callback(new Error('Введите пароль'))
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
        console.log('submit!');
        let request = JSON.stringify(ruleForm);
        let url = '/api/login';

        let options = {
            method: 'POST',
            headers: {
            Accept: '*/*',
            'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
            'Content-Type': 'application/json'
            },
            body: request
        };

        fetch(url, options)
            .then(res => res.json())
            .then(json => console.log(json))
            .catch(err => console.error('error:' + err));

      } else {
        console.log('error submit!')
        return false
      }
    })
  }
</script>
