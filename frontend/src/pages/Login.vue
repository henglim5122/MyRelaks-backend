<template>
  <v-app>
    <v-main class="d-flex align-center justify-center">
      <v-container>
        <div class="d-flex align-center justify-center">
          <v-img
            src="../assets/logo2_coloured.png"
            id="logo-img"
            width="100"
            height="100"
            class="mb-10"
          ></v-img>
        </div>
        <v-responsive
          class="mx-auto border-sm pa-6 rounded-lg bg-grey-lighten-5"
          max-width="400"
        >
          <h1 class="text-center my-5">Login Account</h1>

          <v-form fast-fail @submit.prevent="submitForm" class="pa-4">
            <!-- Email Field -->

            <v-text-field
              class="mb-5"
              v-model="email"
              label="Email Address *"
              placeholder="johndoe@gmail.com"
              type="email"
              :rules="[
                (v) => !!v || 'Email is required',
                (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid',
              ]"
              required
            ></v-text-field>

            <!-- Password Field -->

            <v-text-field
              v-model="password"
              label="Password *"
              placeholder="Enter your password"
              :type="passwordVisible ? 'text' : 'password'"
              :rules="[(v) => !!v || 'Password is required']"
              required
              :append-inner-icon="passwordVisible ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append-inner="passwordVisible = !passwordVisible"
            ></v-text-field>

            <!-- Login Button -->
            <v-btn class="mx-auto mt-5" type="submit" color="#013D5A" block
              >Login</v-btn
            >

            <!-- Registration Link -->
            <p class="text-center my-5">
              Already have an account?
              <RouterLink to="/registration">
                <a class="text-decoration-underline">Register here</a>
              </RouterLink>
            </p>

            <!-- Forgot Password Link -->
            <p class="text-center my-5 text-subtitle-3">
              Forgot Password? Click
              <RouterLink to="/ForgotPassword"
                ><a class="text-decoration-underline">here</a></RouterLink
              >
            </p>
          </v-form>
        </v-responsive>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import Swal from "sweetalert2"; // Import Swal2

const email = ref("");
const password = ref("");
const passwordVisible = ref(false);
// Define email validation regex
const emailRegex = /.+@.+\..+/;

const submitForm = () => {
  // Check if the email or password fields are empty
  if (!email.value || !password.value) {
    // Show error using SweetAlert2 if fields are empty
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Both Email and Password are required!",
    });
    return; // Stop execution if fields are empty
  }

  // Validate the email using regex
  if (!emailRegex.test(email.value)) {
    Swal.fire({
      icon: "error",
      title: "Invalid Email or Password",
      text: "Please enter a valid email address or password!",
    });
    return; // Stop execution if email is invalid
  }

  // Generate random token and save in localStorage if form is valid
  const tokenKey = "authToken";
  const randomChars = Array.from({ length: 12 }, () =>
    Math.random().toString(36).charAt(2)
  ).join("");
  localStorage.setItem(tokenKey, randomChars);

  // Redirect to the logged-in page
  window.location.href = "/loggedin";
};
</script>

<style scoped>
.logo {
  height: 100%;
  width: 10%;
  margin-left: 30px;
}
</style>
