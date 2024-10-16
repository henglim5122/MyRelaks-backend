<template>
  <div id="app" class="chatbot-container">
    <!-- Header Section -->
    <header class="header">
      <h1 class="brand">Mai Relaks</h1>
      <nav>
        <ul class="nav-links">
          <li><a href="#">Home</a></li>
          <li><a href="#">Destinations</a></li>
          <li><a href="#">Activities</a></li>
          <li><a href="#">Itinerary Planning</a></li>
        </ul>
      </nav>
      <button class="sign-in">Sign In</button>
    </header>

    <!-- Chatbot Interface -->
    <div class="chatbot">
      <h2>Hello, Haziq Mudzakir</h2>
      <p>How may I assist you today?</p>

      <div class="buttons">
        <button @click="goToPage('tourist-attractions')">
          Top 10 Tourist Attractions in Malaysia
        </button>
        <button @click="goToPage('popular-activities')">
          Popular Tourist Activities in Malaysia
        </button>
        <button @click="goToPage('build-itinerary')">
          Build an Itinerary for Malaysia
        </button>
      </div>

      <div class="input-box">
        <input type="text" placeholder="Send Message..." v-model="message" />
        <button @click="sendMessage">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: ''
    };
  },
  methods: {
    goToPage(page) {
      alert(`Navigating to: ${page}`);
    },
    sendMessage() {
      alert(`Message sent: ${this.message}`);
      this.message = ''; // Clear input after sending
    }
  }
};
</script>

<style scoped>
/* General Styles */
.chatbot-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #74ebd5, #ACB6E5);
  padding: 20px;
}

/* Header Styling */
.header {
  width: 100%;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.8);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.brand {
  font-size: 1.8rem;
  font-family: 'Courier New', monospace; /* Monospaced font */
  font-weight: bold;
  color: #333;
}

.nav-links {
  display: flex;
  gap: 25px;
}

.nav-links a {
  text-decoration: none;
  color: #333;
  font-family: 'Courier New', monospace; /* Monospaced font */
  font-size: 1rem;
  transition: color 0.3s ease;
}

.nav-links a:hover {
  color: #ACB6E5;
}

.sign-in {
  padding: 10px 20px;
  background-color: #74ebd5;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  color: white;
  font-family: 'Courier New', monospace; /* Monospaced font */
  transition: background-color 0.3s ease;
}

.sign-in:hover {
  background-color: #ACB6E5;
}

/* Chatbot Interface Styling */
.chatbot {
  max-width: 700px;
  margin: 40px auto;
  padding: 30px;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  text-align: center;
}

h2 {
  font-size: 2.5rem;
  font-family: 'Courier New', monospace; /* Monospaced font */
  color: #333;
}

p {
  font-size: 1.2rem;
  margin-bottom: 30px;
  color: #555;
  font-family: 'Courier New', monospace; /* Monospaced font */
}

/* Buttons Styling */
.buttons {
  display: flex;
  flex-direction: column; /* Stacks buttons vertically */
  gap: 15px; /* Adds spacing between the buttons */
  margin-bottom: 20px; /* Add space between buttons and the input box */
}

.buttons button {
  padding: 15px;
  font-size: 1rem; /* Adjust button font size */
  border: none;
  border-radius: 50px;
  background-color: #74ebd5;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
  font-family: 'Courier New', monospace; /* Monospaced font */
  white-space: nowrap; /* Prevent text from wrapping */
}

.buttons button:hover {
  background-color: #ACB6E5;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

/* Input Box Styling */
.input-box {
  margin-top: 20px;
  display: flex;
  gap: 10px;
  align-items: center;
  width: 100%; /* Makes the input-box responsive */
}

input {
  flex-grow: 1;
  padding: 12px 15px;
  border: 2px solid #ddd;
  border-radius: 50px;
  font-family: 'Courier New', monospace; /* Monospaced font */
  outline: none;
  transition: border-color 0.3s ease;
  color: black; /* Ensures text color is black */
  width: 100%; /* Full width for responsive design */
  max-width: none; /* Remove max-width constraint */
  box-sizing: border-box; /* Ensures padding doesn't break the layout */
}

button {
  padding: 12px 20px;
  background-color: #74ebd5;
  border: none;
  border-radius: 50px;
  color: white;
  cursor: pointer;
  font-family: 'Courier New', monospace; /* Monospaced font */
  transition: background-color 0.3s ease;
  flex-shrink: 0; /* Prevent button from shrinking */
}

/* Responsive Design */
@media (max-width: 768px) {
  .buttons {
    flex-direction: column; /* Stack buttons vertically on small screens */
  }
}
</style>
