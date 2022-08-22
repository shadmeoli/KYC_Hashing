<template>
  <v-app>
    <v-app-bar app color="purple">
      <div class="d-flex align-center">
        <v-chip label color="white lighten-3" >
          <v-icon color="purple">mdi-lock</v-icon>
          <span class="ml-3">KYC Hashing</span>
          </v-chip>
      </div>

      <v-spacer></v-spacer>

      
    </v-app-bar>

    <v-main>
      <LoginPage />
    </v-main>
  </v-app>
</template>

<script>
import LandingPage from './components/LandingPage.vue';
import LoginPage from './components/LoginPage.vue';

export default {
  name: "App",
  data: () => ({
    //
    items: [
      { title: "My transactions" },
      { title: "About us" },
      { title: "Help" }
    ]
  }),
  components: { LoginPage }
};
</script>
