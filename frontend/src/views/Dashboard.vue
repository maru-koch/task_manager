<template>
  <div class="home">
    <Analytics :user="user"/>
    <FilterNav @filterChange="current = $event" :current="current" />
    <div v-if="tasks.length">
      <div v-for="task in filteredProjects" :key="task.id">
        <SingleProject :project="task" @delete="handleDelete" @complete="handleComplete" />
      </div>
    </div>
    <div v-else class="empty">
      <i class="fas fa-user"></i>
      <h2>No tasks available</h2>
    </div>
  </div>
</template>

<script>
  import SingleProject from "../components/SingleProject.vue";
  import FilterNav from "../components/FilterNav.vue";
  import Analytics from "../components/Analytics.vue";
  import data from "../../data/db.json"

  export default {
    name: "Dashboard",
    components: { SingleProject, FilterNav, Analytics},
    data() {
      return {
        user:{first_name:"Maruche"},
        tasks: data,
        current: "all",
        base_url:"http://localhost:8000/tasks"
      };
    },
    // mounted() {
    //   fetch(this.base_url).then((res) =>
    //     res
    //       .json()
    //       .then((data) => (this.tasks = data))
    //       .catch((error) => console.log(error.message))
    //   );
    // },
    methods: {
      handleDelete(id) {
        this.tasks = this.tasks.filter((task) => task.id !== id);
      },
      handleComplete(id) {
        const p = this.tasks.find((task) => {
          return task.id === id;
        });
        p.complete = !p.complete;
      },
    },
    computed: {
      filteredProjects() {
        if (this.current === "completed") {
          return this.tasks.filter((task) => task.complete);
        }
        if (this.current === "inprogress") {
          return this.tasks.filter((task) => !task.complete);
        }
        return this.tasks;
      },
    },
  };
</script>
<style>
  .empty{
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    opacity:0.4;
  }

  .empty i{
    font-size: 18rem;
    color: #ccc;
  }

  .empty h2{
    color: #1a1919;
    font-size:14px;
    font-weight: 300;
  }
</style>