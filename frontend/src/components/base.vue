<template>
  <body class="container">
      <header>
          <div class="crossbar-header">
              <div class="waffle-header">
                  <a href="#"><button class="ts-waffle-button"><i class="fas fa-bars"></i></button></a>
                  <span>Anh Nguyen</span>
              </div>
              <div class="search">
                  <i class="fas fa-search"></i>
                  <input type="text" placeholder="Search">
              </div>
              <div class="powerbar-profile">
                  <a href="#"><p class="powerbar"><i class="fas fa-ellipsis-h"></i></p></a>
                  <a href="#"><button><img class="profile" src="image/profile.jpg" alt="profile"></button></a>
              </div>
          </div>
      </header>
      <section class="body">
          <div class="menu">
              <a href="#"><button><i class="far fa-list-alt"></i><br>Question Bank</button></a>
              <a href="#"><button><i class="fas fa-comment-dots"></i><br>Chat</button></a>
              <a href="#"><button><i class="fas fa-users"></i><br>Group</button></a>
              <a href="#"><button><i class="fas fa-phone-alt"></i><br>Call</button></a>
              <a href="#"><button><i class="fas fa-tv"></i><br>Stream</button></a>
              <a href="#"><button><i class="far fa-file"></i><br>Foler</button></a>
              <a href="#"><button><i class="fas fa-ellipsis-h"></i></button></a>
              <a href="#"><button style=" margin-top: 16vh;"><i class="fab fa-buromobelexperte"></i><br>App</button></a>
              <a href="#"><button><i class="far fa-question-circle"></i><br>Help</button></a>
          </div>
        <question-bank/>
      </section>
</body>
</template>

<script lang="ts">
import { defineComponent } from '@vue/composition-api'
import { ref } from "vue"
import axios from 'axios'
import QuestionBank from "@/components/questionBank.vue";
// import SentResult from "@/components/sendResults.vue";
export default defineComponent({
  name: 'Base',
  components: {
    // /SentResult,
    QuestionBank
  }
})
</script>

<style>

</style>
