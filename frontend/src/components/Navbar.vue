<script>
    export default {
        props:["isAuthenticated"],
        data() {
            return {
                isAuthenticated: false
            }
        },
    };
</script>

<template>
    <nav class="main-nav">
        <div class="logo">
            <router-link :to="{ name: 'Home' }">
                <img src="../assets/icon.png" alt="logo" />
            </router-link>
        </div>
        <div v-if="isAuthenticated" class="inner-nav">
            <span class="img-holder">
                <img class="user-profile" src="../assets/logo.png" alt="logo" />
            </span>
            <span>
                <h5>{{ 'Maruche' }}</h5>
            </span>
            <span>
                <router-link :to="{ name: 'Home' }">Log out</router-link>
            </span>
        </div>
        <div v-else class="outer-nav">
            <router-link :to="{ name: 'Login' }">Login</router-link>
            <router-link :to="{ name: 'Register' }">Sign Up</router-link>
        </div>
    </nav>
</template>


<style>
    .main-nav {
        display:flex;
        justify-content: space-between;
        align-items: center;
        padding:8px 0;
    }

    .main-nav .inner-nav, .main-nav .outer-nav{
        display: flex;
        justify-content: space-between;
        gap:20px;
        align-items: center;
    }

    .logo, .img-holder {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        object-fit: contain;
    }

    .main-nav img{
        width: 100%;
        height: 100%;
        overflow: hidden;
    }

    .main-nav a {
        text-decoration: none;
        color: #2b2b2b;
        font-size: 16px;
    }
    .logo a{
        border-bottom:0;
    }
    
    .img-holder .user-profile {
        border-radius: 50%;
        border:1 px solid rgb(188, 176, 199)
    }
</style>