<template>
  <v-app-bar color="#FCF3f3" class="sticky">
    <div class="logo">
      <RouterLink to="/"
        ><v-img src="../assets/logo2_coloured.png" id="logo-img"></v-img
      ></RouterLink>
    </div>
    <!-- <v-spacer></v-spacer> -->
    <v-tabs class="mx-auto" align-tabs="center">
      <div>
        <RouterLink to="/"><v-tab value="Home">Home</v-tab></RouterLink>
        <!-- <RouterLink to="/Destinations" -->
        <RouterLink to="/functionpage"
          ><v-tab value="Destination" @click="filterReturn()"
            >Destination</v-tab
          ></RouterLink
        >
        <!-- <RouterLink to="/Activities" -->
        <RouterLink to="/functionpage"
          ><v-tab value="Activities" @click="filterReturn()"
            >Activities</v-tab
          ></RouterLink
        >
        <!-- <RouterLink to="/ItineraryPlanner" -->
        <RouterLink to="/aboutus"
          ><v-tab value="ItineraryPlanner">Itinerary Planner</v-tab></RouterLink
        >
      </div>
    </v-tabs>
    <!-- <v-spacer></v-spacer> -->
    <div id="sign-in">
      <RouterLink to="/login">
        <v-btn
          id="sign-in-button"
          append-icon="mdi-account"
          class="rounded-xl ma-5 text-black"
          >Sign In
        </v-btn></RouterLink
      >
    </div>
  </v-app-bar>
</template>

<script>
import { useMapState } from "@/stores/mapStores";
import { map } from "leaflet";

let mapStore = useMapState();

export default {
  name: "NavigationBar",

  methods: {
    filterReturn() {
      mapStore.stateFilter = "";
      mapStore.activityFilter = "";
      mapStore.destionationFilter = "";
    },
  },
};
</script>

<style scoped>
.v-app-bar {
  z-index: 10; /* Ensure it is above other elements */
}

.v-tab {
  margin-inline: 10px;
  color: black;
  font-weight: bold;
}
.logo {
  height: 100%;
  width: 10%;
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
