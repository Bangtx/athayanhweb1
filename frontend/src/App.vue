<template>
  <div>
    <Base/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from '@vue/composition-api'
import Base from "@/components/base.vue"

export default defineComponent({
  components: {
    Base
  }
})
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
*{
    margin: 0;
    box-sizing: border-box;
}
.crossbar-header{
    -webkit-app-region: drag;
    background: #464775;
    height: 3.3rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: #fff;
}
.waffle-header{
    width: 16%;
}
.waffle-header button{
    height: 3.3rem;
    width: 65px;
    background-color: #464775;
    border: none;
}
.ts-waffle-button i{
    color: white;
    font-size: 20px;
}
.ts-waffle-button:hover{
    background-color: #7d7ebe;
}
.waffle-header span{
    padding-left: 19px;
    font-size: 23px;
    font-weight: bold;
}
.crossbar-header .search{
    width: 60%;
    position: relative;
}

.search input{
    width: 70%;
    height: 30px;
    border: none;
    font-size: 10pt;
    float: left;
    color: #63717f;
    padding-left: 45px;
    padding-right: 20px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
    padding-left: 30px;
    border-radius: 2px;
}
.search i{
    position: absolute;
    top: 9px;
    left: 8px;
    font-size: 15px;
    color: rgba(0, 0, 0, 0.568);
}
.crossbar-header .powerbar-profile{
    width: 15%;
    display: flex;
    text-align: right;
}
.powerbar-profile a{
    text-decoration: none;
    color: white;
    /* padding-left: 10px; */
}
.powerbar-profile .powerbar{
    padding: 35px 10px;
    font-size: 13px;
    width: 40%;
}
.powerbar-profile .profile{
    width: 60%;
    padding: 25px 0px 25px 0px;
    border-radius: 50%;
}
.powerbar i:hover{
    transform: scale(1.3);
    transition: 0.7s;
}
.profile:hover{
    transform: scale(1.3);
    transition: 0.7s;
}
.powerbar-profile button{
    height: 70px;
    width: 65px;
    background-color: #464775;
    border: none;
}
.powerbar-profile button image{
    padding-top: 3px;
}
.powerbar-profile button:hover{
    background-color: #8889c0;
}
.body{
    height: 100vh;
    display: flex;
}
.menu{
    width: 5.2%;
    height: 100vh;
    position: relative;
    background-color: #efefef;
}
.menu a{
    text-decoration: none;
    width: 100%;
}
/* .menu i:hover{
    transform: scale(1.2);
} */
.menu button:hover{
    background-color: #8889c0;
}
.menu i{
    font-size: 19px;
    padding-bottom: 3px;
}
.menu button{
    height: 8vh;
    width: 100%;
    text-align: center;
    border: none;
    font-size: 13px;
    overflow: hidden;
    /*position: absolute;*/
}
.body .list{
    width: 16%;
    padding-left: 5px;
    color: darkblue;
    background-color: #f5f5f5;
    box-shadow: -5px 0 10px #8080802e;
    padding-top: 15px;
}
/*.list .topic{*/
/*    padding-bottom: 15px;*/
/*    width: 100%;*/
/*}*/
/*.topic div{*/
/*    padding-right: 8px;*/
/*    width: 40%;*/
/*    height: 100%;*/
/*    font-size: 25px;*/
/*    float: left;*/
/*}*/

/*.topic select{*/
/*    width: 50%;*/
/*    margin-left: 5%;*/
/*    height: 100%;*/
/*}*/
.list {
    width: 100%;
}

.list div{
    float: left;
    padding-bottom: 15px;
    width: 100%;
}
.list div div{
    padding-right: 8px;
    width: 40%;
    height: 100%;
    font-size: 25px;
    float: left;
}
.list div select{
    width: 50%;
    margin-left: 5%;
    height: 100%;
}
.list .level{
    padding-bottom: 15px;
}
/*.level div{*/
/*    padding-right: 8px;*/
/*    font-size: 25px;*/
/*}*/
/*.level select{*/
/*    width: 115px;*/
/*}*/
.list .doc{
    padding-bottom: 15px;
}
/*.doc span{*/
/*    padding-right: 22px;*/
/*    font-size: 25px;*/
/*}*/
.doc select{
    width: 116px;
}
.list .list-MSSV{
    /* padding: 7% 0 0 15%; */
    /* width: 150px; */
    text-align: center;
    width: 100%;
    height: 60vh;
}
.list-MSSV select{
  width: 80%;
  margin: 0 auto;
}
select{
    font-size: 19px;
}
#info{
    width: 380px;
    height: 140px;
    background-color: #70809012;
    display: none;
    transition: 1s;
}
#info .header-info{
    width: 100%;
    display: flex;
}
#info .header-info .left{
    width: 30%;
}
#info .header-info .left .image-info{
    width: 55px;
    border-radius: 50%;
    margin: 10px 0 0 30px;
}
#info div.header-info .right{
    width: 70%;
    margin-top: 17px;
    margin-left: -10px;
}
#info .contact-icons{
    width: 100%;
    margin-left: 11px;
    margin-top: 10px;
}
.contact-icons i{
    padding-left: 17px;
}

input[type="file"] {
    display: block;
}
.imageThumb {
    max-height: 75px;
    border: 2px solid;
    padding: 1px;
    cursor: pointer;
}
.pip {
    display: inline-block;
    margin: 10px 10px 0 0;
}
.remove {
    display: block;
    background: #444;
    border: 1px solid black;
    color: white;
    text-align: center;
    cursor: pointer;
}
.remove:hover {
    background: white;
    color: black;
}
.Image{
    width: 77.8%;
    height: 100vh;

    background-color: #fff;
}

#myImage{
    display: none;
    width:600px;
    height: 380px;
    margin: 140px auto;
}

/* sign in */

.sign-in{
    text-align: center;
    width: 315px;
    height: 420px;
    border: 1px solid #228be6;
    border-radius: 5px;
    margin: 0 auto;
}
.title h2{
    color: #000000db;
    padding-top: 10px;
}
.title h4{
    color: #228be6;
    padding-top: 5px;
}
.sign-in p{
    padding: 10px 0 4px 65px;
    float: left;
    font-size: 16px;
}
.sign-in input{
    border-radius: 5px;
    height: 35px;
    width: 205px;
    border-color: #dee2e6;
    box-shadow: inset 0 5px 5px 0 rgb(0 0 0 / 8%);
}
.sign-in .forget{
    float: right;
    padding-right: 30px;
    text-decoration: none;
}
.sign-in button{
    border-radius: 30px;
    width: 205px;
    border: none;
    height: 40px;
    background-color: #228be6;
    color: white;
    font-size: 16px;
}
</style>
