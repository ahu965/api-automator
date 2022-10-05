import { ref } from "vue";
import { defineStore } from "pinia";

export const useApiResponseStore = defineStore("apiResponse", () => {
  const resBody = ref("");
  const resHeaders = ref([]);
  const reqContent = ref("");
  const updateResponse = (data) => {
    resBody.value = data["body"];
    resHeaders.value = data["headers"];
    reqContent.value = data["content"];
  };

  return { resBody, resHeaders, reqContent, updateResponse };
});
