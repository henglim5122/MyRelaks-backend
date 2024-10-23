<template>
    <v-app>
      <NavigationBar />
        <v-main>
        <div v-for="(destination,index) in destinationFilter" :key="index">
          <!-- <div>{{destination.state}}</div> -->
           {{  }}
          <DestinationCard :destination="destination" height="250px"/>
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
      stateTitle: ''
    }
  },

  mounted() {
    window.scrollTo(0, 0)
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
.v-main,
.v-app {
  background-color: rgba(252,243,243,0.5)
}
</style>
