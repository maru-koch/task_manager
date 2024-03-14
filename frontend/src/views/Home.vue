<template>
  <div class="home">
    <Analytics :analytics="analytics" />
    <FilterNav @filterChange="current = $event" :current="current" />
    <div v-if="projects.length">
      <div v-for="project in filteredProjects" :key="project.id">
        <SingleProject :project="project" @delete="handleDelete" @complete="handleComplete" />
      </div>
    </div>
  </div>
</template>

<script>
  import SingleProject from "../components/SingleProject.vue";
  import FilterNav from "../components/FilterNav.vue";
  import Analytics from "../components/Analytics.vue";

  export default {
    name: "Home",
    components: { SingleProject, FilterNav, Analytics },
    data() {
      return {
        tasks: [],
        current: "all",
        base_url:"http://localhost:8000/tasks"
      };
    },
    mounted() {
      fetch(this.base_url).then((res) =>
        res
          .json()
          .then((data) => (this.tasks = data))
          .catch((error) => console.log(error.message))
      );
    },
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
        if (this.current === "ongoing") {
          return this.tasks.filter((task) => !task.complete);
        }
        return this.tasks;
      },
    },
  };
</script>
