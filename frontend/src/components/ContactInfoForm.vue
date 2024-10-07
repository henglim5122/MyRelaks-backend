<template>
  <v-text-field
    label="Date of Birth *"
    type="date"
    :modelValue="formattedDob"
    @update:modelValue="onDobChange"
    :rules="[validateRequired]"
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
        :rules="[validateRequired]"
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
        :rules="[validateRequired]"
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
        :rules="[validateRequired]"
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
        :rules="[validateRequired]"
        solo
        required
        class="no-margin"
      />
    </v-col>
  </v-row>

  <v-text-field
    label="Password *"
    type="password"
    :modelValue="password"
    @update:modelValue="$emit('update:password', $event)"
    :rules="[validateRequired]"
    class="mt-9 no-margin"
    required
  />
  <v-text-field
    label="Confirm Password *"
    type="password"
    :modelValue="confirmPassword"
    @update:modelValue="$emit('update:confirmPassword', $event)"
    :rules="[validateRequired, validatePasswordsMatch]"
    class="mt-4 no-margin"
    required
  />
</template>

<script>
import countries from "./../countries.json";
import { useDateFormatter } from "@/composables/useDateFormatter";

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
    validateRequired(v) {
      return !!v || "Field is required";
    },
    validatePasswordsMatch(v) {
      return v === this.password || "Passwords must match";
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

.dob-spacing {
  margin-bottom: 20px; /* Adjust spacing for Date of Birth */
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

/* For Chrome, Safari, Edge (WebKit-based browsers) */
input[type="date"] {
  padding-right: 40px; /* Create space for the native calendar icon */
  position: relative;
  display: inline-block;
}

input[type="date"]::-webkit-calendar-picker-indicator {
  position: absolute;
  right: 10px; /* Adjust the right value to move it all the way to the end */
  padding: 0;
  cursor: pointer;
}

input[type="date"]::-webkit-inner-spin-button,
input[type="date"]::-webkit-clear-button {
  display: none; /* Optional: Hide the spin and clear buttons */
}

input[type="date"]::-webkit-calendar-picker-indicator {
  opacity: 1;
  width: auto;
}
</style>
