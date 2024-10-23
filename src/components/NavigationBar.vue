<template>
  <v-app-bar color="#FCF3f3" class="sticky">
    <div class="logo">
      <RouterLink to="/"
          ><v-img src="../assets/logo2_coloured.png" id="logo-img" ></v-img></RouterLink> 
    </div>
    <!-- <v-spacer></v-spacer> -->
    <v-tabs class="mx-auto" align-tabs="center" v-model="active_tab">
      <div>
        <RouterLink to="/"><v-tab value="Home">Home</v-tab></RouterLink>            
        <RouterLink to="/functionpage"><v-tab value="Destination" v-bind="props" @click="filterReturn()">Destination</v-tab></RouterLink>
        <RouterLink to="/functionpage"><v-tab value="Activities" @click="filterReturn()">Activities</v-tab></RouterLink>
        <RouterLink to="/aboutus"><v-tab value="ItineraryPlanner">Itinerary Planner</v-tab></RouterLink>
        <v-menu v-if="states" open-on-hover>
          <template v-slot:activator="{ props }">
            <v-tab value="Filter" v-bind="props" @click="filterReturn()">Filter</v-tab>
          </template>
          <v-list>
            <v-list-item
              v-for="(state, index) in states"
              :key="index">
              <v-list-item-title>{{ state }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
    </v-tabs>

    <v-menu open-on-hover v-if="states">

    </v-menu>
    <!-- <v-spacer></v-spacer> -->
    <div id="sign-in">
      <RouterLink to="/aboutus">
      <v-btn
        id="sign-in-button"
        append-icon="mdi-account"
        class="rounded-xl ma-5 text-black"
        >Sign In
      </v-btn></RouterLink>
    </div>
  </v-app-bar>
</template>

<script>
import {useMapState } from "@/stores/mapStores";
import { map } from "leaflet";

let  mapStore= useMapState();

export default {
  name: "NavigationBar",
  data: () => {
    return {
      states: ["Selangor","Kedah","Perlis","Negeri Sembilan","Johor","Melaka","Pulau Pinang","Perak","Perlis","Sabah","Sarawak","Kuala Lumpur"],
    }
  },
  methods: {
    filterReturn() {
      mapStore.stateFilter = ""
      mapStore.activityFilter = ""
      mapStore.destionationFilter = ""
    }}
    
    }
</script>

<style scoped>
.v-app-bar {
  z-index: 1000 !important; /* Ensure it is above other elements */
}

.v-tab {
  margin-inline: 10px;
  color: black;
  font-weight: bold;
}
.logo {
  height: 100%;
  width: 15%;
  margin-left: 30px;
}

#sign-in-button {
  background-color: rgba(1, 61, 90, 0.25);
  
}

#sign-in {
  width: 15%;
}

.sticky {
  position: sticky !important;
  margin-top: -20px;
}
</style>
