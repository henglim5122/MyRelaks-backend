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
          <h1 class="text-center my-5">Reset Password?</h1>

          <p class="text-center my-5">
            Enter a new password below to change your password
          </p>

          <v-form ref="form" @submit.prevent="submitForm" class="pa-4">
            <!-- New Password Field with Validation -->
            <v-text-field
              v-model="newPassword"
              label="New Password *"
              placeholder="Enter your new password"
              type="password"
              :rules="[
                (v) => !!v || 'New password is required',
                (v) =>
                  v.length >= 6 ||
                  'Password must be at least 6 characters long',
              ]"
              required
              class="mb-2"
            ></v-text-field>

            <!-- Confirm Password Field with Validation -->
            <v-text-field
              v-model="confirmPassword"
              label="Confirm Password *"
              placeholder="Confirm your new password"
              type="password"
              :rules="[
                (v) => !!v || 'Please confirm your password',
                (v) =>
                  v.length >= 6 ||
                  'Confirm password must be at least 6 characters long',
                (v) => v === newPassword || 'Passwords do not match',
              ]"
              required
            ></v-text-field>

            <!-- Submit Button -->
            <v-btn class="mx-auto mt-5" type="submit" color="#013D5A" block>
              Change Password
            </v-btn>
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
      newPassword: "", // Tracks the new password input
      confirmPassword: "", // Tracks the confirmation password input
    };
  },
  methods: {
    async submitForm() {
      // Check if the form is valid before proceeding
      const isValid = this.$refs.form.validate();

      // Additional custom validation for password length and match
      const isLengthValid = this.newPassword.length >= 6;
      const doPasswordsMatch = this.newPassword === this.confirmPassword;

      if (isValid && isLengthValid && doPasswordsMatch) {
        try {
          // Simulate API call to reset the password
          await this.resetPassword(this.newPassword);
          // Show success message
          Swal.fire({
            title: "Success!",
            text: "Your password has been changed successfully.",
            icon: "success",
            confirmButtonText: "Okay",
          });
          // Optionally, reset the input fields
          this.newPassword = "";
          this.confirmPassword = "";
        } catch (error) {
          // Show error message
          Swal.fire({
            title: "Error!",
            text: "Failed to change the password. Please try again.",
            icon: "error",
            confirmButtonText: "Okay",
          });
        }
      } else {
        // Handle validation errors
        if (!isLengthValid) {
          Swal.fire({
            title: "Validation Error!",
            text: "Password must be at least 6 characters long.",
            icon: "warning",
            confirmButtonText: "Okay",
          });
        } else if (!doPasswordsMatch) {
          Swal.fire({
            title: "Validation Error!",
            text: "Passwords do not match.",
            icon: "warning",
            confirmButtonText: "Okay",
          });
        } else {
          Swal.fire({
            title: "Validation Error!",
            text: "Please correct the errors before submitting.",
            icon: "warning",
            confirmButtonText: "Okay",
          });
        }
      }
    },
    // Simulated function to reset the password
    resetPassword(newPassword) {
      return new Promise((resolve, reject) => {
        // Simulating a successful API call
        setTimeout(() => {
          // Here you can implement actual API call logic
          // If success, call resolve(), otherwise reject()
          if (newPassword) {
            resolve();
          } else {
            reject(new Error("Failed to reset password"));
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
