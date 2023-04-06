<template>
  <div id="app">

    <b-form v-if="age === ''" v-on:submit.prevent="onSubmit" @submit="submit">
      <h3>Enter your Data</h3>
        <b-form-group id="input-group-1" label="Name" label-for="input-1">

          <b-form-input
            id="input-1"
            type="text"
            v-model="dataentry.name"
            placeholder="Name"
          ></b-form-input>
        </b-form-group>
        <b-form-invalid-feedback id="name-validation">
          Name is a required field.
        </b-form-invalid-feedback>
        <b-form-group id="input-group-2" label="Date of birth" label-for="input-2">
          <date-picker class="dob" v-model="dataentry.dob" valueType="format"></date-picker>
        </b-form-group>
      <b-button pill @click="submit" id="button-1" type="submit" variant="dark">Confirm</b-button>

    </b-form>
    <div v-else @goBack="goBack">
      <h3>Thank you for your submission.</h3>
      <br>
      <div class="aftermath">
        <h4> <strong>Name:</strong> {{ dataentry.name }}</h4>
        <h4> <strong>Date of Birth:</strong> {{ dataentry.dob }} </h4>
        <h4 ><strong>Age:</strong> {{ age }} </h4>
      </div>
      <br>
      <b-button pill @click="goBack" id="button-2" class="centered-button" variant="dark">Back</b-button>
    </div>
  </div>
  </template>
  <script>
    import DatePicker from 'vue2-datepicker';
    import 'vue2-datepicker/index.css';
    import axios from 'axios'

  export default{
    components: { DatePicker },
    data() {
      return {
         dataentry:{
          name:"",
          dob: null,
        },
         age: "",
      }
    },
    methods:{
      submit:function(){
        const path = 'http://127.0.0.1:5000/dataentry'
        axios.post(path, {
          name:this.dataentry.name,
          dob:this.dataentry.dob,
          }
        )
         .then(response => {
          console.log("your age:", response.data.age);
          this.age = response.data.age;
          console.log(response);
        })
         .catch(err =>{
          console.log("error");
          console.log(err);
        })
      },
      goBack:function(){
        this.$router.go(0)
      }
    }
  }
  </script>

  <style>
  @import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Castoro&display=swap');
  #app {
    font-family: 'Lato', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }

  .dob {
    width: 100%;
    background-color: pink;
  }

  #input-group-1 {
    margin-left:25%;
    margin-bottom: 20px;
    width: 50%;
    padding-left: 80px;
    margin-top: 50px;
    font-weight:bold;

  }
  h3{
    /* margin-left:40%; */
    margin-top:20px;
    font-family: 'Castoro', serif;
    text-align: center;
  }
  #input-group-2{
    margin-left:25%;
    margin-bottom: 20px;
    width:50%;
    padding-left:80px;

    font-weight:bold;
  }
  #button-1{
  margin-left:50%;
  }

  .centered-button {
    margin: auto;
    display: block;
  }
  .nav-bar{
    padding-left: 50px;;
  }
  .link{
    padding-right:100px;
    font-size: 20px;
    color:white;
  }
  h4 {
    font-size: 16px;
  }
  .aftermath {
  margin: auto;
  padding-left: 45%;
  padding-right: 15%;
  align-items: center;
 /*  display: block; */
  text-align: left;
  line-height: 3;
  }
  </style>
