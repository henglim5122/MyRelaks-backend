<template>
  <v-container fluid>
    <div class="carousel-3d-container">
      <div class="carousel-3d">
        <div
          v-for="(slide, i) in slides"
          :key="i"
          :class="['carousel-3d-item', { 'is-active': currentSlide === i }]"
          :style="getSlideStyle(i)"
        >
          <v-img :src="slide" class="carousel-img"></v-img>
          <div class="text-center">
            <v-text class="text-center bg-white"> {{ slide }}</v-text>
          </div>
        </div>
        <v-btn icon @click="prevSlide">
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
        <v-btn icon @click="nextSlide">
          <v-icon>mdi-chevron-right</v-icon>
        </v-btn>
      </div>
    </div>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      currentSlide: 0,
      slides: [
        "https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg",
        "https://cdn.vuetifyjs.com/images/carousel/sky.jpg",
        "https://cdn.vuetifyjs.com/images/carousel/bird.jpg",
        "https://cdn.vuetifyjs.com/images/carousel/planet.jpg",
        "https://cdn.vuetifyjs.com/images/carousel/planet.jpg",
        "https://cdn.vuetifyjs.com/images/carousel/planet.jpg",
        "https://cdn.vuetifyjs.com/images/carousel/planet.jpg",
        "https://cdn.vuetifyjs.com/images/carousel/planet.jpg",
      ],
    };
  },
  methods: {
    prevSlide() {
      this.currentSlide =
        (this.currentSlide - 1 + this.slides.length) % this.slides.length;
    },
    nextSlide() {
      this.currentSlide = (this.currentSlide + 1) % this.slides.length;
    },
    getSlideStyle(index) {
      const angle = (360 / this.slides.length) * index;
      const translateZ = -500; // Controls the depth of the carousel
      const currentRotation = (360 / this.slides.length) * this.currentSlide;

      return {
        transform: `rotateY(${
          angle - currentRotation
        }deg) translateZ(${translateZ}px)`,
      };
    },
  },
};
</script>

<style scoped>
.carousel-3d-container {
  perspective: 600px;
  position: relative;
  overflow: hidden;
  height: 400px;
}

.carousel-3d {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.5s ease-in-out;
}

.carousel-3d-item {
  position: absolute;
  top: 10%;
  left: 25%;
  width: 45%;
  height: 50%;
  transform-origin: center;
  transition: transform 0.5s ease-in-out;
}

.carousel-img {
  width: 50%;
  height: 50%;
  object-fit: cover;
  /* box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3); */
}

.v-btn {
  position: absolute;
  top: 25%;
  transform: translateY(-50%);
}

.v-btn:first-of-type {
  left: 10px;
}

.v-btn:last-of-type {
  right: 10px;
}
</style>
