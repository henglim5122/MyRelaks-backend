/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App
 */

// Plugins
import { registerPlugins } from "@/plugins";

// Components
import App from "./App.vue";

// Composables
import { createApp } from "vue";

// Import Firebase functions
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore"; // Import Firestore
import { getAuth } from "firebase/auth"; // Import Authentication

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBT9y0-IQAaPxiXgX6CLS9B0lNSHtcK3xM",
  authDomain: "gaia-capstone05-prd.firebaseapp.com",
  projectId: "gaia-capstone05-prd",
  storageBucket: "gaia-capstone05-prd.appspot.com",
  messagingSenderId: "906395275480",
  appId: "1:906395275480:web:ab4829e8139b695af2c7ad",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firestore
const db = getFirestore(app);

// Initialize Authentication
const auth = getAuth(app);

const vueApp = createApp(App);

registerPlugins(vueApp);

vueApp.mount("#app");

export { db, auth }; // Export Firestore and Authentication
