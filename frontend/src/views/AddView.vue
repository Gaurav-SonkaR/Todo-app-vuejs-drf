<template>
  <div>
    <h1>Add Task</h1>
    <form @submit.prevent="add">
      <label for="title">Title : </label>
      <input type="text" v-model="title" placeholder="Title" required />
      <label for="description">Description : </label>
      <input type="text" v-model="description" placeholder="Description"  />
      <button type="submit">Add</button>
    </form>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  data(){
    return{
      title: '',
      description: ''
    }
  },
  methods:{
    add(){
        axios.post('http://127.0.0.1:8000/api/task-create/', {
          title:this.title,
          description: this.description,
        }).then(response => {
          this.title = '';
          this.description = '';
          alert('Task added successfully');
        }).catch(error => {
          alert('An error occurred while adding the task');
        });
    }
  }
}
</script>

<style scoped>
form{
  display: flex;
  flex-direction: column;
  width: 50%;
  margin: 0 auto;
}
label{
  margin: 0.5rem 0;
}
input{
  margin: 0.5rem 0;
  padding: 0.5rem;
}
button{
  padding: 0.5rem;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}
</style>