<template>
  <h1>You are logged in!</h1>
  <v-btn @click="logout">Log Out</v-btn>
</template>

<script setup>
const logout = () => {
  localStorage.removeItem("authToken");
  window.location.href = "/login";
};
</script>
