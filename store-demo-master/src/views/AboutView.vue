<template>
  <div  v-if="calculatePageSize() > 900">
    <div class="about-body-div"> 
      <nav class="about-nav"> 
          <div class="about-logo-image"><img src="/src/views/imges/Site-Logo.png" alt="Logo" class="logo-image"></div>
          <div class="about-nav-buttons">
            <router-link to="/login"><el-button color="#626aef">Войти</el-button></router-link>
            <router-link to="/register"><el-button color="#626aef">Зарегистрироваться</el-button></router-link>
          </div>
      </nav>
      
      <div class="about-main">
        <div class="about-name"><h1>Олимпик</h1></div>
        <h1 class="about-main-h1"> А ты помнишь,</h1>
        <h1 class="about-main-h1">когда олимпиада?</h1>
        <router-link to="/login"><button class="about-main-button">Войти</button></router-link>
      </div>
      <div class="about-information">
        <div class="step1 steps">
          <div class="step-numbers">
            <h1 class="step-numbers">1</h1>
          </div>
          <div class="step-name-next-info">
            <h1 class="step-name">Зарегистрируйся</h1>
            <p class="step-next-info">на сайте и войди в личный кабинет</p></div>
        </div>
        <div class="step2 steps">
          <div class="step-name-next-info">
            <h1 class="step-name">Выбери олимпиады</h1>
            <p class="step-next-info">в которых будешь участвовать в этом учебном году</p>
          </div>
          <div class="step-numbers"><h1 class="step-numbers">2</h1></div></div>
        <div class="step3 steps">
          <div class="step-numbers">
            <h1 class="step-numbers">3</h1>
          </div>
          <div class="step-name-next-info">
            <h1 class="step-name">Получай уведомления</h1>
            <p class="step-next-info">только там, где ты хочешь их получать</p>
          </div>
        </div>
        <div class="step4 steps">
          <div class="step-name-next-info"><h1 class="step-name">Участвуй и побеждай!</h1></div>
          <div class="step-numbers"><h1 class="step-numbers">4</h1></div></div>
      </div>

      <div class="about-message-places">
        <div class="about-message-places-h1"><h1>Получай уведомления там, где удобно!</h1></div>
        <div class="about-message-places-images">
          <div class="site-image about-image"><img src="/src/views/imges/Site-Logo_png.png" alt="" class="message-places-image"></div>
          <div class="gmail-image about-image"><img src="/src/views/imges/Gmail-Logo.png" alt="" class="message-places-image"></div>
          <div class="telegram-image about-image"><img src="/src/views/imges/Telegram-Logo.png" alt="" class="message-places-image"></div>
          <div class="vk-image about-image"><h1>(В разработке)</h1></div>
        </div>
      </div>
      <div class="before-footer"></div>
    </div>
    <footer>
      <p class="footer-mail">E-mail разработчика: kotosusl@gmail.com</p>
    </footer>
  </div>

  <!-----------Mobile-version-------------->

  <div v-else>
    <div class="about-mobile-body-div"> 
      <nav class="about-mobile-nav">
        <div><img src="/src/views/imges/Site-Logo_png.png" alt="Logo" class="logo-image"></div>
          <div class="about-mobile-nav-buttons">
            <router-link to="/login"><el-button color="#626aef">Войти</el-button></router-link>
          </div>
      </nav>
      <div class="about-mobile-main">
        <div class="about-mobile-name"><h1>Олимпик</h1></div>
        <h1 class="about-mobile-main-h1"> А ты помнишь,</h1>
        <h1 class="about-mobile-main-h1">когда олимпиада?</h1>
        <router-link to="/login"><button class="about-mobile-main-button">Войти</button></router-link>
      </div>
      <div class="about-mobile-information">
        <div class="mobile-step1 mobile-steps">
          <div class="mobile-step-numbers">
            <h1 class="mobile-step-numbers">1</h1>
          </div>
          <div class="mobile-step-name-next-info">
            <h1 class="mobile-step-name">Зарегистрируйся</h1>
            <p class="mobile-step-next-info">на сайте и войди в личный кабинет</p></div>
        </div>
        <div class="mobile-step2 mobile-steps">
          <div class="mobile-step-numbers">
            <h1 class="mobile-step-numbers">2</h1>
          </div>
          <div class="mobile-step-name-next-info">
            <h1 class="mobile-step-name">Выбери олимпиады</h1>
            <p class="mobile-step-next-info">в которых будешь участвовать в этом учебном году</p></div>
          </div>
          
        <div class="mobile-step3 mobile-steps">
          <div class="mobile-step-numbers">
            <h1 class="mobile-step-numbers">3</h1>
          </div>
          <div class="mobile-step-name-next-info">
            <h1 class="mobile-step-name">Получай уведомления</h1>
            <p class="mobile-step-next-info">только там, где ты хочешь их получать</p>
          </div>
        </div>
        <div class="mobile-step4 mobile-steps">
          <div class="mobile-step-numbers"><h1 class="mobile-step-numbers">4</h1></div>
          <div class="mobile-step-name-next-info"><h1 class="mobile-step-name">Участвуй и побеждай!</h1></div></div>
          
      </div>
      <div class="about-mobile-message-places">
        <div class="about-mobile-message-places-h1"><h1>Получай уведомления там, где удобно!</h1></div>
        <div class="about-mobile-message-places-images">
          <el-row>
            <div class="mobile-site-image about-mobile-image"><img src="/src/views/imges/Site-Logo_png.png" alt="" class="mobile-message-places-image"></div>
            <div class="mobile-gmail-image about-mobile-image"><img src="/src/views/imges/Gmail-Logo.png" alt="" class="mobile-message-places-image"></div>
          </el-row>
          <el-row>
            <div class="mobile-telegram-image about-mobile-image"><img src="/src/views/imges/Telegram-Logo.png" alt="" class="mobile-message-places-image"></div>
            <div class="mobile-vk-image about-mobile-image"><h1>(В разработке)</h1></div>
          </el-row>
        </div>
      </div>
      <div class="mobile-before-footer"></div>
    </div>
    <footer class="mobile-footer">
      <p class="footer-mail">E-mail разработчика: kotosusl@gmail.com</p>
    </footer>
  </div>
</template>

<style src="/src/views/AboutView.css"></style>

<script lang="ts" setup>
import { ref } from 'vue'

const calculatePageSize = () => {
    const width = ref(window.innerWidth);
    return width.value;
};
</script>



olimpiks

olympiks

olimpyks

olympyks

olimpics

olympics

olimpycs

olympycs