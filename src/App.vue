<template>
  <div id="app">
  <button @click="SelectWinner()">Select a Winner</button>
    <img src="./assets/logo.png">
    {{winner}}
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'App',
  data() {
      return {
          names: null,
          winner: null,
      }
  },
  mounted: function() {
    this.FetchData();
  },
  methods: {
      FetchData: function() {
          var app = this;
          axios.get(process.env.API_URL + "/api_example/").then(response => {
              app.names = response.data.names;
              console.log(app.names);
          });
      },
      SelectWinner: function() {
        var winner = this.names[Math.floor(Math.random()*this.names.length)];
        this.winner = winner;
      },
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
