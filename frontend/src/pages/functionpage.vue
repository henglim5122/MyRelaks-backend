<template>
  <v-app>
    <NavigationBar @filter="refreshPage" @subscribe="subscribe"/>
      <v-main>
        <div :class="{'blur-background': subscribePopup}" @click="subscribePopup = false">
          <div v-if="destinationFilter.length === 0" class="errorMsg">
            <v-alert type="info" elevation="2" color="error">
            No destinations found for the selected criteria.
            </v-alert>
          </div>
          <div v-for="(destination,index) in destinationFilter" :key="index">
            <!-- <div>{{destination.state}}</div> -->
            <DestinationCard :destination="destination" height="250px"/>
          </div>
        </div>

        <div v-if="subscribePopup" class="subscriptionPopup text-center overlay" >
          <div class="d-flex justify-center align-center mx-5">
          <v-spacer></v-spacer>
          <h2 class="my-5 ml-10">Get Your Offer Now</h2>
          <v-spacer></v-spacer>
            <v-icon @click="subscribePopup = false">mdi-close</v-icon>
          </div>
          <div class="aligncenter border-lg d-flex justify-center align-start">
            <v-row>
              <v-col v-for="(tier,index) in subscriptionTier" :key="index" col="12"> 
                <v-btn class="tierStyle"><div @click='selectTier(tier)' >{{ tier }}</div></v-btn>
              </v-col>
            </v-row>
            
          </div>
          <div class="tierSelected"><LandingSubscription height="450px" width="325px" :isSingle="true" :tier="selectedTier"/></div>
        </div>
      </v-main>
  </v-app>
</template>

<script>
import DestinationCard from "@/components/DestinationCard.vue";
import { useMapState } from "@/stores/mapStores";
import destinationAll from "@/assets/Updated_destination.json";

const mapStore = useMapState();

export default {
  name: "FunctionPage",
  components: {
    DestinationCard 
  },
  data() {
    return {
      stateArray: [mapStore.stateFilter],
      activityArray: [mapStore.activityFilter],
      destArray: [mapStore.destinationFilter],
      destinationFilter: [],
      stateTitle: '',
      subscribePopup: false,
      subscriptionTier: ['Freemium','Starter','Intermediate','Pro'],
      selectedTier: '',
    }
  },

  mounted() {
    
  },
  methods: {
    refreshPage() {
      location.reload();
  },
    subscribe() {
      this.subscribePopup = !this.subscribePopup;
      // console.log(this.subscribePopup);
   },
   selectTier(tier) {
    // console.log(tier);
     this.selectedTier = tier;
   }
  },

  computed: {
    destinationFilter() {
      return destinationAll.filter((destination) => {
        const stateMatch =  (this.stateArray.length === 1) && (this.stateArray.includes('')) || this.stateArray.includes(destination.state)
        // console.log(stateMatch);
        const activityMatch = (this.activityArray.length === 1) && (this.activityArray.includes('')) || this.activityArray.includes(destination.activityCategory) 
        // console.log(activityMatch);
        const nameMatch = (this.destArray.length === 1) && (this.destArray.includes('')) || this.destArray.includes(destination.name)
        // console.log(nameMatch);
        return stateMatch && activityMatch && nameMatch ;
      });
      
    },
    
  },
}
</script>

<style scoped>
.errorMsg {
  width: 90%;
  margin: auto;
  margin-top: 20px;
}

.tierStyle{
  font-weight: bold;
  font-size: 20px;
  border: black 1px solid;
  border-radius: 10px;
}

.tierSelected {
  font-weight: bold;
  transition: opacity 1s ease;
  opacity: 1;
}

.aligncenter {
  /* position: absolute;
  left: 50%;
  top: 30%;
  transform: translateX(-50%) translateY(-50%); */
  background-color: white;
  width: 100%;
  margin-bottom: 1%;
}
.subscriptionPopup {
  position: absolute;
  left: 50%;
  top: 55%;
  transform: translateX(-50%) translateY(-50%);
  background-color: white;
  height: 550px;
  width: 90%;
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
</style>