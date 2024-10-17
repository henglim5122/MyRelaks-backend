<template>
  <v-footer id="LandingFooter" class="border-lg">
    <v-container>
      <v-row>
        <v-col>
          <v-col cols="12" sm="12" md="12" id="title"> MY RELAKS </v-col>
          <v-col cols="12" sm="12" md="12"></v-col>
          <v-col cols="12" sm="12" md="12">
            Your gateway to discovering the hidden gems and cultural treasures
            of Malaysia
          </v-col>
        </v-col>
        <v-col>
          <v-col cols="12" sm="12" md="12" class="d-flex justify-center">
            <router-link to="/AboutUs" class="link">About Us</router-link>
            <v-spacer></v-spacer>
            <router-link to="/registration" target="_blank" class="link"
              >Sign Up</router-link
            >
            <v-spacer></v-spacer>
          </v-col>
          <v-col cols="12" sm="12" md="12">
            <v-icon>mdi-map-marker</v-icon>
            53-61, Jalan SS 22/23, Damansara Jaya, 47400 Petaling Jaya, Selangor
          </v-col>
          <v-col cols="12" sm="12" md="12" class="d-flex justify-center">
            <v-icon>mdi-phone</v-icon>
            +60123456789
            <v-spacer></v-spacer>
            <v-icon>mdi-copyright</v-icon>Copyright 2024
          </v-col>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<style scoped>
#LandingFooter {
  background-color: rgba(1, 61, 90);
}

.v-container {
  color: white;
}

.link {
  color: white !important;
}

#title {
  font-weight: bold;
  font-size: x-large;
}
</style>
