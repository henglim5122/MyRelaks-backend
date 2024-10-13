<template>
  <v-app>
    <v-main class="d-flex align-center justify-center">
      <v-container>
        <h1 class="text-center mb-6 text-black title">Mai Relaks</h1>
        <v-responsive
          class="mx-auto border-sm pa-6 rounded-lg bg-grey-lighten-5"
          max-width="400"
        >
          <h1 class="text-center my-5">Forgot Password?</h1>

          <p class="text-center my-5">
            That’s okay, insert your email address to reset your password
          </p>

          <v-form
            fast-fail
            ref="form"
            @submit.prevent="submitForm"
            class="pa-4"
          >
            <!-- Email Field with Validation -->
            <v-text-field
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

            <!-- Submit Button -->
            <v-btn class="mx-auto mt-5" type="submit" color="#013D5A" block>
              Submit
            </v-btn>

            <!-- Sign In Link -->
            <p class="text-center my-5">
              Remember your password?
              <RouterLink to="/login">
                <a class="text-decoration-underline">Log In</a>
              </RouterLink>
              here
            </p>
          </v-form>
        </v-responsive>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Swal from "sweetalert2";

export default {
  data() {
    return {
      email: "", // Tracks the email input
    };
  },
  methods: {
    async submitForm() {
      // Check if the form is valid before proceeding
      if (this.$refs.form.validate()) {
        try {
          // Simulate API call to send the email
          await this.sendResetPasswordEmail(this.email);
          // Show success message
          Swal.fire({
            title: "Success!",
            text: "An email has been sent for password reset.",
            icon: "success",
            confirmButtonText: "Okay",
          });
          // Optionally, reset the email input field
          this.email = "";
        } catch (error) {
          // Show error message
          Swal.fire({
            title: "Error!",
            text: "Failed to send the email. Please try again.",
            icon: "error",
            confirmButtonText: "Okay",
          });
        }
      }
    },
    // Simulated function to send a reset password email
    sendResetPasswordEmail(email) {
      return new Promise((resolve, reject) => {
        // Simulating a successful API call
        setTimeout(() => {
          // Here you can implement actual API call logic
          // If success, call resolve(), otherwise reject()
          if (email === "test@example.com") {
            // Simulating a specific email check
            resolve();
          } else {
            reject(new Error("Failed to send email"));
          }
        }, 1000); // Simulate network delay
      });
    },
  },
};
</script>

<style scoped>
.v-btn {
  min-width: 80%;
}

.title {
  font-family: "Kaushan Script", sans-serif;
}
</style>
