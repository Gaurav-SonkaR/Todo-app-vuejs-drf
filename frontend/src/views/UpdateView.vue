<template>
    <div>
      <h1>Update Task</h1>
      <form @submit.prevent="update">
        <div>
          <label for="title">Title : </label>
        <input type="text" v-model="title" placeholder="Title" required />
      </div>
      <div>
          <label for="description">Description : </label>
          <input type="text" v-model="description" placeholder="Description"  />
      </div>
        <div>
          <label for="complete">Is Completed ? : </label>
          <input type="checkbox" v-model="complete" />{{ complete ? "Yes":"No" }}
      </div>
      <button type="submit">Update Task</button>
      </form>
    </div>
  </template>
  
  <script>
  
  import axios from 'axios'
  
  export default {
    data(){
      return{
        title: '',
        description: '',
        complete: false,
        id: null
      }
    },
    // props: ['id'],
    created(){
      this.id = this.$route.params.id;
    axios.get(`http://127.0.0.1:8000/api/task-detail/${this.id}/`).then(response => {
      let task = response.data;
      console.log(response.data);
        this.title = task.title;
        this.description = task.description;
        this.complete = task.complete;
    }).catch(error => {
      alert(error);
    });	

    },
    methods:{
      update(){
          axios.patch(`http://127.0.0.1:8000/api/task-update/${this.id}/`, {
            id: this.id,
            title:this.title,
            description: this.description,
            complete: this.complete
          }).then(response => {
            this.title = '';
            this.description = '';
            this.complete = '';
            this.$router.push('/');
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

form div{
  margin: 1rem 0;
}

button{
  padding: 0.5rem;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}
</style>