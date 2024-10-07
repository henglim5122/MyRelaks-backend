<template>
  <v-radio-group
    class="mt-12"
    :modelValue="gender"
    inline
    :rules="[(v) => !!v || 'Gender is required']"
  >
    <v-radio value="male">
      <template v-slot:label>
        <div class="gender-option d-flex align-center">
          <v-avatar size="120" class="mr-2 male-avatar">
            <v-img
              src="@/assets/images/male-icon.png"
              :class="{ 'selected-gender': gender === 'male' }"
            ></v-img>
          </v-avatar>
          <div
            :class="{ 'blue--text': gender === 'male' }"
            class="gender-label"
          >
            MALE
          </div>
        </div>
      </template>
    </v-radio>

    <v-radio value="female">
      <template v-slot:label>
        <div class="gender-option d-flex align-center">
          <v-avatar size="120" class="mr-2 female-avatar">
            <v-img
              src="@/assets/images/female-icon.png"
              :class="{ 'selected-gender': gender === 'female' }"
            ></v-img>
          </v-avatar>
          <div
            :class="{ 'pink--text': gender === 'female' }"
            class="gender-label"
          >
            FEMALE
          </div>
        </div>
      </template>
    </v-radio>
  </v-radio-group>
</template>

<script>
export default {
  props: {
    gender: {
      type: String,
      required: true,
    },
  },
  emits: ["update:gender"],
};
</script>

<style scoped>
.gender-option {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  margin-right: 60px;
  transition: transform 0.3s ease; /* Add smooth scaling effect */
}

.gender-option:hover {
  transform: scale(1.05); /* Scale up on hover for visual feedback */
}

.gender-label {
  font-size: 16px; /* Adjust font size */
  font-weight: bold; /* Make the text bold */
  text-align: center; /* Center the text */
  transition: color 0.3s ease; /* Smooth color transition */
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2); /* Add a subtle shadow for depth */
}

.v-avatar {
  border: 2px solid transparent;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow around avatars */
  border-radius: 50%; /* Ensures avatars are circular */
  overflow: hidden; /* Ensures the image stays circular */
}

.male-avatar {
  background-color: rgba(33, 150, 243, 0.1); /* Light blue background */
}

.female-avatar {
  background-color: rgba(233, 30, 99, 0.1); /* Light pink background */
}

.male-avatar.selected-gender {
  border-color: #2196f3; /* Blue border for selected male */
  background: linear-gradient(
    to bottom right,
    #e3f2fd,
    #bbdefb
  ); /* Gradient for selected male */
  box-shadow: 0 4px 12px rgba(33, 150, 243, 0.4); /* Enhanced shadow on selected */
  transform: scale(1.2); /* Zoom effect when selected */
}

.female-avatar.selected-gender {
  border-color: #e91e63; /* Pink border for selected female */
  background: linear-gradient(
    to bottom right,
    #fce4ec,
    #f8bbd0
  ); /* Gradient for selected female */
  box-shadow: 0 4px 12px rgba(233, 30, 99, 0.4); /* Enhanced shadow on selected */
  transform: scale(1.2); /* Zoom effect when selected */
}

.v-img {
  opacity: 0.6;
  transition: opacity 0.3s ease, transform 0.3s ease; /* Include transform in transition */
}

.selected-gender .v-img {
  opacity: 1;
  transform: scale(1.2); /* Zoom effect for the image */
}

/* Color filters for the icons */
.male-avatar .v-img ::v-deep(img) {
  filter: brightness(0) saturate(100%) invert(39%) sepia(57%) saturate(2406%)
    hue-rotate(196deg) brightness(102%) contrast(95%);
}

.female-avatar .v-img ::v-deep(img) {
  filter: brightness(0) saturate(100%) invert(28%) sepia(83%) saturate(2541%)
    hue-rotate(316deg) brightness(95%) contrast(90%);
}

/* Hide the default radio button */
.v-radio ::v-deep(.v-input--selection-controls__input) {
  display: none;
}
</style>
