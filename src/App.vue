<template>
  <v-app>
    <v-app-bar app color="secondary" dark>
      <v-chip label elevation="5" pill color="red lighten-1 white--text"
        >KYC Hash</v-chip
      >

      <v-spacer></v-spacer>

      <div>
        <v-row>
          <v-text-field
            elevation="4"
            color="secondary"
            class="text-center mt-5"
            label="HashBase"
            solo
            dense
          ></v-text-field>
          <v-btn class="mt-5 mr-10" elevation="4" color="secondary">
            <v-icon>mdi-magnify</v-icon>
          </v-btn>
        </v-row>
      </div>
    </v-app-bar>

    <v-main align="center">
      <LandingPage />
      <HomeView />
    </v-main>
  </v-app>
</template>

<script>
import LandingPage from "./components/LandingPage.vue";
import HomeView from "./views/HomeView.vue";

export default {
  name: "App",
  data: () => ({
    //
  }),
  components: { LandingPage, HomeView },
};
</script>
