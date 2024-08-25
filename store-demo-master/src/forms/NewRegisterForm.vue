<template>
    <div  v-if="calculatePageSize() > 800">
        <div class="body-div">
          <router-link to="/about" ><div class="register-back-button-div" @click="registerBackButtonClick()"><img src="/src/views/imges/arrow_left.png" alt="" class="register-back-button"></div></router-link>
            <div class="container">
                <div class="form-container sign-up">
                <el-form
                ref="ruleFormRef"
                :model="ruleForm"
                status-icon
                :rules="rules"
                class="demo-ruleForm">
                    <h1>Регистрация</h1>
                    <br>
                    <el-form-item prop="email">
                        <el-input  v-model="ruleForm.email" type="email" placeholder="Email" maxlength="50"/>
                    </el-form-item>
                    <el-form-item prop="password">
                        <el-input type="password" placeholder="Пароль" v-model="ruleForm.password" maxlength="50"/>
                    </el-form-item>
                    <el-form-item prop="checkPass">
                        <el-input type="password" placeholder="Поввтор пароля" v-model="ruleForm.checkPass" maxlength="50"/>
                    </el-form-item>
                    <el-form-item>
                        <el-button color="#626aef" @click="submitForm(ruleFormRef)">Зарегистрироваться</el-button>
                    </el-form-item>
                </el-form>
            </div>
            <div class="toggle-container">
                <div class="toggle">
                    <div class="toggle-panel toggle-left">
                        <h1>Уже был на сайте?</h1>
                        <p>войди в свой аккаунт</p>
                        <router-link to="/login"><el-button color="#626aef" class="hidden" id="login">Войти</el-button></router-link>
                    </div>
                </div>
            </div>
            </div>
        </div>
    </div>

<!-------------------Mobile-version--------------------->

    <div v-else>
        <div class="mobile-body-div">
          <router-link to="/about"><div class="mobile-register-back-button-div" @click="registerBackButtonClick()"><img src="/src/views/imges/arrow_left.png" alt="" class="mobile-register-back-button"></div></router-link>
            <div class="mobile-container">
            <div class="mobile-form-container mobile-sign-up">
                <el-form
                ref="ruleFormRef"
                :model="ruleForm"
                status-icon
                :rules="rules"
                class="demo-ruleForm">
                    <h1>Регистрация</h1>
                    <br>
                    <el-form-item prop="email">
                        <el-input  v-model="ruleForm.email" type="email" placeholder="Email" />
                    </el-form-item>
                    <el-form-item prop="password">
                        <el-input type="password" placeholder="Пароль" v-model="ruleForm.password" />
                    </el-form-item>
                    <el-form-item prop="checkPass">
                        <el-input type="password" placeholder="Поввтор пароля" v-model="ruleForm.checkPass"/>
                    </el-form-item>
                    <el-form-item>
                        <el-button color="#626aef" @click="submitForm(ruleFormRef)">Зарегистрироваться</el-button>
                    </el-form-item>
                </el-form>
            </div>
            

            </div>
            <div class="mobile-to-login">
                <span><b>Уже есть аккаунт?</b></span>
                <router-link to="/login"><el-button color="#626aef">Войти</el-button></router-link>
            </div>
        </div>
    </div>
</template>


<script lang="ts" setup>
import { reactive, ref } from 'vue'
import type { FormInstance, FormRules } from 'element-plus'
import { ElMessage } from 'element-plus'

const calculatePageSize = () => {
    const width = ref(window.innerWidth);
    return width.value;
};

const ruleForm = reactive({
  password: '',
  checkPass: '',
  email: '',
})

const ruleFormRef = ref<FormInstance>()

const checkMail = (rule: any, value: any, callback: any) => {
  if (!value) {
    callback(new Error('Укажите email'))
  } else {
    callback()
  }
}

const validatePass = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('Введите пароль'))
  } else {
    if (ruleForm.checkPass !== '') {
      if (!ruleFormRef.value) return
      ruleFormRef.value.validateField('checkPass', () => null)
    }
    callback()
  }
}
const validatePass2 = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('Повторите пароль'))
  } else if (value !== ruleForm.password) {
    callback(new Error("Пароли не совпадают!"))
  } else {
    callback()
  }
}



const rules = reactive<FormRules<typeof ruleForm>>({
  password: [{ validator: validatePass, trigger: 'blur' }],
  checkPass: [{ validator: validatePass2, trigger: 'blur' }],
  email: [{ validator: checkMail, trigger: 'blur' }],
})

const response = reactive({'success': ''});

const errorMessage = () => {
  ElMessage({
    showClose: true,
    message: response['success'],
    type: 'error',
    duration: 10000
  })
}

const successMessage = () => {
  ElMessage({
    showClose: true,
    message: 'Пользователь успешно зарегистрирован',
    type: 'success',
    duration: 10000
  })
}

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.validate((valid) => {
    if (valid) {
      let request = JSON.stringify(ruleForm);

      let url = '/api/add_user';

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
        .then(json => {
          response['success'] = json['success'];
          if (response['success'] != 'OK' && response['success'] != '') {
            errorMessage();
          } else if (response['success'] == 'OK'){
            successMessage();
            ruleForm.password = '';
            ruleForm.email = '';
            ruleForm.checkPass = '';
          }
        })
        .catch(err => console.error('error:' + err));
      
      
      

    } else {
      console.log('form is empty')
      return false
    }
  })
  
}

function registerBackButtonClick() {
  ruleForm.email = '';
  ruleForm.checkPass = '';
  ruleForm.password = '';
}

</script>


<style src="/src/forms/NewRegisterForm.css"></style>

