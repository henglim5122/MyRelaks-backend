<template>
  <v-col cols="12" md="4" lg="3">
    <v-card class="bot-card blue-card" @click="onClick" hover>
      <v-card-text>
        {{ text }}
      </v-card-text>
    </v-card>
  </v-col>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      required: true,
    },
    onClick: {
      type: Function,
      required: true,
    },
  },
};
</script>

<style scoped>
.bot-card {
  padding: 15px;
  cursor: pointer;
  min-height: 120px; /* Adjust height to your needs */
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  max-width: 100%; /* Set a max-width to control card size */
  margin: auto; /* Center the card */
}

.blue-card {
  background-color: rgba(1, 61, 90);
  color: white;
}
</style>
