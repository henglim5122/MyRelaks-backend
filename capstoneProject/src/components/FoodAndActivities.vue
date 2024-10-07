<template>
  <h1 class="mx-auto text-center">Things to do and try</h1>
  <div class="carousel-3d-wrapper pa-10 mt-10 mx-auto">
    <div class="carousel-3d">
      <div
        v-for="(image, index) in images"
        :key="index"
        class="carousel-item"
        :class="{ active: index === current }"
        @click="current = index"
        @dblclick="dbclickOpen(image.title)"
      >
        <v-img :src="image.src" :alt="image.title" class="circle-image" :cover="true"></v-img>
        <br>
        <h2 v-if="index === current" class="title"><a href="/FunctionPage" target="_blank" style="text-decoration: none; color: black;"  @click="filterReturn(image.title)">{{ image.title }}</a></h2>
      </div>
    </div>
    <div id="button-wrapper">
      <v-btn
        density="compact"
        icon="mdi-menu-left"
        @click="prev"
        class="prev-btn"
      ></v-btn>
      <v-btn
        density="compact"
        icon="mdi-menu-right"
        @click="next"
        class="next-btn"
      ></v-btn>
  </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import {useMapState } from "@/stores/mapStores";

let  mapStore= useMapState();

function filterReturn(activity:any) {
  mapStore.activityFilter = activity
  mapStore.stateFilter = ""
}
function dbclickOpen(activity:any) {
  filterReturn(activity);
  window.open('/FunctionPage', '_blank');
}

const current = ref(3); // Start with the third image as active
const images = ref([
  {
    src: "src/assets/FoodActivities/local food.jpg",
    title: "Localty Specialties",
  },
  {
    src: "src/assets/FoodActivities/Pavilion-KL.jpg",
    title: "Shopping Spree",
  },
  {
    src: "src/assets/FoodActivities/theme park.jpg",
    title: "Amusement Park",
  },
  {
    src: "src/assets/FoodActivities/culture.jpg",
    title: "Culture Shock",
  },
  {
    src: "src/assets/FoodActivities/cafe.jpg",
    title: "Cafe Hopping",
  },
  { src: "src/assets/FoodActivities/kinabalu.jpg"
  , title: "Leg Day" },
  {
    src: "src/assets/FoodActivities/diving.jpg",
    title: "Water Experience",
  },
]);

const prev = () => {
  current.value =
    (current.value - 1 + images.value.length) % images.value.length;
};

const next = () => {
  current.value = (current.value + 1) % images.value.length;
};
</script>

<style scoped>
.carousel-3d-wrapper {
  text-align: center;
  position: relative;
  width: 100%;
}

.carousel-3d {
  display: flex;
  justify-content: center;
  align-items: center;
  transform-style: preserve-3d;
  margin-bottom: 50px;
}

.carousel-item {
  position: relative;
  transition: transform 0.2s ease, opacity 0.2s ease;
  opacity: 0.25;
  margin: 0 -20px;
  cursor: pointer;
}


.carousel-item.active {
  transform: scale(1.3);
  opacity: 1;
}

.carousel-item .title {
  margin-top: 10px;
  font-weight: bold;
}

.circle-image {
  border-radius: 50%;
  width: 200px;
  height: 200px;
  transition: transform 0.2s ease;
}

.v-btn {
  height: 40px;
  width: 40px;
  /* background-color: rgba(1, 61, 90, 0.25); */
}

.prev-btn,
.next-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-75%);
}

.prev-btn {
  left: 20px;
}

.next-btn {
  right: 20px;
}
</style>
