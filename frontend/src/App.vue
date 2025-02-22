<script setup>
import { RouterLink, RouterView } from 'vue-router'
import UpdateView from './views/UpdateView.vue';
</script>

<template>
  <header>
    <div class="wrapper">
      <div><h1>TOdo</h1></div>
      <div >
        
          <RouterLink to="/">Home</RouterLink>
          |  
          <RouterLink to="/add">Add Task</RouterLink> |
          <RouterLink to="/update/:id">Update Task</RouterLink>
         
      </div>
  
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1;
  max-height: 100vh;
}

.wrapper {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  
  /* background-color: #f8f9fa; */
  border-bottom: 1px solid #b4b6b9;
}

.link {
  margin: 1rem;
  justify-content: space-between;
  align-items: center;
}
</style>
