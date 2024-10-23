<template>
  <v-app>
    <NavigationBar />
    <v-main>
      <v-row no-gutters>
        <!-- Sidebar (3/12 of the page) -->
        <v-col cols="12" md="6">
          <v-navigation-drawer app permanent>
            <v-list>
              <v-list-item>
                <v-list-item-title class="text-h6">Filter</v-list-item-title>
              </v-list-item>
              <v-divider />

              <!-- Filter button with color -->
              <v-btn color="yellow" @click="showFilterDialog = true" class="mb-4">Filter</v-btn>

              <!-- Show selected States and Activities in the sidebar -->
              <v-list-item>
                <v-list-item-subtitle>Selected States:</v-list-item-subtitle>
                <v-row>
                  <v-col v-for="state in selectedStates" :key="state" cols="auto">
                    <v-chip>{{ state }}</v-chip>
                  </v-col>
                </v-row>
              </v-list-item>

              <v-list-item>
                <v-list-item-subtitle>Selected Activities:</v-list-item-subtitle>
                <v-row>
                  <v-col v-for="activity in selectedActivities" :key="activity" cols="auto">
                    <v-chip>{{ activity }}</v-chip>
                  </v-col>
                </v-row>
              </v-list-item>

              <!-- Favorites Filter Indicator -->
              <v-list-item>
                <v-list-item-subtitle>Show Favorites Only:</v-list-item-subtitle>
                <v-switch v-model="showFavoritesOnly" label="Favorites" class="mt-2" />
              </v-list-item>
            </v-list>
          </v-navigation-drawer>
        </v-col>

        <!-- Main Content (9/12 of the page) -->
        <v-col cols="12" md="9">
          <div v-for="(destination, index) in filteredDestinations" :key="index">
            <DestinationCard
              :destination="destination"
              height="250px"
              :isFavorited="isFavorite(destination)"
              @onLiked="toggleFavorite(destination)"
              @click="openDetailDialog(destination)"
            />
          </div>
        </v-col>
      </v-row>

      <!-- Filter Popup Dialog -->
      <v-dialog v-model="showFilterDialog" max-width="600px">
        <v-card>
          <v-card-title>
            <span class="headline">Filter Options</span>
          </v-card-title>

          <v-card-text>
            <!-- States selection -->
            <h3>Select Your States</h3>
            <v-row>
              <v-col v-for="state in states" :key="state" cols="auto">
                <v-checkbox
                  v-model="tempSelectedStates"
                  :label="state"
                  :value="state"
                />
              </v-col>
            </v-row>

            <!-- Activities selection -->
            <h3>Select Your Activities</h3>
            <v-row>
              <v-col v-for="activity in activities" :key="activity" cols="auto">
                <v-checkbox
                  v-model="tempSelectedActivities"
                  :label="activity"
                  :value="activity"
                />
              </v-col>
            </v-row>

            <!-- Favorites selection -->
            <h3>Favorites</h3>
            <v-switch v-model="tempShowFavoritesOnly" label="Show Favorites Only" />
          </v-card-text>

          <!-- Submit button -->
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-2" dark @click="applyFilter">Submit</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <!-- Detail Popup Dialog -->
      <v-dialog v-model="showDetailDialog" max-width="600px">
        <v-card class="greyish-blue-background">
          <v-card-title>
            <span class="headline">{{ selectedDestination.name || 'Destination Details' }}</span>
          </v-card-title>

          <v-card-text>
            <!-- Destination Image Placeholder -->
            <v-img src="https://via.placeholder.com/400x250" alt="Destination Image" max-height="250px"></v-img>

            <!-- Destination Description -->
            <p v-if="selectedDestination.description">{{ selectedDestination.description }}</p>

            <!-- Location -->
            <p v-if="selectedDestination.location"><strong>Location:</strong> {{ selectedDestination.location }}</p>

            <!-- Rating -->
            <p>
              <strong>Rating:</strong>
              <span>
                <v-icon v-for="star in getStars(selectedDestination.reviewRating)" :key="star" class="gold">{{ star }}</v-icon>
              </span>
            </p>

            <!-- Price Range -->
            <p><strong>Price Range:</strong> $10 - $50</p> <!-- Example placeholder -->

            <!-- Phone Number -->
            <p><strong>Phone Number:</strong> (123) 456-7890</p> <!-- Example placeholder -->

            <!-- Opening Hours -->
            <p><strong>Opening Hours:</strong> 10:00 AM - 10:00 PM</p> <!-- Example placeholder -->
          </v-card-text>

          <!-- Location Button -->
          <v-card-actions>
            <v-btn color="green" :href="getGoogleMapsLink(selectedDestination)" target="_blank">View on Google Maps</v-btn>
            <v-spacer></v-spacer>
            <v-btn @click="showDetailDialog = false">Close</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-main>
  </v-app>
