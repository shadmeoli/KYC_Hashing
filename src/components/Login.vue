<template>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center" dense>
          <v-col cols="12" sm="8" md="4" lg="4">         
            <v-card elevation="0">
              <div class="text-center">
                <h1 class="mb-2">Login</h1>
              </div>
              <a href="" name="KYC_Hashing" title="KYC_Hashing" target="_blank">
                <v-img src="@/assets/logo.svg" alt="KYC_Hashing" contain height="200"></v-img>
              </a>
              <v-card-text>
                <v-form>
                  <v-text-field label="Enter your email" name="email" prepend-inner-icon="mdi-email" type="email" class="rounded-5" color="purple" outlined></v-text-field>
                  <v-text-field label="Enter your password" name="password" prepend-inner-icon="mdi-lock" type="password" class="rounded-4" color="purple" outlined></v-text-field>
                  <a href="../components/ForgotPassword.vue" class="pl-6" style="color: purple; float: right;">Forgot Password?</a>
                  <v-btn class="rounded-5" color="purple" x-large block dark>Login</v-btn>
                  <v-card-actions class="text--secondary">
                    <v-checkbox color="#000000" label="Remember me"></v-checkbox>
                    <v-spacer></v-spacer>
                    No account? <a href="../components/Register.vue" class="pl-2" style="color: purple">Sign Up</a>
                  </v-card-actions>
                </v-form>
              </v-card-text>
              <v-card-actions class="ml-6 mr-6 text-center">
                <p>By continuing, you agree to KYC_Hashing's <a href="#" class="pr-2 pl-2" style="color: purple">Policy </a> and <a href="#" class="pl-2" style="color: purple">Terms of Use</a></p>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
</template>

<script>
export default {
  name: 'app-login'
}
</script>

<style lang="css" scoped>
</style>