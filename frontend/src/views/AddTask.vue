<template>
  <div class="container">
    <form @submit.prevent="handleSubmit">
      <label>Title</label>
      <input type="text" v-model="title" required />
      <label>Description</label>
      <textarea v-model="details" required></textarea>
      <button>Add Task</button>
    </form>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        title: "",
        description: "",
      };
    },
    methods: {
      handleSubmit() {
        const project = {
          title: this.title,
          description: this.description,
          complete: false,
        };

        fetch("http://localhost:3000/tasks", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(project),
        })
          .then(() => {
            // navigate to home page if task is 
            // sucessfully added.
            this.$router.push("/");
          })
          .catch((error) => console.log(error.message));
      },
    },
  };
</script>

<style>
  .container{
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 40px auto;
    widows: 100%;
  }
  form {
    background: white;
    padding: 20px;
    border-radius: 10px;
    max-width: 400px;
  }

  label {
    display: block;
    color: #bbb;
    text-transform: uppercase;
    font-size: 14px;
    font-weight: bold;
    letter-spacing: 1px;
    margin: 20px 0 10px 0;
  }

  input {
    padding: 10px;
    border: 0;
    border-bottom: 1px solid #ddd;
    width: 100%;
    box-sizing: border-box;
  }

  textarea {
    border: 1px solid #ddd;
    padding: 10px;
    width: 100%;
    box-sizing: border-box;
    height: 100px;
  }

  form button {
    display: block;
    margin: 20px auto 0;
    background: #00ce89;
    color: white;
    padding: 10px;
    border: 0;
    border-radius: 6px;
    font-size: 16px;
  }
</style>
