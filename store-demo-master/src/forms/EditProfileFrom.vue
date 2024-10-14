<template>
  <div v-if="calculatePageSize() > 800">
    <el-form 
      :model="form_data" 
      label-width="120px">
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
          <el-radio value="M" label="M">Мужской</el-radio>
          <el-radio value="F" label="F">Женский</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="Уведомления">
        <el-checkbox-group v-model="form_data.messages_places" >
          <el-checkbox value="Mail" label="Mail" name="message_places" />
          <el-checkbox value="VK" label="VK" name="message_places" disabled/>
          <el-checkbox value="Telegram" label="Telegram" name="message_places" />
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="@Username">
        <el-input v-model="form_data.telegram_name" />
      </el-form-item>
      <el-form-item label="Предметы">
    <el-select
    v-model="form_data.subjects"
      multiple
      filterable
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
        <!--<el-button @click="onCancel">Отмена</el-button>-->
      </el-form-item>
    </el-form>
  </div>

<!---------------Mobile-version----------------->

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
          <el-radio value="M" label="M">Мужской</el-radio>
            <el-radio value="F" label="F">Женский</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="Уведомления">
        <el-checkbox-group v-model="form_data.messages_places" >
          <el-checkbox value="Mail" label="Mail" name="message_places" />
          <el-checkbox value="VK" label="VK" name="message_places" disabled/>
          <el-checkbox value="Telegram" label="Telegram" name="message_places" />
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="@Username">
        <el-input v-model="form_data.telegram_name" />
      </el-form-item>
      <el-form-item label="Предметы">
    <el-select
    v-model="form_data.subjects"
      multiple
      filterable
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
        <!--<el-button @click="onCancel">Отмена</el-button>-->
      </el-form-item>
    </el-form>
  </div>
  </template>
  
  <script lang="ts" setup>
import { ref, reactive } from 'vue'
import { UserList } from '@/store/UsersData.js'
import { userToken } from '@/store/tokenData';
import router from '@/router';


  const emit = defineEmits(['onsubmit', 'oncancel'])
  
  const calculatePageSize = () => {
    const width = ref(window.innerWidth);
    return width.value;
};


let url = '/api/get_profile_info';
let request_options = {
   method: 'POST',
   headers: {
      Accept: '*/*',
   'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
   'Content-Type': 'application/json',
   'x-access-token': userToken.getters.get_token
},
body: userToken.getters.get_request
}

let form_user = ref({})
let form_data = ref({})

