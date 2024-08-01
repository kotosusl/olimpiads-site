<template>
  <div v-if="calculatePageSize() > 800">
    <el-form :model="form_data" label-width="120px">
      <el-form-item label="Фамилия">
        <el-input v-model="form_data.surname" />
      </el-form-item>
      <el-form-item label="Имя">
        <el-input v-model="form_data.name" />
      </el-form-item>
      <el-form-item label="Класс">
        <el-select v-model="form_data.school_class" placeholder="">
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
        <el-form-item label="Пол">
        <el-radio-group v-model="form_data.male">
          <el-radio value="M" label="M" />
          <el-radio value="F" label="F" />
        </el-radio-group>
      </el-form-item>
      <el-form-item label="Уведомления">
        <el-checkbox-group v-model="form_data.messages_places" >
          <el-checkbox value="Mail" label="Mail" name="message_places" />
          <el-checkbox value="VK" label="VK" name="message_places" disabled/>
          <el-checkbox value="Telegram" label="Telegram" name="message_places" />
        </el-checkbox-group>
      </el-form-item>
      
      <el-form-item label="Предметы">
    <el-select
    v-model="form_data.subjects"
      multiple
      collapse-tags
      collapse-tags-tooltip
      :max-collapse-tags="3"
      placeholder="Интересующие предметы"
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
        <el-button type="primary" color="#626aef" @click="onUpdate">Сохранить</el-button>
        <el-button @click="onCancel">Отмена</el-button>
      </el-form-item>
    </el-form>
  </div>

  <div v-else>
    <el-form :model="form_data" label-width="120px" label-position="top">
      <el-form-item label="Фамилия">
        <el-input v-model="form_data.surname" />
      </el-form-item>
      <el-form-item label="Имя">
        <el-input v-model="form_data.name" />
      </el-form-item>
      <el-form-item label="Класс">
        <el-select v-model="form_data.school_class" placeholder="">
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
        <el-form-item label="Пол">
        <el-radio-group v-model="form_data.male">
          <el-radio label="M">Мужской</el-radio>
            <el-radio label="F">Женский</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="Уведомления">
        <el-checkbox-group v-model="form_data.messages_places" >
          <el-checkbox value="Mail" label="Mail" name="message_places" />
          <el-checkbox value="VK" label="VK" name="message_places" disabled/>
          <el-checkbox value="Telegram" label="Telegram" name="message_places" />
        </el-checkbox-group>
      </el-form-item>
      
      <el-form-item label="Предметы">
    <el-select
    v-model="form_data.subjects"
      multiple
      collapse-tags
      collapse-tags-tooltip
      :max-collapse-tags="3"
      placeholder="Интересующие предметы"
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
        <el-button type="primary" color="#626aef" @click="onUpdate">Сохранить</el-button>
        <el-button @click="onCancel">Отмена</el-button>
      </el-form-item>
    </el-form>
  </div>
  </template>
  
  <script lang="ts" setup>
   import { ref, reactive } from 'vue'
  import { UserList } from '@/store/UsersData.js'
  const emit = defineEmits(['onsubmit', 'oncancel'])
  
  const calculatePageSize = () => {
    const width = ref(window.innerWidth);
    return width.value;
};


  let form_user = reactive(UserList().users[0]);
  
let form_data = reactive({
   user_id: form_user.user_id,
   name: form_user.name,
   surname: form_user.surname,
   male: form_user.male,
   school_class: form_user.school_class,
   subjects: form_user.subjects,
   messages_places: form_user.messages_places
 })



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
function onCancel()
{ 
  form_user = reactive(UserList().users[0]);
  form_data.name = form_user.name;
  form_data.surname = form_user.surname;
  form_data.male = form_user.male;
  form_data.subjects = form_user.subjects;
  form_data.school_class = form_user.school_class;
  form_data.user_id = form_user.user_id;
  form_data.messages_places = form_user.messages_places;

   emit('oncancel')
}
function onUpdate()
{ 
   UserList().users[0].name = form_data.name;
   UserList().users[0].surname = form_data.surname;
   UserList().users[0].male = form_data.male;
   UserList().users[0].subjects = form_data.subjects;
   UserList().users[0].school_class = form_data.school_class;
   UserList().users[0].user_id = form_data.user_id;
   UserList().users[0].messages_places = form_data.messages_places;

   console.log('submit!')
   emit('onsubmit', form_user)
   emit('oncancel')
}
  </script>
  