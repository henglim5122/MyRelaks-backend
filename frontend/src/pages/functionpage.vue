<template>
  <v-app>
    <NavigationBar @filter="refreshPage" @subscribe="subscribe" class="navigation" />
    <v-main :class="{ blur: paymentActive }">
      <div :class="{ 'blur-background': subscribePopup }" @click="closePopUp">
        <div v-if="destinationFilter.length === 0" class="errorMsg">
          <v-alert type="info" elevation="2" color="error">
            No destinations found for the selected criteria.
          </v-alert>
        </div>
        <div v-for="(destination, index) in destinationFilter" :key="index">
          <!-- <div>{{destination.state}}</div> -->
          <DestinationCard :destination="destination" height="250px" />
        </div>
      </div>

      <div v-if="subscribePopup" class="subscriptionPopup text-center overlay">
        <div class="d-flex justify-center align-center mx-5">
          <v-spacer></v-spacer>
          <h1 class="my-3 ml-10">Get Your Offer Now</h1>
          <v-spacer></v-spacer>
          <v-icon @click="closePopUp">mdi-close</v-icon>
        </div>
        <div class="aligncenter">
          <v-row>
            <v-col v-for="(tier, index) in subscriptionTier" :key="index" col="12">
              <v-btn class="tierStyle"
                ><div @click="selectTier(tier)">{{ tier }}</div></v-btn
              >
            </v-col>
          </v-row>
        </div>
        <div class="tierSelected">
          <LandingSubscription
            height="450px"
            width="325px"
            :isSingle="true"
            :tier="selectedTier"
            @pay="openPayment"
          />
        </div>
      </div>
    </v-main>
    <div v-if="paymentActive" class="overlay-payment">
      <Payment :paymentAmount="selectedSub.price" @close="paymentActive = false" />
    </div>
  </v-app>
</template>

<script>
import DestinationCard from '@/components/DestinationCard.vue';
import { useMapState } from '@/stores/mapStores';
import destinationAll from '@/assets/Updated_destination.json';

const mapStore = useMapState();

export default {
  name: 'FunctionPage',
  components: {
    DestinationCard,
  },
  data() {
    return {
      stateArray: [mapStore.stateFilter],
      activityArray: [mapStore.activityFilter],
      destArray: [mapStore.destinationFilter],
      destinationFilter: [],
      stateTitle: '',
      subscribePopup: false,
      subscriptionTier: ['Freemium', 'Starter', 'Intermediate', 'Pro'],
      selectedTier: ['Freemium'],
      active: false,
      paymentActive: false,
      selectedSub: '',
    };
  },

  mounted() {},
  methods: {
    closePopUp() {
      this.subscribePopup = false;
      this.selectedTier = ['Freemium'];
    },

    refreshPage() {
      location.reload();
    },
    subscribe() {
      this.subscribePopup = !this.subscribePopup;
      // console.log(this.subscribePopup);
    },
    selectTier(tier) {
      if (!this.selectedTier.includes(tier)) {
        if (this.selectedTier.length > 2) {
          this.selectedTier.shift();
        }
        this.selectedTier.push(tier);
      } else if (tier !== 'Freemium') {
        this.selectedTier.splice(this.selectedTier.indexOf(tier), 1);
        // console.log(this.selectedTier);
      }
    },
    openPayment(subscription) {
      this.selectedSub = subscription;
      this.paymentActive = true;
      this.subscribePopup = false;
    },
  },

  computed: {
    destinationFilter() {
      return destinationAll.filter((destination) => {
        const stateMatch =
          (this.stateArray.length === 1 && this.stateArray.includes('')) ||
          this.stateArray.includes(destination.state);
        // console.log(stateMatch);
        const activityMatch =
          (this.activityArray.length === 1 && this.activityArray.includes('')) ||
          this.activityArray.includes(destination.activityCategory);
        // console.log(activityMatch);
        const nameMatch =
          (this.destArray.length === 1 && this.destArray.includes('')) ||
          this.destArray.includes(destination.name);
        // console.log(nameMatch);
        return stateMatch && activityMatch && nameMatch;
      });
    },
  },
};
</script>

<style scoped>
.errorMsg {
  width: 90%;
  margin: auto;
  margin-top: 20px;
}

.tierStyle {
  font-weight: bold;
  font-size: 20px;
  border: black 1px solid;
  border-radius: 10px;
}

.tierSelected {
  margin-top: -15px;
}

.aligncenter {
  background-color: white;
  width: 100%;
  margin-bottom: 1%;
}
.navigation {
  z-index: 250;
}

.subscriptionPopup {
  position: absolute;
  left: 50%;
  top: 55%;
  transform: translateX(-50%) translateY(-50%);
  background-color: white;
  height: 600px;
  width: 1300px;
  /* cursor: pointer; */
  border: 1px solid black;
  box-shadow: 3px 3px 3px 3px rgba(0, 0, 0, 0.2);
  border-radius: 20px;
  z-index: 9999;
}

.subscriptionLayout {
  position: absolute;
  left: 50%;
  top: 55%;
  transform: translateX(-50%) translateY(-50%);
}

.blur-background {
  filter: blur(10px);
  transition: filter 0.15s ease;
}

.overlay {
  position: fixed;
  z-index: 50;
}

.blur-background {
  filter: blur(10px);
  transition: filter 0.15s ease;
}

.blur {
  filter: blur(8px);
  transition: filter 0.3s ease;
}
.overlay-payment {
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
</style>