</template>

<script>
import DestinationCard from "@/components/DestinationCard.vue";
import destinationAll from "@/assets/Updated_destination.json";

export default {
  name: "FunctionPage",
  components: {
    DestinationCard
  },
  data() {
    return {
      showFilterDialog: false,
      showDetailDialog: false,
      selectedStates: [],
      selectedActivities: [],
      tempSelectedStates: [],
      tempSelectedActivities: [],
      favoriteDestinations: [], // Array to store favorited destinations
      tempShowFavoritesOnly: false, // Temporary filter for the "Show Favorites" option
      showFavoritesOnly: false, // Actual filter for showing favorites
      states: [
        "Johor", "Kedah", "Kelantan", "Kuala Lumpur", "Melaka", "Negeri Sembilan", 
        "Pahang", "Penang", "Perak", "Perlis", "Putrajaya", "Sabah", "Sarawak", 
        "Selangor", "Terengganu"
      ],
      activities: [
        "Local Specialty", "Leg Day", "Culture Shock", "Cafe Hopping", "Water Experience",
        "Amusement Park", "Shopping Spree"
      ],
      selectedDestination: {},
      destinations: destinationAll,
    };
  },
  methods: {
    applyFilter() {
      this.selectedStates = [...this.tempSelectedStates];
      this.selectedActivities = [...this.tempSelectedActivities];
      this.showFavoritesOnly = this.tempShowFavoritesOnly;
      this.showFilterDialog = false;
    },
    openDetailDialog(destination) {
      this.selectedDestination = destination;
      this.showDetailDialog = true;
    },
    getGoogleMapsLink(destination) {
      if (!destination || !destination.coordinate) return '#';
      const lat = destination.coordinate.latitude; // Accessing latitude
      const lng = destination.coordinate.longitude; // Accessing longitude
      return `https://www.google.com/maps?q=${lat},${lng}`;
    },
    toggleFavorite(destination) {
      const index = this.favoriteDestinations.findIndex(fav => fav.name === destination.name);
      if (index === -1) {
        this.favoriteDestinations.push(destination);
      } else {
        this.favoriteDestinations.splice(index, 1);
      }
    },
    isFavorite(destination) {
      return this.favoriteDestinations.some(fav => fav.name === destination.name);
    },
    getStars(rating) {
      const stars = [];
      const fullStars = Math.floor(rating);
      const halfStars = rating % 1 >= 0.5 ? 1 : 0;
      const emptyStars = 5 - fullStars - halfStars;

      for (let i = 0; i < fullStars; i++) {
        stars.push('mdi-star');
      }
      if (halfStars) {
        stars.push('mdi-star-half-full');
      }
      for (let i = 0; i < emptyStars; i++) {
        stars.push('mdi-star-outline');
      }

      return stars;
    }
  },
  computed: {
    filteredDestinations() {
      return this.destinations.filter((destination) => {
        const stateMatch =
          this.selectedStates.length === 0 ||
          this.selectedStates.includes(destination.state);
        const activityMatch =
          this.selectedActivities.length === 0 ||
          this.selectedActivities.includes(destination.activityCategory);
        const favoriteMatch =
          !this.showFavoritesOnly || this.favoriteDestinations.some(fav => fav.name === destination.name);
        return stateMatch && activityMatch && favoriteMatch;
      });
    }
  }
};
</script>

<style scoped>
.v-btn {
  margin: 10px;
}
.v-img {
  border-radius: 8px;
  margin-bottom: 10px;
}
.gold {
  color: gold;
}
.grey {
  color: grey;
}
.greyish-blue-background {
  background-color: #f0f4f8; /* Example greyish blue */
}
</style>
