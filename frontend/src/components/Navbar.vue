<script>
    export default {
        data() {
            return {
                isAuthenticated: true
            }
        },
    };
</script>

<template>
    <nav class="main-nav">
        <div class="logo">
            <img src="../assets/logo2.png" alt="logo" />
        </div>
        <div v-if="isAuthenticated" class="inner-nav">
            <span class="img-holder">
                <img src="../assets/logo.png" alt="logo" />
            </span>
            <span>
                <h5>{{ 'Maruche' }}</h5>
            </span>
            <span>
                <router-link :to="{ name: 'Home' }">Log out</router-link>
            </span>
        </div>
        <div v-else class="outer-nav">
            <router-link :to="{ name: 'Home' }">Login</router-link>
            <router-link :to="{ name: 'Home' }">Sign Up</router-link>
        </div>
    </nav>
</template>


<style>
    .main-nav {
        display:flex;
        justify-content: space-between;
        align-items: center;
    }

    .main-nav .inner-nav, .main-nav .outer-nav{
        display: flex;
        justify-content: space-between;
        gap:20px;
        align-items: center;
    }
    .logo, .img-holder {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        object-fit: contain;
    }

    .logo img, .img-holder img {
        width: 100%;
        height: 100%;
        overflow: hidden;
    }

    .main-nav a {
        text-decoration: none;
        color: #000;
        font-size: 18px;
    }

    .img-holder img {
        border-radius: 50%;
        border:1 px solid rgb(188, 176, 199)
    }
</style>