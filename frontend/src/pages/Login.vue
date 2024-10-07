<template>
  <v-app>
    <v-main class="d-flex align-center justify-center">
      <v-container>
        <h1 class="text-center mb-6">Mai Relaks</h1>
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
              type="password"
              :rules="[(v) => !!v || 'Password is required']"
              required
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
            <p class="text-center my-5 text-subtitle-2">
              Forgot
              <RouterLink to="/forgotpassword">
                <a class="text-decoration-underline">Username/Password</a>
              </RouterLink>
            </p>
          </v-form>
        </v-responsive>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    submitForm() {
      if (this.$refs.form.validate()) {
        // Handle form submission
        alert("Form is valid and submitted.");
      }
    },
  },
};
</script>
