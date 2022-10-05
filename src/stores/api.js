import {ref} from "vue";
import {defineStore} from "pinia";

export const useApiResponseStore = defineStore("apiResponse", () => {
    const resBody = ref("");
    const resHeaders = ref([]);
    const reqContent = ref("");
    const updateResponse = (data) => {
        resBody.value = data["body"];
        resHeaders.value = data["headers"];
        reqContent.value = data["content"];
    };

    return {resBody, resHeaders, reqContent, updateResponse};
});

export const useApiRequestStore = defineStore("apiRequest", () => {
    const reqParams = ref([]);
    const reqHeaders = ref([]);
    const reqBodyType = ref("NONE");
    const reqFormBody = ref([]);
    const reqJsonBody = ref("");
    const reqApiCategory = ref("");
    const reqApi = ref("");

    const resetData = () => {
        reqParams.value = [];
        reqHeaders.value = [];
        reqBodyType.value = "NONE";
        reqFormBody.value = [];
        reqJsonBody.value = "";
        reqApiCategory.value = "";
        reqApi.value = "";
    }

    const updateRequest = (api) => {
        // 增加初始化步骤，避免切换时数据影响
        resetData();
        reqApi.value = api;
        if (api.params != null) {
            reqParams.value = JSON.parse(api.params)
        }
        if (api.headers != null) {
            reqHeaders.value = JSON.parse(api.headers)
        }
        reqBodyType.value = api.body_type
        switch (api.body_type) {
            case "JSON":
                reqJsonBody.value = api.body;
                break;
            case "FORM":
                reqFormBody.value = JSON.parse(api.body);
                break;
            default:
                break;
        }
        reqApiCategory.value = api.category;
    }

    return {
        reqParams,
        reqBodyType,
        reqFormBody,
        reqJsonBody,
        reqHeaders,
        reqApiCategory,
        reqApi,
        resetData,
        updateRequest
    };
});