fetch(url, request_options)
.then(res => res.json())
.then(json => {
   if (json['success'] != 'OK') {
      router.push('/login');
      
   } else if (json['success'] == 'OK'){
      form_user.value = json['profile_info'];
      form_data.value.user_id = form_user.value['user_id'];
      form_data.value.name = form_user.value['name'];
      form_data.value.surname = form_user.value['surname'];
      form_data.value.male = form_user.value['male'];
      form_data.value.messages_places = form_user.value['messages_places'];
      form_data.value.school_class = form_user.value['school_class'];
      form_data.value.subjects = form_user.value['subjects'];
      form_data.value.email = form_user.value['email'];
      form_data.value.telegram_name = form_user.value['telegram_name']
      if (form_user.value['name'] == null){
        form_user.value['name'] = 'Имя';
        form_data.value.name = '';
      }
      if (form_user.value['surname'] == null){
        form_user.value['surname'] = 'Фамилия';
        form_data.value.surname = '';
      }
      if (form_user.value['subjects'].length == 0){
        form_user.value['subjects'] = ['Не выбрано'];
        form_data.value.subjects = [];
      }
      if (form_user.value['school_class'] == null){
        form_user.value['school_class'] = 11;

      }
      if (form_user.value['telegram_name'] == null){
        form_user.value = 'Не задано';
        form_data.value.telegram_name = '';
      }
      userToken.commit('set_request', "{}");
   }
})
.catch(err => console.error('error:' + err));
  


  const options = [{value: 'математика', label: 'Математика'}, {value: 'физика', label: 'Физика'}, 
                                                          {value: "информатика", label: 'Информатика'}, {value: "робототехника", label: 'Робототехника'},
                                                          {value: "черчение", label: 'Черчение'}, 
                  {value: 'английский язык', label: 'Английский язык'}, {value: 'русский язык', label: 'Русский язык'}, 
                                                     {value: 'немецкий язык', label: 'Немецкий язык'}, {value: 'французский язык', label: 'Французский язык'}, 
                                                     {value: 'лингвистика', label: 'Лингвистика'}, {value: 'испанский язык', label: 'Испанский язык'}, 
                                                     {value: 'латинский язык', label: 'Латинский язык'}, {value: 'китайский язык', label: 'Китайский язык'},
                                                     {value: 'итальянский язык', label: 'Итальянский язык'}, {value: 'арабский язык', label: 'Арабский язык'},
                                                     {value: 'японский язык', label: 'Японский язык'}, {value: 'корейский язык', label: 'Корейский язык'},
                  {value: 'литература', label: 'Литература'}, {value: 'история', label: 'История'},
                                                               {value: 'обществознание', label: 'Обществознание'}, {value: 'экономика', label: 'Экономика'},
                                                               {value: 'право', label: 'Право'}, {value: 'обществознание', label: 'Обществознание'},
                                                               {value: 'основы предпринимательства', label: 'Основы предпринимательства'},
                                                               {value: 'психология', label: 'Психология'}, {value: 'менеджмент', label: 'Менеджмент'}, 
                  {value: 'биология', label: 'Биология'}, {value: 'география', label: 'География'}, 
                                                           {value: "химия", label: 'Химия'}, {value: 'экология', label: 'Экология'}, {value: 'астрономия', label: 'Астрономия'},
                                                           {value: 'обществознание', label: 'Обществознание'},
                  {value: 'обж', label: 'ОБЖ'}, {value: 'технология', label: 'Технология'},
                                                                    {value: 'искусство', label: 'Искусство'}, {value: 'физкультура', label: 'Физкультура'},
                                                                    {value: 'изо', label: 'ИЗО'}
               ];

function onCancel()
{ 

      form_data.value.user_id = form_user.value['user_id'];
      form_data.value.name = form_user.value['name'];
      form_data.value.surname = form_user.value['surname'];
      form_data.value.male = form_user.value['male'];
      form_data.value.messages_places = form_user.value['message_places'];
      form_data.value.school_class = form_user.value['school_class'];
      form_data.value.subjects = form_user.value['subjects'];
      if (form_user.value['name'] == null){
        form_user.value['name'] = 'Имя';
        form_data.value.name = '';
      }
      if (form_user.value['surname'] == null){
        form_user.value['surname'] = 'Фамилия';
        form_data.value.surname = '';
      }
      if (form_user.value['subjects'].length == 0){
        form_user.value['subjects'] = ['Не выбрано'];
        form_data.value.subjects = [];
      }
      if (form_user.value['school_class'] == null){
        form_user.value['school_class'] = 11;

      }

   emit('oncancel')
}
function onUpdate()
{ 
  let request = JSON.stringify(form_data.value);
      let url = '/api/edit_user_profile';
      let request_options = {
        method: 'POST',
        headers: {
          Accept: '*/*',
          'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
          'Content-Type': 'application/json',
          'x-access-token': userToken.getters.get_token
        },
        body: request
      }

      fetch(url, request_options)
        .then(res => res.json())
        .then(json => {
          if (json['success'] != 'OK'){
            router.push('/login');
          } else {
            userToken.commit('set_reload_page', '/profile')
            router.push('/reload')
          }
        })
        .catch(err => console.error('error:' + err));
      emit('onsubmit', form_user)
      emit('oncancel')
    
}
  </script>
  