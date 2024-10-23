<template>
  <v-app>
    <v-main>
      <div class="displayNone">
        <router-view />
      </div>

      <div class="displayBlock text-center">
        <v-alert color="error">
          Display is available only on desktop
        </v-alert>                                                                 
      </div>
    </v-main>
  </v-app>
</template>

<script lang="ts" setup></script>

<style>
@media only screen and (max-width: 1440px) {
  .displayNone{
    display: none;
  }
  .displayBlock {
    display: block !important;
  }
}

@media only screen and (min-width: 1441px) {
  .displayBlock {
    display: none;
  }
}
  

</style>


