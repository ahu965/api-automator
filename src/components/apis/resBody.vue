<template>
  <div class="res-body">
    <api-coder
      :lang="json"
      :initHeight="'250px'"
      :content="apiResponse.resBody"
      @updateScript="updateContent"
    ></api-coder>
  </div>
</template>

<script setup>
import ApiCoder from "@/components/ApiCoder.vue";
import { useApiResponseStore } from "../../stores/api";

const apiResponse = useApiResponseStore();

const updateContent = (content) => {
  apiResponse.resBody = content;
};
</script>

<style lang="scss">
.res-body {
}
</style>
