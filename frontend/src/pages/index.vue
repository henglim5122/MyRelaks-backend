<template>
  <v-app>
    <NavigationBar @subscribe="subscribe" @filter="refreshPage" />
    <v-main :class="{ blur: paymentActive }">
      <v-container max-width="1600px" id="container-wrapper">
        <LandingCarousel :src="images" />
        <div class="pa-10"></div>
        <LandingDivider />
        <div class="pa-5"></div>
        <LandingFeature height="550px" />
        <div class="pa-5"></div>
        <LandingDivider />
        <div class="pa-5"></div>
        <LandingMap />
        <div class="pa-5"></div>
        <LandingDivider />
        <div class="pa-5"></div>
        <FoodAndActivities />
        <div class="pa-10"></div>
      </v-container>
      <LandingChatBot height="600px" width="1600px" />
      <div class="pa-5"></div>
      <div class="backgroundColour">
        <div class="subscriptionTitle" id="subscription">Subscription Plan</div>
        <LandingSubscription height="450px" width="325px" @pay="openPayment" />
      </div>
      <div class="pa-5"></div>

      <!-- <Payment /> -->
    </v-main>
    <LandingFooter />

    <div v-if="paymentActive" class="overlay">
      <Payment :paymentAmount="selectedSub.price" @close="paymentActive = false" />
    </div>
  </v-app>
</template>

<script>
import NavigationBar from '@/components/NavigationBar';
import LandingCarousel from '@/components/LandingCarousel';

export default {
  data() {
    return {
      images: [
        'src/assets/LandingCarousel/1.jpg',
        'src/assets/LandingCarousel/2.jpg',
        'src/assets/LandingCarousel/3.jpg',
        'src/assets/LandingCarousel/4.jpg',
        'src/assets/LandingCarousel/5.jpg',
        'src/assets/LandingCarousel/6.jpg',
      ],
      paymentActive: false,
      selectedSub: '',
    };
  },
  methods: {
    // refreshPage() {
    //   location.reload();
    // },
    subscribe() {
      const yOffset = -100;
      const element = document.getElementById('subscription');
      const y = element.getBoundingClientRect().top + window.scrollY + yOffset;
      window.scrollTo({ top: y, behavior: 'smooth' });
      // this.$refs.subscription?.scrollIntoView({ behavior: 'smooth' });
    },
    openPayment(subscription) {
      this.selectedSub = subscription;
      this.paymentActive = true;
    },
    handleKeydown(event) {
      if (event.key === 'Escape') {
        this.paymentActive = false;
      }
    },
  },
  mounted() {
    window.addEventListener('keyup', this.handleKeydown);
  },
};
</script>

<style scoped>
.v-main,
.v-app {
  background-color: #fcf3f3;
}

#container-wrapper {
  color: black;
}

.backgroundColour {
  background: linear-gradient(to bottom, rgba(1, 61, 90), #fcf3f3);
  padding: 30px 0px 30px 0px;
}
.subscriptionTitle {
  font-size: 65px;
  font-weight: bold;
  letter-spacing: 2px;
  margin-bottom: 30px;
  text-align: center;
  color: white;
  -webkit-text-stroke: 1.5px black;
}
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent dark overlay */
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.blur {
  filter: blur(8px);
  transition: filter 0.3s ease;
}
</style>
