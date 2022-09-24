<template>
  <codemirror
    v-model="script"
    :style="{ height: initHeight, 'font-size': '14px' }"
    :autofocus="true"
    :indent-with-tab="true"
    :tab-size="2"
    :extensions="extensions"
    :disabled="readOnly"
    :lang="lang"
    @blur="updateScript"
  />
</template>

<script setup>
import { ref, watch } from "vue";
import { Codemirror } from "vue-codemirror";
import { python } from "@codemirror/lang-python";
import { json } from "@codemirror/lang-json";

const props = defineProps({
  content: {
    type: String,
    default: "",
  },
  lang: {
    type: String,
    default: "python",
  },
  readOnly: {
    type: Boolean,
    default: false,
  },
  initHeight:{
    type: String,
    default: "600px",
  }
});

const extensions = [python(), json()];

let script = ref("");

watch(
  () => props.content,
  () => {
    script.value = props.content;
  },
  { immediate: true } // immediate选项可以开启首次赋值监听
);

const emit = defineEmits(["updateScript"]);

const updateScript = () => {
  emit("updateScript", script.value);
};
</script>

<style scoped></style>
