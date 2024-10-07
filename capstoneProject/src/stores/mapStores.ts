import { useLocalStorage } from "@vueuse/core";
import { defineStore } from "pinia";
import {ref} from 'vue';

// type Marker = {
//   latitude: number;
//   longitude: number;
// };

// export let userMarker = useLocalStorage<Marker>("USER_MARKER", {
//   latitude: 0,
//   longitude: 0,
// });

// export let nearbyMarkers = useLocalStorage<Marker[]>("NEARBY_MARKERS", []);


export const useMapState = defineStore("State", {
  state: () => ({
    stateFilter: useLocalStorage('stateFilter',ref()),
    activityFilter: useLocalStorage('activityFilter',ref()),
    destionationFilter: useLocalStorage('destionationFilter',ref()),
    }),
  actions: {setStateFilter(state: string) {
      this.stateFilter = state;
      // console.log(this.stateFilter);
    },setactivityFilter(activity: string) {
      this.activityFilter = activity;
      // console.log(this.stateFilter);
    },setdestinationFilter(destination: string) {
      this.destionationFilter = destination;
      // console.log(this.stateFilter);
    }}
  
})