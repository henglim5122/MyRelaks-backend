<template>
  <v-row class="mt-12">
    <v-col cols="6">
      <v-text-field
        label="First Name *"
        :modelValue="firstName"
        :rules="[validateRequired, validateOnlyLetters]"
        required
      />
    </v-col>
    <v-col cols="6">
      <v-text-field
        label="Last Name *"
        :modelValue="lastName"
        :rules="[validateRequired, validateOnlyLetters]"
        required
      />
    </v-col>
  </v-row>

  <v-text-field
    label="Username *"
    :modelValue="username"
    :rules="[validateRequired]"
    class="mt-9"
    required
  />
  <v-text-field
    label="Email *"
    :modelValue="email"
    :rules="[validateRequired, validateEmail]"
    type="email"
    class="mt-4"
    required
  />
</template>

<script>
export default {
  props: {
    firstName: String,
    lastName: String,
    username: String,
    email: String,
  },
  emits: [
    "update:firstName",
    "update:lastName",
    "update:username",
    "update:email",
  ],
  methods: {
    validateRequired(v) {
      return !!v || "Field is required";
    },
    validateOnlyLetters(v) {
      return /^[A-Za-z]+$/.test(v) || "Must contain only letters";
    },
    validateEmail(v) {
      return /.+@.+\..+/.test(v) || "E-mail must be valid";
    },
  },
};
</script>

<style scoped>
.v-text-field {
  margin-bottom: 20px;
}

.v-col {
  padding-left: 8px;
  padding-right: 8px;
}
</style>
