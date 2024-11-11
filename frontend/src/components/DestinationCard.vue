<template>
    <v-card :height="height" :width="width" class="mx-auto rounded-lg my-10">
      <div class="d-flex justify-center align-center">
        <v-card-title class="text-h5">{{ destination.name }}</v-card-title>
        <v-spacer></v-spacer>
        <v-icon class="mr-5" @click="isLiked">
          <v-icon v-if="!onLiked">mdi-cards-heart-outline</v-icon>
          <v-icon v-else class="red-heart">mdi-heart</v-icon>
        </v-icon>
      </div>
  
      <v-img 
        v-if="destination.pictureUrl" 
        :src="destination.pictureUrl" 
        alt="Destination Image" 
        max-height="250px"
        class="mb-3"
        error-icon="mdi-image-not-found"
      ></v-img>
  
      <div>
        <v-card-subtitle>
          <strong>{{ destination.location }}, {{ destination.state }}</strong>
          ({{ destination.coordinate.latitude }}, {{ destination.coordinate.longitude }})
        </v-card-subtitle>
        <v-card-text>
          <div class="destinationStyle" id="destinationDescription">
            <strong>{{ destination.description }}</strong>
          </div>
          <div class="destinationStyle">Category: <strong>{{ destination.activityCategory }}</strong></div>
          <div class="destinationStyle">
            Rating: <i><strong :style="textColor(destination.reviewRating)">{{ destination.reviewRating }}</strong></i>
          </div>
        </v-card-text>
      </div>
    </v-card>
  </template>
  
  <script>
  import destination from "@/assets/Updated_destination.json";
  
  export default {
    name: "DestinationCard",
    props: {
      destination: {
        type: Object,
        required: true,
      },
      height: {
        type: String,
        default: "",
      },
      width: {
        type: String,
        default: "",
      },
      isLiked: {
        type: Boolean,
        default: false,
      },
      onLiked: {
        type: Function,
        required: true,
      },
    },
    data() {
      return {
        // No data property needed for image display
      };
    },
    methods: {
      isLiked() {
        this.onLiked = !this.onLiked;
        this.$emit("onLiked");
        console.log(this.onLiked);
      },
  
      textColor(rating) {
        // Color logic for rating display
        // ... same as before
      },
    },
  };
  </script>
  
  <style scoped>
  .v-card {
    width: 80%;
  }
  
  .red-heart {
    color: red;
  }
  
  .destinationStyle {
    margin-top: 20px;
  }
  
  #destinationDescription {
    font-size: larger;
  }
  </style>