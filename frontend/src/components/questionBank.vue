<template>
    <div class="list">
        <div class="topic">
            <div><span>Topic:</span></div>
            <select>
                <option>A</option>
                <option>B</option>
                <option>C</option>
            </select>
        </div>
        <div class="type">
            <div>Type:</div>
            <select>
                <option>Multiple-C</option>
                <option>a</option>
                <option>b</option>
            </select>
        </div>
        <div class="level">
            <div>Level:</div>
            <select>
                <option>Easy</option>
                <option>Medium</option>
                <option>Hard</option>
            </select>
        </div>
        <div class="doc">
            <div>Doc:</div>
            <select>
                <option>Tài liệu 1</option>
                <option>Tài liệu 2</option>
                <option>Tài liệu 3</option>
            </select>
        </div>
        <!--      <QuestionBank-->
        <!--          v-on:change_src_image="change_src_image"-->
        <!--      />-->
         <div class="list-MSSV">
              <select multiple ="multiple" style="width: 70%; margin: 0 auto">
                  <option v-for="item in all_data" :key="item[0]" v-on:dblclick="change_src_image(item)">{{ item[4] }}</option>
              </select>
         </div>
    </div>
   <div class="Image">
        <div class="show-image"><img id="myImage" v-bind:src="link_image"></div>
            <sent-result
                v-bind:isMultiChoice="isMultiChoice"
                v-bind:isLongResponse="isLongResponse"
                v-on:sentResult="sentResult"
            />
   </div>
</template>

<script lang="ts">
import { ref } from 'vue'
import { defineComponent } from '@vue/composition-api'
import SentResult from "@/components/sendResults.vue";
import axios from 'axios'
export default defineComponent({
  name: 'QuestionBank',
  props: {},
  components: {
    SentResult
  },
  setup ( props, { emit }) {
    const isMultiChoice = ref(false)
    const isLongResponse = ref(false)
    const link_image = ref('aa')
    const all_data = ref([1, 4])
    const id_question = ref('0')
    const getdata = async () => {
      await axios.get('http://127.0.0.1:8000/data/').then(rs => {
        all_data.value = JSON.parse(rs.data)
      })
    }
    getdata()
    const change_src_image = (data: any) => {
      const type = data[5]
      if (type === 'multi choice'){
        isMultiChoice.value = true
        isLongResponse.value = false
      }
      if (type === 'long response'){
        isMultiChoice.value = false
        isLongResponse.value = true
      }
      link_image.value =  data[6]
      id_question.value = data[0]
    }

    const sentResult =  async (result: any) => {
      console.log('sentResult', result)
      console.log('http://127.0.0.1:8000/' + '1/' + result + '/' + id_question.value)
      await axios.get('http://127.0.0.1:8000/receive/' + '1/' + result + '/' + id_question.value)
    }

    return {
      id_question,
      getdata,
      all_data,
      link_image,
      change_src_image,
      isMultiChoice,
      isLongResponse,
      sentResult
    }
  }
})
</script>

<style>
.Image{
  width: 77.8%;
  height: 100vh;
  background-color: #fff;
}

.Image .show-image{
  width: 100%;
  height: 100vh;
  position: relative;
  /*background-color: red;*/
  float: left;
}

#myImage{
  width:75%;
  max-height: 80vh;
  position: absolute;
  top: 45%;
  left: 50%;
  transform: translate(-50%, -50%);
    /*margin: 0 auto;*/
}
.Image .sentResult{
  width: 100%;
  height: 10vh;
  display: block;
  position: absolute;
  bottom: -10%;
  /*flex-direction: column-reverse;*/

  /*justify-content: center;*/
  /*align-items: center;*/
}
</style>
