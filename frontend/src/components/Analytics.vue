<template>
    <div class="display">
        <p>Hi <span style="font-weight: bold;">{{user.first_name}}</span>, Welcome!</p>
        <div v-if="showAnalytics" class="card-holder">
            <div class="card completed">
                <h2 class="number">{{analystics.completed}}</h2>
                <p class="">Completed</p>
            </div>
            <div class="card inprogress">
                <h2 class="number">{{analystics.inprogress}}</h2>
                <p class="">In Progress</p>
            </div>
            <div class="card pending">
                <h2 class="number">{{analystics.pending}}</h2>
                <p class="">Pending</p>
            </div>
        </div>
    </div>
  </template>
  
  <script>
    import ENDPOINTS from '../api/client';

    export default {
      props: ["user"],
      data() {
        return {
            showAnalytics: false,
            analystics:{
                total: 0,
                completed: 0,
                inprogress: 0,
                pending: 0},
        };
        },
      async mounted(){
        //fetches the analytics data from the backend

        const res = await ENDPOINTS.fetchAnalytics()
        const data = res?.data;
        if (data.length) {this.showAnalytics = True}
        this.analystics.total = data.total_tasks;
        this.analystics.completed = data.completed_tasks;
        this.analystics.inprogress = data.in_progress_tasks;
        this.analystics.pending = data.pending_tasks;
        console.log(this.analystics)
      }
      }
  </script>
  
  <style scoped>
    .display{
      background: white;
      padding:20px;
      border-radius: 8px;
      box-shadow: 2px 3px 2px rgba(0, 0, 0, 0.05);
      margin:20px 0;
    }

    .card{
      border-radius: 8px;
      height: 50px;
      width: 100px;
      box-shadow: 2px 3px 2px rgba(0, 0, 0, 0.05);
      background-image: -moz-linear-gradient()(45deg, #ebedee 30%, #9d9a9e 90%);
      background-color: transparent;
      background-image: linear-gradient()(45deg, #ebedee 30%, #9d9a9e 90%);
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      padding:16px;
    }
  
    .card p, .card h2{
      padding:0;
      margin: 0;
      font-size:0.8rem;
    }
    .card.completed {
      border-bottom: 4px solid #00ce89;
      background-color: #e6f0ec;
    }

    .card.inprogress {
      border-bottom: 4px solid #0052ce;
        background-color: #e8ecf1;
    }

    .card.pending {
      border-bottom: 4px solid #ca032e;
      background-color: #eee6e7;
    }
    .card-holder {
      display: flex;
      justify-content: space-evenly;
      align-items: center;
    }
  
    .card .number {
      font-size: 44px;
      font-weight: 700;
    }

    .card:hover {
      color: #777;
    }
  </style>
  