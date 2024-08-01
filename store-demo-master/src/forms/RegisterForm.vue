<template>
  <el-form
    ref="ruleFormRef"
    :model="ruleForm"
    status-icon
    :rules="rules"
    label-width="120px"
    class="demo-ruleForm"
  >
  <el-form-item label="Login" prop="email">
      <el-input v-model="ruleForm.email" type="mail" autocomplete="off" />
  </el-form-item>
    <el-form-item label="Password" prop="password">
      <el-input v-model="ruleForm.password" type="password" autocomplete="off" />
    </el-form-item>
    <el-form-item label="Confirm" prop="checkPass">
      <el-input
        v-model="ruleForm.checkPass"
        type="password"
        autocomplete="off"
      />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm(ruleFormRef)"
        >Submit</el-button
      >
    </el-form-item>
  </el-form>



  <el-form
                ref="ruleFormRef"
                :model="ruleForm"
                status-icon
                :rules="rules"
                class="demo-ruleForm">
                    <h1>Зарегистрироваться</h1>
                    <span>и получать уведомления о проведении олимпиад</span>
                    <el-form-item prop="email">
                        <el-input  v-model="ruleForm.email" type="email" placeholder="Email" />
                    </el-form-item>
                    <el-form-input prop="password">
                        <el-input type="password" placeholder="Пароль" v-model="ruleForm.password" />
                    </el-form-input>
                    <el-form-input prop="checkPass">
                        <el-input type="text" placeholder="Поввтор пароля" v-model="ruleForm.checkPass"/>
                    </el-form-input>
                    <el-form-input>
                        <el-button color="#626aef" @click="submitForm(ruleFormRef)">Зарегистрироваться</el-button>
                    </el-form-input>
                </el-form>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import type { FormInstance, FormRules } from 'element-plus'

const ruleForm = reactive({
  password: '',
  checkPass: '',
  email: '',
})

const ruleFormRef = ref<FormInstance>()

const checkMail = (rule: any, value: any, callback: any) => {
  if (!value) {
    callback(new Error('Please input the mail'))
  } else {
    callback()
  }
}

const validatePass = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('Please input the password'))
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
    callback(new Error('Please input the password again'))
  } else if (value !== ruleForm.password) {
    callback(new Error("Two inputs don't match!"))
  } else {
    callback()
  }
}



const rules = reactive<FormRules<typeof ruleForm>>({
  password: [{ validator: validatePass, trigger: 'blur' }],
  checkPass: [{ validator: validatePass2, trigger: 'blur' }],
  email: [{ validator: checkMail, trigger: 'blur' }],
})

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.validate((valid) => {
    if (valid) {
      console.log('submit!')
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
        .then(json => console.log(json))
        .catch(err => console.error('error:' + err));

    
    } else {
      console.log('error submit!')
      return false
    }
  })
  
}
</script>
