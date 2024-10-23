<template>
  <!-- color="#FCF3f3" -->
  <v-app-bar color="#FCF3f3" class="sticky">
    <div class="logo">
      <RouterLink to="/"
        ><v-img src="../assets/logo2_coloured.png" id="logo-img"></v-img
      ></RouterLink>
    </div>
    <!-- <v-spacer></v-spacer> -->
    <v-tabs class="mx-auto" align-tabs="center" v-model="model">
      <div>
        <RouterLink to="/"><v-tab value="Home">Home</v-tab></RouterLink>

        <!-- <RouterLink to="/Destinations" -->
        <v-menu>
          <template v-slot:activator="{ props }">
            <v-tab value="Destinations" v-bind="props"
              >Destinations</v-tab
            >
          </template>
          <v-list>
            <v-row>
              <v-col cols='6' sm="6" md="6">
                <v-list-item v-for="(state, i) in firstColumn"
                  :key = 'i'
                  :value = 'i'>
                  <!-- <v-btn > -->
                    <RouterLink to="/functionpage" :style="{'text-decoration': 'none', 'color': 'black'}">
                      <v-list-item-title @click="filterReturn(state.title,null)"  class="listItem">
                        {{ state.title }}
                      </v-list-item-title>
                    </RouterLink>
                  <!-- </v-btn> -->
                </v-list-item>
              </v-col>  

              <v-col cols='6' sm="6" md="6">
                <v-list-item v-for="(state, i) in secondColumn"
                  :key = 'i'
                  :value = 'i' class="listItem">
                  <!-- <v-btn > -->
                    <RouterLink to="/functionpage" :style="{'text-decoration': 'none', 'color': 'black'}">
                      <v-list-item-title @click="filterReturn(state.title,null)" class="listItem">
                        {{ state.title }}
                      </v-list-item-title>
                    </RouterLink>
                  <!-- </v-btn> -->
                </v-list-item>
              </v-col>  
            </v-row>
          </v-list>
        </v-menu>

        <v-menu>
          <template v-slot:activator="{ props }">
            <v-tab value="Activities" v-bind="props"
              >Activities</v-tab
            >
          </template>
          <v-list>
            <v-list-item
              v-for="(activity, i) in activities"
              :key = 'i'
              :value = 'i'>
              <RouterLink to="/functionpage" :style="{'text-decoration': 'none', 'color': 'black'}">
                <v-list-item-title @click="filterReturn(null,activity.title)" class="listItem">
                  {{ activity.title }}
                </v-list-item-title>
                </RouterLink>
            </v-list-item>
          </v-list>
        </v-menu>
        <RouterLink to="/aboutus"
          ><v-tab value="ItineraryPlanner">Itinerary Planner</v-tab></RouterLink
        >
        <RouterLink to="/accommodation"
          ><v-tab value="accommodation">Accommodation</v-tab></RouterLink
        >
      </div>
    </v-tabs>
    <div id="sign-in">
      <v-icon @click="$emit('subscribe')" class="subscribeBtn">mdi-alpha-s-circle</v-icon>
      <RouterLink to="/login">
        <v-btn
          id="sign-in-button"
          append-icon="mdi-account"
          class="rounded-xl mx-5 text-white"
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
  data() {
    return {
      model: null,
      states: [
        { title: 'All' },
        { title: 'Perlis' },
        { title: 'Kedah' },
        { title: 'Pulau Pinang' },
        { title: 'Perak' },
        { title: 'Kelantan' },
        { title: 'Terengganu' },
        { title: 'Pahang' },
        { title: 'Selangor' },
        { title: 'Kuala Lumpur' },
        { title: 'Putrajaya' },
        { title: 'Negeri Sembilan' },
        { title: 'Melaka' },
        { title: 'Johor' },
        { title: 'Sabah' },
        { title: 'Labuan' },
        { title: 'Sarawak' },
      ],
      activities: [
        {title: "All"},
        {title: "Amusement Park"},
        {title: "Culture Shock"},
        {title: "Water Experience"},
        {title: "Cafe Hopping"},
        {title: "Local Specialty"},
        {title: "Shopping Spree"},
        {title: "Leg Day"},]
    };
  },
  mounted() {
    this.states = this.sortArray(this.states);
    this.activities = this.sortArray(this.activities);
  },
  emits: ["filter",'subscribe'],
  methods: {
    filterReturn(state, activity) {
      this.$emit('filter',{ state, activity })
      if (state) {state !== 'All' ?
          mapStore.setStateFilter (state) :mapStore.setStateFilter("")
          mapStore.setactivityFilter("")}
      else if (activity) {
        activity !== 'All' ?
        mapStore.setactivityFilter(activity) : mapStore.setactivityFilter("")  
        mapStore.setStateFilter("")
    }
    },
    sortArray(array) {
      // Separate "All" from the rest, sort the rest alphabetically
      let allItem = array.find(item => item.title === 'All');
      let sortedArray = array
        .filter(item => item.title !== 'All')
        .sort((a, b) => a.title.localeCompare(b.title));

      // Put "All" back at the top
      if (allItem) {
        sortedArray.unshift(allItem);
      }
      return sortedArray;
    },
  },
  computed: {
    firstColumn() {
      return this.states.slice(0, Math.ceil(this.states.length / 2));
    },
    secondColumn() {
      return this.states.slice(Math.ceil(this.states.length / 2));
    },
  }
};
</script>

<style scoped>
.v-app-bar {
  z-index: 10; /* Ensure it is above other elements */
}

.v-list-item {
  font-size: small;
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
  background-color: rgba(1, 61, 90);
  margin: 19px 0px 19px 0px;
}

#sign-in {
  width: 15%;
  
}

.sticky {
  position: sticky !important;
  margin-top: -20px;
}

.listItem {
  text-wrap: wrap;
  margin: 0px 5px 0px 5px;
}

.listItem:hover {
  font-weight: bold;
}

.subscribeBtn {
  font-size: 35px;
  color: gold;
  -webkit-text-stroke: 1px black;
  padding-right: 10px;
}
</style>
