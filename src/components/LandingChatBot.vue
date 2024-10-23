<template>
  <v-img src="@/assets/beach.jpg" :height="height" cover>
    <v-row class="fill-height">
      <v-col cols="7" md="7" sm="7">
        <v-container class="ml-15">
          <v-row><v-text id="chat-bot-text-1">Personalise</v-text></v-row>
          <v-row
            ><v-text id="chat-bot-text-2">Your Itinerary With </v-text></v-row
          >
          <v-row><v-text id="chat-bot-text-3">MY RELAKS !</v-text></v-row>

          <br /><br /><br /><br /><br /><br /><br /><br /><br />
          <v-row
            ><v-text id="chat-bot-text-4"
              >Plan with ease, explore, and enjoy – <br />your journey begins
              here with AI
            </v-text></v-row
          >
        </v-container>
      </v-col>
      <v-col cols="5" md="5" sm="5" class="d-flex justify-center align-center">
        <v-row justify="center">
          <v-container class="d-flex justify-center align-center">
            <v-card
              class="chat-bot-card"
              width="400px"
              height="400px"
              lass="mx-auto"
            >
              <v-card-title id="chat-bot-card-title">
                Here are a few simple examples of how you can ask the chatbot
                about itinerary planning</v-card-title
              >
              <v-card-subtitle class="mx-auto">
                <v-card-text class="chat-bot-question-example">
                  <ol>
                    <v-card-text>
                      <li>
                        Plan a 4-person trip to Selangor for next weekend?
                      </li>
                      <li>What can 6 of us do in Johor for 3 days?"</li>
                      <li>
                        Plan a 4-person trip to Selangor for next weekend?
                      </li>
                    </v-card-text>
                  </ol>
                </v-card-text>
              </v-card-subtitle>
              <br />
              <v-card-actions class="justify-center">
                <a href="/chatbot" target="_blank"><v-btn
                  id="chat-bot-button"
                  color="primary"
                  rounded="xl"
                  variant="flat"
                  class="align-center"
                  width="150px"
                  >Try Me!</v-btn
                ></a></v-card-actions
              >
            </v-card></v-container
          >
        </v-row>
      </v-col></v-row
    >
  </v-img>
</template>

<script>
export default {
  props: {
    src: {
      type: String,
      default: "",
    },
    height: {
      type: String,
      default: "",
    },
  },
};
</script>

<style scoped>
#chat-bot-text-1 {
  color: white;
  font-size: 100px;
  font-weight: bolder;
  -webkit-text-stroke: 1.5px black;
}

#chat-bot-text-2 {
  font-size: 50px;
  font-weight: bolder;
  color: black;
}

#chat-bot-text-3 {
  color: white;
  font-size: 40px;
  font-weight: bolder;
  -webkit-text-stroke: 1px black;
}

#chat-bot-text-4 {
  font-size: 20px;
  color: black;
}

#chat-bot-card {
  background-color: white;
  border-radius: 10px;
  border-color: black;
}

#chat-bot-card-title {
  margin: auto;
  text-wrap: wrap;
  justify-content: center;
  text-align: center;
  font-size: 22px;
}

.chat-bot-question-example {
  font-size: 16px;
  margin-top: 10px;
  text-wrap: wrap;
  color: black;
  font-weight: bold;
  border: solid 1px black;
  border-radius: 10px;
}

#chat-bot-button {
}
</style>
