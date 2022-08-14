<template>
  <v-container display="flex" centered>
    <v-card dark align="center" width="auto">
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-col>
          <v-col cols="12" sm="8" md="3">
            <v-text-field
              v-model="name"
              :counter="10"
              :rules="nameRules"
              label="First Name"
              required
              solo
            ></v-text-field>

            <v-text-field
              v-model="name"
              :counter="10"
              label="Second/Last Name"
              solo
            ></v-text-field>

            <v-text-field
              class="cols-"
              v-model="email"
              :rules="emailRules"
              label="E-mail"
              required
              solo
            ></v-text-field>

            <v-text-field label="phone number" solo></v-text-field>

            <v-text-field
              :counter="8"
              :rules="passwordRules"
              label="set password"
              solo
            ></v-text-field>

            <v-text-field
              :counter="8"
              :rules="passwordRules"
              label="confirm password"
              solo
            ></v-text-field>
          </v-col>

          <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
            @click="validate"
          >
            <v-icon>mdi-lock</v-icon>
          </v-btn>

          <v-btn color="error" class="mr-4" @click="reset">
            <v-icon>mdi-restore</v-icon>
          </v-btn>

          <v-btn color="warning" @click="resetValidation">
            <v-icon>mdi-autorenew</v-icon>
          </v-btn>
        </v-col>
      </v-form>
    </v-card>
  </v-container>
</template>


<script>
export default {
  data: () => ({
    valid: true,
    name: "",
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => (v && v.length <= 10) || "Name must be less than 10 characters",
    ],
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
    password: "",
    passwordRules: [
      (v) => !!v || "A password is required",
      (v) =>
        (v && v.length <= 8) || "A password should have atleast 8 characters",
    ],

    select: null,
    items: ["Item 1", "Item 2", "Item 3", "Item 4"],
    checkbox: false,
  }),

  methods: {
    validate() {
      this.$refs.form.validate();
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
  },
};
</script>
