<template>
  <v-app>
    <NavigationBar :subscribeBtn="false" />
    <v-main class="d-flex align-center justify-center">
      <v-container>
        <div class="d-flex align-center justify-center">
          <v-img
            src="../assets/logo2_coloured.png"
            id="logo-img"
            width="150"
            height="150"
            class="mb-10"
          ></v-img>
        </div>
        <v-responsive class="mx-auto border-sm pa-6 rounded-lg bg-grey-lighten-5" max-width="400">
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
            <v-btn class="mx-auto mt-5" type="submit" color="#013D5A" block>Login</v-btn>

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
import Swal from 'sweetalert2'; // Import Swal2
// import { loginUser } from '@/stores/userStore';

const email = ref('');
const password = ref('');
const passwordVisible = ref(false);
// Define email validation regex
const emailRegex = /.+@.+\..+/;

const submitForm = async () => {
  if (!email.value || !password.value) {
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: 'Both Email and Password are required!',
    });
    return;
  }

  if (!emailRegex.test(email.value)) {
    Swal.fire({
      icon: 'error',
      title: 'Invalid Email',
      text: 'Please enter a valid email address!',
    });
    return;
  }

  try {
    await loginUser(email.value, password.value); // Call async function
  } catch (error) {
    Swal.fire({
      icon: 'error',
      title: 'Login Failed',
      text: 'Invalid email or password.',
    });
    console.error('Error in submitForm:', error);
  }
};
</script>

<style scoped>
.logo {
  height: 100%;
  width: 10%;
  margin-left: 30px;
}
</style>
