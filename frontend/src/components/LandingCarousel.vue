<template>
  <v-carousel
    show-arrows="hover"
    hide-delimiter-background
    cycle
    class="mx-auto"
    height="550px"
  >
    <!-- <template v-slot:prev="{ props }" >
        <v-btn
          class="prevBtn"
          variant="elevated"
          @click="props.onClick"
          @mouseover="props.onHover"
        ><</v-btn>
      </template>
      <template v-slot:next="{ props }">
        <v-btn
          class="nextBtn"
          variant="elevated"
          @click="props.onClick"
          @mouseover="props.onHover"
        >></v-btn>
      </template> -->
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
  width: 90%;
  margin: -20px;
}

.prevBtn {
  margin: -20px;
  height: 20px;
  width: 20px;
  border-radius: 25%;
  background-color: rgba(1, 61, 90)
}
/* .prevBtn:hover {
  background-color: rgba(1, 61, 90);
} */

.nextBtn {
  margin: -20px;
  height: 20px;
  width: 20px;
  border-radius: 25%;
  background-color: rgba(1, 61, 90)
}
</style>
