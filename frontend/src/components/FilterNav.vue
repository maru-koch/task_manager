<template>
  <nav class="filter-nav">
    <div class="nav-btn">
    
      <button @click="updateFilter('all')" :class="{ active: current === 'all' }">View all</button>
      <button @click="updateFilter('completed')" :class="{ active: current === 'completed' }">
        Completed
      </button>
      <button @click="updateFilter('ongoing')" :class="{ active: current === 'ongoing' }">
        Ongoing
      </button>
    </div>  
    <div class="nav-add">
        <router-link :to="{ name: 'AddTask' }"><span style="margin:0 4px"><i class="fas fa-plus"></i></span>New Task</router-link>
    </div>
  </nav>
</template>

<script>
  export default {
    props: ["current"],
    methods: {
      updateFilter(by) {
        this.$emit("filterChange", by);
      },
    },
  };
</script>

<style>
  .filter-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 20px 0;
  }
  .nav-btn button {
    background: none;
    border: none;
    color: #bbb;
    outline: none;
    font-size: 12px;
    text-transform: uppercase;
    margin-right: 10px;
    letter-spacing: 1px;
    font-weight: bold;
    cursor: pointer;
  }

  .nav-btn button.active {
    color: #555;
  }

  .nav-add a {
    display: inline-block;
    text-decoration: none;
    margin: 0 10px;
    color: #999;
    font-size: 18px;
  }

  a.router-link-active {
    border-bottom: 2px solid #00ce89;
    padding-bottom: 4px;
  }

  .nav-add a{
    background-color: #00ce89;
    color:white;
    font-size: 14px;
    border-radius: 8px;
    padding:4px 8px;
  }
</style>
