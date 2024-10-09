<template>
  <v-carousel
    show-arrows="hover"
    hide-delimiter-background
    cycle
    class="mx-auto"
    height="550px"
  >
    <v-carousel-item v-for="(img, i) in src" :key="i"
      ><v-img
        :src="img"
        :height="height"
        :width="width"
        cover
        class="mx-15 rounded-xl"
      ></v-img
    ></v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  name: "navigationCarousel",
  props: {
    src: {
      type: Array,
      default: [],
    },
    width: {
      type: String,
      default: "",
    },
    height: {
      type: String,
      default: "",
    },
  },
};
</script>

<style scoped>
.v-carousel {
  justify-content: center;
  align-items: center;
  width: 95%;
}
</style>
