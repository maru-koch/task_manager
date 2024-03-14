  <script>
      import Navbar from "./components/Navbar.vue";
      export default {
        components: { Navbar },
      };
  </script>

<template>
  <Navbar />
  <router-view />
</template>

<style>
  body {
    background: #f2f2f2;
  }

  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    max-width: 60vw;
    margin: 0 auto;
    color: #555;
  }

  button {
    cursor: pointer;
  }
</style>
