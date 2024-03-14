<template>
    <div class="container">
        <form @submit.prevent="handleSubmit">
            <fieldset>
                <span>Email</span>
                <input type="text" v-model="email" required placeholder="Enter Email Address"/>
            </fieldset>
            <fieldset>
                <span>Password</span>
                <input type="password" v-model="password" required placeholder="Enter password"/>
            </fieldset>
            <button @click="handleSubmit">Log in</button>
        </form>
    </div>
</template>
  
  <script>
    import ENDPOINTS from "../api/client";
    export default {
      data() {
        return {
          email: "",
          password: "",
        };
      },
      methods: {
        async handleSubmit() {
          const payload = {
            email: this.email,
            password: this.password,
          };

          const res = await ENDPOINTS.login(payload);
          // handle response
        
          if (res.status===200){
            const data = res.data;
            console.log(data['status'])
            if (data['status'] === 200){
                const token = data.token.access;
                ENDPOINTS.setAuthorization(token)
                const user = data.user;
                this.$router.push('/dashboard')
                // toastify success.

            }else if(data.status===404){
              const msg = data.msg;
              // toastify
              console.log(msg)
            }

          }else{
            console.log('Server error')
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
        height: auto;
        width:100%;
        background-color: transparent;
  }
    form {
      background: white;
      width:400px;
      height: auto;
      border-radius: 8px;
      box-shadow: 2px 3px 2px rgba(0, 0, 0, 0.05);
      padding: 20px;
      background-color: white;
      border-radius: 10px;
    }
  
    input {
      padding: 10px;
      border: 0;
      border: 1px solid #ddd;
      width: 100%;
      box-sizing: border-box;
      border-radius: 4px;
    }
    input:active, input:focus{
      outline: none;
      border:0;
      border-radius:0;
      border-bottom: 1px solid #00ce89;
    }
    form button {
      display: block;
      margin: 20px auto 0;
      background: #00ce89;
      color: white;
      padding: 10px 20px;
      border: 0;
      border-radius: 6px;
      font-size: 16px;
    }

    fieldset{
      outline:none;
      border: 0;
    }
    fieldset span{
      margin-bottom:4px;
    }
  </style>
  