<template>
  <v-app>
    <NavigationBar @subscribe="subscribe" />

    <v-main :class="{ blur: paymentActive }">
      <v-container class="text-center my-5" fluid :class="{ 'blur-background': subscribePopup }">
        <h1 v-if="userName">Hello, {{ username }}</h1>
        <h1 v-else>Hello, Team 5</h1>
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
          <BotCard text="Build me an itinerary for Malaysia" :onClick="buildItinerary" />
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

      <div v-if="subscribePopup" class="subscriptionPopup text-center overlay">
        <div class="d-flex justify-center align-center mx-5">
          <v-spacer></v-spacer>
          <h1 class="my-3 ml-10">Get Your Offer Now</h1>
          <v-spacer></v-spacer>
          <v-icon @click="closePopUp">mdi-close</v-icon>
        </div>
        <div class="aligncenter">
          <v-row>
            <v-col v-for="(tier, index) in subscriptionTier" :key="index" col="12">
              <v-btn class="tierStyle"
                ><div @click="selectTier(tier)">{{ tier }}</div></v-btn
              >
            </v-col>
          </v-row>
        </div>
        <div class="tierSelected">
          <LandingSubscription
            height="450px"
            width="325px"
            :isSingle="true"
            :tier="selectedTier"
            @pay="openPayment"
          />
        </div>
      </div>
    </v-main>
    <div v-if="paymentActive" class="overlay-payment">
      <Payment :paymentAmount="selectedSub.price" @close="paymentActive = false" />
    </div>
  </v-app>
</template>

<script>
import NavigationBar from '@/components/NavigationBar';
import BotCard from '@/components/BotCard.vue';

export default {
  components: {
    NavigationBar,
    BotCard,
  },
  data() {
    return {
      userMessage: '',
      subscribePopup: false,
      subscriptionTier: ['Freemium', 'Starter', 'Intermediate', 'Pro'],
      selectedTier: ['Freemium'],
      active: false,
      paymentActive: false,
      selectedSub: '',
    };
  },
  methods: {
    suggestAttractions() {
      alert('Top 10 attractions will be displayed here.');
    },
    popularActivities() {
      alert('Popular tourist activities will be displayed here.');
    },
    buildItinerary() {
      alert('Itinerary suggestions will be generated here.');
    },
    sendMessage() {
      if (this.userMessage.trim() !== '') {
        alert(`You sent the message: "${this.userMessage}"`);
        this.userMessage = '';
      } else {
        alert('Message cannot be empty!');
      }
    },
    closePopUp() {
      this.subscribePopup = false;
      this.selectedTier = ['Freemium'];
    },
    subscribe() {
      this.subscribePopup = !this.subscribePopup;
      // console.log(this.subscribePopup);
    },
    selectTier(tier) {
      if (!this.selectedTier.includes(tier)) {
        if (this.selectedTier.length > 2) {
          this.selectedTier.shift();
        }
        this.selectedTier.push(tier);
      } else if (tier !== 'Freemium') {
        this.selectedTier.splice(this.selectedTier.indexOf(tier), 1);
        // console.log(this.selectedTier);
      }
    },
    openPayment(subscription) {
      this.selectedSub = subscription;
      this.paymentActive = true;
      this.subscribePopup = false;
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
  color: rgba(1, 61, 90);
}
.blur-background {
  filter: blur(10px);
  transition: filter 0.15s ease;
}
.tierStyle {
  font-weight: bold;
  font-size: 20px;
  border: black 1px solid;
  border-radius: 10px;
}
.subscriptionPopup {
  position: absolute;
  left: 50%;
  top: 55%;
  transform: translateX(-50%) translateY(-50%);
  background-color: white;
  height: 600px;
  width: 1300px;
  /* cursor: pointer; */
  border: 1px solid black;
  box-shadow: 3px 3px 3px 3px rgba(0, 0, 0, 0.2);
  border-radius: 20px;
  z-index: 9999;
}

.overlay {
  position: fixed;
  z-index: 50;
}

.blur {
  filter: blur(8px);
  transition: filter 0.3s ease;
}
.overlay-payment {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent dark overlay */
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.tierSelected {
  margin-top: 10px;
}
</style>
