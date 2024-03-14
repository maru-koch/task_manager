<template>
    <div class="display">
        <p @click="toggleDetails">Hi {{'Maruche'}}, Welcome!</p>
        <div class="card-holder">
            <div class="card completed">
                <span class="number">{{analytics.completed}}</span>
                <span class="title"> Completed</span>
            </div>
            <div class="card inprogress">
                <span class="number">{{analytics.inprogress}}</span>
                <span class="title">In Progress</span>
            </div>
            <div class="card pending">
                <span class="number">{{analytics.pending}}</span>
                <span class="title">Pending</span>
            </div>
        </div>
    </div>
  </template>
  
  <script>
    export default {
      props: ["user"],
      data() {
        return {
            showDetails: false,
            analystics:{
                total: 0,
                completed: 0,
                inprogress: 0,
                pending: 0},
            base_url:"http://localhost:8000/tasks"
        };
        }
      }
  </script>
  
  <style scoped>
    .display{
      margin: 20px auto;
      background: white;
    }
    .card.complete {
      border-bottom: 4px solid #00ce89;
    }

    .card.inprogress {
      border-bottom: 4px solid #0052ce;
    }

    .card.pending {
      border-bottom: 4px solid #ca032e;
    }
    .card-holder {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
  
    .card{
      border-radius: 10px;
      box-shadow: 2px 3px 4px rgba(0, 0, 0, 0.05);
      background-image: -moz-linear-gradient()(45deg, #ebedee 30%, #9d9a9e 90%);
      background-color: #bbb;
      cursor: pointer;
    }
  
    .card .number {
      font-size: 24px;
      font-weight: 700;
    }

    .card:hover {
      color: #777;
    }
  </style>
  