<template>
  <v-app>
    <NavigationBar />

    <v-main>
      <v-container class="text-center my-5" fluid>
        <h1>Hello, Ruben</h1>
        <h3>How may I assist you today?</h3>

        <!-- Bot Interaction Cards -->
        <v-row class="mt-5 justify-space-around">
          <!-- Changed to justify-space-around -->
          <BotCard
            text="Suggest top 10 most visited tourist attractions in Malaysia"
            :onClick="suggestAttractions"
          />
          <BotCard
            text="What are some of the most popular tourist activities in Malaysia?"
            :onClick="popularActivities"
          />
          <BotCard
            text="Build me an itinerary for Malaysia"
            :onClick="buildItinerary"
          />
        </v-row>

        <div class="flex-grow-1"></div>

        <!-- User Input Section (Rounded) -->
        <v-row class="justify-center mb-5">
          <v-col cols="12" md="8">
            <div class="chat-container">
              <input
                type="text"
                v-model="userMessage"
                class="chat-input"
                placeholder="Send message..."
                @keydown.enter="sendMessage"
              />
              <i class="mdi mdi-send send-icon" @click="sendMessage"></i>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import NavigationBar from "@/components/NavigationBar";
import BotCard from "@/components/BotCard.vue";

export default {
  components: {
    NavigationBar,
    BotCard,
  },
  data() {
    return {
      userMessage: "",
    };
  },
  methods: {
    suggestAttractions() {
      alert("Top 10 attractions will be displayed here.");
    },
    popularActivities() {
      alert("Popular tourist activities will be displayed here.");
    },
    buildItinerary() {
      alert("Itinerary suggestions will be generated here.");
    },
    sendMessage() {
      if (this.userMessage.trim() !== "") {
        alert(`You sent the message: "${this.userMessage}"`);
        this.userMessage = "";
      } else {
        alert("Message cannot be empty!");
      }
    },
  },
};
</script>

<style scoped>
html,
body,
#app {
  height: 100%;
  margin: 0;
  padding: 0;
}

.v-container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100vh;
}

.flex-grow-1 {
  flex-grow: 1;
}

.chat-container {
  position: relative;
  width: 100%;
  max-width: 100%;
  margin: 10px 0;
}

.chat-input {
  width: 100%;
  padding: 10px 50px 10px 15px;
  border-radius: 25px;
  border: 2px solid #ccc;
  background-color: transparent;
  color: inherit;
  outline: none;
  font-size: 16px;
  box-sizing: border-box;
}

.send-icon {
  position: absolute;
  top: 50%;
  right: 15px;
  transform: translateY(-50%);
  color: inherit;
  cursor: pointer;
  font-size: 24px;
}
</style>
