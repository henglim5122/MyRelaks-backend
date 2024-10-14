<template>
  <v-text-field
    label="Date of Birth *"
    type="date"
    :modelValue="formattedDob"
    @update:modelValue="onDobChange"
    :rules="[(v) => validateRequired(v, 'Date of Birth'), validateAge]"
    required
    class="dob-spacing mt-7"
  ></v-text-field>

  <v-row>
    <v-col cols="3">
      <v-autocomplete
        label="Code *"
        :modelValue="code"
        :items="countryCodes"
        @update:modelValue="$emit('update:code', $event)"
        :rules="[(v) => validateRequired(v, 'Code')]"
        solo
        required
        class="no-margin"
      />
    </v-col>
    <v-col cols="9">
      <v-text-field
        label="Phone No. *"
        :modelValue="phone"
        @update:modelValue="$emit('update:phone', $event)"
        :rules="[
          (v) => validateRequired(v, 'Phone Number'),
          (v) => validateNumeric(v, 'Phone Number'),
        ]"
        required
        class="no-margin"
      />
    </v-col>
  </v-row>

  <v-row>
    <v-col cols="6">
      <v-text-field
        label="City *"
        :modelValue="city"
        @update:modelValue="$emit('update:city', $event)"
        :rules="[
          (v) => validateRequired(v, 'City'),
          (v) => validateAlphabets(v),
        ]"
        required
        class="no-margin"
      />
    </v-col>
    <v-col cols="6">
      <v-autocomplete
        label="Country *"
        :modelValue="country"
        :items="countryNames"
        @update:modelValue="onCountryChange"
        :rules="[(v) => validateRequired(v, 'Country')]"
        solo
        required
        class="no-margin"
      />
    </v-col>
  </v-row>

  <v-text-field
    label="Password *"
    :type="passwordVisible ? 'text' : 'password'"
    :modelValue="password"
    @update:modelValue="$emit('update:password', $event)"
    :rules="[(v) => validateRequired(v, 'Password'), validateMinLength]"
    class="mt-9 no-margin"
    required
    :append-inner-icon="passwordVisible ? 'mdi-eye' : 'mdi-eye-off'"
    @click:append-inner="passwordVisible = !passwordVisible"
  />
  <v-text-field
    label="Confirm Password *"
    :type="confirmPasswordVisible ? 'text' : 'password'"
    :modelValue="confirmPassword"
    @update:modelValue="$emit('update:confirmPassword', $event)"
    :rules="[
      (v) => validateRequired(v, 'Confirm Password'),
      validatePasswordsMatch,
    ]"
    class="mt-4 no-margin"
    required
    :append-inner-icon="confirmPasswordVisible ? 'mdi-eye' : 'mdi-eye-off'"
    @click:append-inner="confirmPasswordVisible = !confirmPasswordVisible"
  />
</template>

<script>
import countries from "@/assets/countries.json";
import { useDateFormatter } from "@/composables/useDateFormatter.js";

export default {
  props: {
    dob: String,
    code: String,
    phone: String,
    city: String,
    country: String,
    password: String,
    confirmPassword: String,
  },
  data() {
    return {
      countryCodes: [], // Stores the dial codes
      countryNames: [], // Stores the country names
      formattedDob: this.dob, // Initializes formatted date of birth
      countryDialMap: {}, // Map of country names to dial codes
      passwordVisible: false, // Track visibility of password
      confirmPasswordVisible: false, // Track visibility of confirm password
    };
  },
  emits: [
    "update:dob",
    "update:code",
    "update:phone",
    "update:city",
    "update:country",
    "update:password",
    "update:confirmPassword",
  ],
  mounted() {
    this.loadCountryData();
    if (this.dob) {
      this.formattedDob = this.formatDate(this.dob); // Format dob if it's already set
    }
  },
  methods: {
    loadCountryData() {
      // Extract the dial codes and country names from the countries JSON
      this.countryCodes = countries.map((country) => country.dial_code);
      this.countryNames = countries.map((country) => country.name);

      // Create a map of country names to their dial codes
      this.countryDialMap = countries.reduce((map, country) => {
        map[country.name] = country.dial_code;
        return map;
      }, {});
    },
    validateRequired(v, fieldName) {
      return !!v || `${fieldName} is required`;
    },
    validateAlphabets(v) {
      return /^[A-Za-z]+$/.test(v) || "Only alphabets are allowed";
    },
    validateMinLength(v) {
      return v.length >= 6 || "Password must be at least 6 characters long";
    },
    validatePasswordsMatch(v) {
      return v === this.password || "Passwords must match";
    },
    validateNumeric(v, fieldName) {
      return /^\d+$/.test(v) || `${fieldName} must contain only numbers`;
    },
    validateAge(v) {
      if (!v) return true; // Skip if dob is empty, will be caught by required validation

      const selectedDate = new Date(v);
      const today = new Date();

      // Calculate the difference in years
      const age = today.getFullYear() - selectedDate.getFullYear();
      const monthDiff = today.getMonth() - selectedDate.getMonth();
      const dayDiff = today.getDate() - selectedDate.getDate();

      // Check if age is under 18 considering the month and day differences
      if (
        age > 18 ||
        (age === 18 && (monthDiff > 0 || (monthDiff === 0 && dayDiff >= 0)))
      ) {
        return true;
      }

      return "You must be at least 18 years old to register";
    },
    onDobChange(newDob) {
      this.formattedDob = newDob;
      const parsedDate = this.parseDate(newDob); // Parse the new date
      this.$emit("update:dob", parsedDate); // Emit the parsed date

      // Run the age validation when the DOB changes
      const ageValid = this.validateAge(newDob);
      if (ageValid !== true) {
        // You could add a custom action here if needed
        console.log("Age validation failed");
      }
    },
    // Use the methods from the composable
    ...useDateFormatter(),

    onDobChange(newDob) {
      this.formattedDob = newDob;
      const parsedDate = this.parseDate(newDob); // Parse the new date
      this.$emit("update:dob", parsedDate); // Emit the parsed date
    },

    onCountryChange(newCountry) {
      this.$emit("update:country", newCountry);

      // Automatically update the code based on the selected country
      const dialCode = this.countryDialMap[newCountry];
      if (dialCode) {
        this.$emit("update:code", dialCode);
      }
    },
  },
};
</script>

<style scoped>
/* Custom style for ensuring fields don't shift during validation */
.no-margin {
  margin-bottom: 0; /* Ensures no additional margins are added during validation */
}

/* Prevent shifting caused by validation messages */
.v-messages__message {
  margin-top: 0;
  margin-bottom: 0;
}

.v-col {
  padding-left: 8px;
  padding-right: 8px;
}

.v-text-field {
  margin-bottom: 20px;
}

input[type="date"] {
  -webkit-appearance: none; /* For Chrome */
  -moz-appearance: none; /* For Firefox */
  appearance: none;
}

.dob-spacing {
  position: relative;
}

.dob-spacing input[type="date"] {
  width: 100%;
}
</style>
