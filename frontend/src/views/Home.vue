<template>
    <div class="container">
        <div class="img-holder">
            <img src="../assets/logo.png"/>
        </div>
        <router-link :to="{name: 'Login' }">Get Started</router-link>
    </div>
</template>

<style>
    .container{
        display:flex;
        justify-content: center;
        align-items: center;
        margin:40px auto;
        flex-direction: column;
        height: auto;
        width:100%;
    }

    .img-holder{
        width:100%;
        height: 400px;
        margin:0 40px;
        object-fit: contain;
        display:flex;
        justify-content: center;
        align-items: center;
    }

    .img-holder img{
        width:auto;
        height:100%
    }

    .container a{
      margin: 20px auto 0;
      background: #00ce89;
      color: white;
      padding: 10px 20px;
      border: 0;
      border-radius: 8px;
      font-size: 16px;
    }
</style>