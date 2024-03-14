<template>
    <div class="container">
        <form @submit.prevent="handleSubmit">
            <fieldset>
                <span>First Name</span>
                <input type="text" v-model="first_name" required placeholder="Enter your first name"/>
            </fieldset>
            <fieldset>
                <span>Last Name</span>
                <input type="text" v-model="last_name" required placeholder="Your surname"/>
            </fieldset>
            <fieldset>
                <span>Email</span>
                <input type="email" v-model="email" required placeholder="Enter Email Address"/>
            </fieldset>
            <fieldset>
                <span>Password</span>
                <input type="password" v-model="password" required placeholder="Enter password"/>
            </fieldset>
            <fieldset>
                <span>Confirm Password</span>
                <input type="password" v-model="password2" required placeholder="Confirm your password"/>
            </fieldset>
            <button @click="handleSubmit">Register</button>
        </form>
    </div>
</template>
  
  <script>

  import ENDPOINTS from "../api/client";

    export default {
      data() {
        return {
          first_name: "",
          last_name: "",
          email: "",
          password: "",
          password2:""
        };
      },
      methods: {
       async handleSubmit(){
          const payload = {
            first_name:this.first_name,
            last_name:this.last_name,
            email: this.email,
            password: this.password,
            password2: this.password2
          };
          
          // call the registration endpoint
          const res = await ENDPOINTS.register(payload);
         
          // display notification based on response code
          if (res?.status===200){
            const data = res?.data;
            if (data.status===201){
                const msg = data?.msg;
                const data_ = data?.data;
                console.log(data_)
                this.$router.push('/login')
            }else if(data['status']===400){
                const msg = data?.msg;
                console.log(msg)

            }else{
                const msg = data?.msg;
                console.log(msg)
            }
          }else{
            console.log('Server Error ')
          }
         
          console.log(res)
      },
    }}
  </script>
  
  <style>
  .container{
        display: flex;
        justify-content: center;
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
      margin:8px auto;
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
      font-size: 16px;
    }
  </style>
  