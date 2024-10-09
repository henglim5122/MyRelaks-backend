<template>
  <v-app>
    <NavigationBar/>
    <v-main>
      <v-container max-width="1600px" id="container-wrapper">
      <LandingCarousel :src="images" />
      <div class="pa-5"></div>
      <LandingDivider />
      <div class="pa-5"></div>
      <LandingFeature height="550px"/>
      <div class="pa-5"></div>
      <LandingDivider />
      <div class="pa-5"></div>
      <LandingMap />
      <div class="pa-10"></div>
      <FoodAndActivities />
      <div class="pa-10"></div>
    </v-container>
      <LandingChatBot height="600px" />
      <div class="pa-5"></div>
    </v-main>
    <LandingFooter />
  </v-app>
</template>

<script>
import NavigationBar from "@/components/NavigationBar";
import LandingCarousel from "@/components/LandingCarousel";

export default {
  data() {
    return {
      images: [
"src/assets/LandingCarousel/1.jpg",
"src/assets/LandingCarousel/2.jpg",
"src/assets/LandingCarousel/3.jpg",
"src/assets/LandingCarousel/4.jpg",
"src/assets/LandingCarousel/5.jpg",
"src/assets/LandingCarousel/6.jpg",
      ],
    };
  },
};
</script>

<style>
.v-main,
.v-app {
  background-color: #fcf3f3;
}

#container-wrapper {
  color: black;
}
</style>
