<template>
  <div>HedgeHog Page</div>
</template>

<script>
import router from "../../router";
export default {
  name: "HedgeHogs",
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    checkLoggedIn() {
      router.push("/auth");
    },
  },
};
</script>
