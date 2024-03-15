<template>
  <div class="container">
    <form @submit.prevent="handleSubmit">
      <span>Title</span>
      <input type="text" v-model="title" required />
      <span>Description</span>
      <textarea v-model="description" required></textarea>
      <button>Add Task</button>
    </form>
  </div>
</template>

<script>
  import ENDPOINTS from '@/api/client';
  export default {
    data() {
      return {
        title: "",
        description: "",
      };
    },
    methods: {
     async handleSubmit() {
      try{
        const payload = {
          title: this.title,
          description: this.description,
        };
        const res = await ENDPOINTS.createTask(payload)
        if (res.status===201){
            console.log('task added successfully')
            this.$router.push("/dashboard");
        }else{
            console.log('unable to add task')
        }
      }catch(err){
          if (err.response.status === 401){
              ENDPOINTS.getAuthorization()
              ENDPOINTS.removeAuthorization()
              this.$router.push('/login')
          }
      }  
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
