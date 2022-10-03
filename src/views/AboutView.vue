<template>
  <div class="about">
    <h1 v-for="(value,key,index) in cars" :key="index">{{ key }}:{{ value }}</h1>
  </div>
</template>

<script setup>
const cars = {
  name: "xx",
  color: "白色",
  price: "0.01"
}
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
