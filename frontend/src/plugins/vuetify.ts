/**
 * plugins/vuetify.ts
 *
 * Framework documentation: https://vuetifyjs.com
 */

// Styles
import "@mdi/font/css/materialdesignicons.css";
import "vuetify/styles";

// Composables
import { createVuetify } from "vuetify";

// Custom theme definition
const myCustomLightTheme = {
  dark: false, // This is a light theme
  colors: {
    background: "#fcf3f3", // Custom background color
    surface: "#ffffff", // Surface color, change as needed
    primary: "#fcf3f3", // You can add more custom colors like 'primary'
    secondary: "#8e44ad", // Add a secondary color (example)
    error: "#b71c1c",
    info: "#2196f3",
    success: "#4caf50",
    warning: "#fb8c00",
  },
};

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
export default createVuetify({
  theme: {
    defaultTheme: "myCustomLightTheme", // Set your custom theme as default
    themes: {
      myCustomLightTheme, // Register the custom theme
    },
  },
});
