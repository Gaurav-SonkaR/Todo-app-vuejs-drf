<template>
 <div>
  <h1>Todo List</h1> 
  <table>
    <tr>
      <th>Title</th>
      <th>Description</th>
      <th>Is Completed ?</th>
      <th>Actions</th>
    </tr>
    <tr v-for="task in tasks" :key="task.id">
      <td>{{ task.title }}</td>
      <td>{{ task.description }}</td>
      <td>{{ task.complete }}</td>
      <td class="actions">
        <div><router-link :to="`/update/${task.id}`"><img class="btn" src="https://img.icons8.com/?size=100&id=118958&format=png&color=000000"/></router-link></div>
        <div><p @click="remove(task.id)"><img class="btn" src="https://img.icons8.com/?size=100&id=102350&format=png&color=000000"></p></div>
      </td>
    </tr>
  </table>
  </div>
</template>

<script>

import axios from 'axios';


  export default{
    data(){
      return{
        tasks: []
      }
    },
    created(){
    
        axios.get('http://127.0.0.1:8000/api/task-list/').then(response => {
          this.tasks = response.data;
        }).catch(error => {
          alert(error);
        });	
  
    },
    methods:{

      remove(id){
        axios.delete(`http://127.0.0.1:8000/api/task-delete/${id}/`).then(response => {
          this.tasks = this.tasks.filter(task => task.id !== id);
          alert('Task removed successfully');
        }).catch(error => {
          alert('An error occurred while removing the task');
        });
      }
    }
  }
</script>

<style>
  table{
    width: 90%;
    border-collapse: collapse;    
    margin: 0 auto;
  }
  th, td{
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  th{
    background-color: #cbcaca;
    text-align: center;
  }
  td{
    text-align: center;
  }
  tr:nth-child(even){
    background-color: #f2f2f2;
  }

  h1{
    text-align: center;
  }

  .actions{
    margin: 0 5px;
  }

  .btn{
    width: 20px;
    height: 20px;
  }
</style>