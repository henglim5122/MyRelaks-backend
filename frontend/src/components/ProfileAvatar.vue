<template>
  <div class="avatar-container">
    <v-avatar
      :color="color"
      :size="size"
      class="mb-4"
      @click="selectFile"
      style="cursor: pointer"
    >
      <img
        v-if="profileImage"
        :src="profileImage"
        alt="Profile"
        class="profile-image"
      />
      <v-icon v-else icon="mdi-account-circle" :size="size / 2"></v-icon>
    </v-avatar>
    <v-file-input
      ref="fileInput"
      v-show="false"
      @change="onFileChange"
      accept="image/*"
      :rules="fileRules"
    ></v-file-input>
    <v-btn
      v-if="profileImage"
      icon
      class="mt-2 delete-btn"
      @click="removeProfileImage"
    >
      <v-icon>mdi-delete</v-icon>
    </v-btn>
  </div>
</template>

<script>
export default {
  props: {
    profileImage: String,
    fileRules: Array,
    size: {
      type: Number,
      default: 80, // Default avatar size
    },
    color: {
      type: String,
      default: "grey", // Default avatar color
    },
  },
  methods: {
    selectFile() {
      this.$refs.fileInput.click();
    },
    onFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.$emit("update:profileImage", e.target.result);
        };
        reader.readAsDataURL(file);
      }
    },
    removeProfileImage() {
      this.$emit("update:profileImage", null);
      this.$refs.fileInput.reset();
    },
  },
};
</script>

<style scoped>
.avatar-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.profile-image {
  object-fit: cover;
  border-radius: 50%;
}

.delete-btn {
  margin-top: 8px;
  align-self: center; /* Center the bin icon below the avatar */
}
</style>
