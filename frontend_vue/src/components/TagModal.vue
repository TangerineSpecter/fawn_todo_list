<template>
  <div v-if="visible" class="fixed inset-0 z-50 flex items-center justify-center p-4" @click="closeModal">
    <div class="absolute inset-0 bg-black/50 backdrop-blur-sm transition-opacity"></div>
    <div class="relative bg-white dark:bg-slate-800 rounded-lg shadow-xl w-full max-w-md overflow-hidden transition-all"
      @click.stop>
      <div class="p-6">
        <div class="flex items-center justify-between mb-4">
          <h3 class="text-lg font-semibold text-slate-800 dark:text-white">添加新标签</h3>
          <button @click="closeModal"
            class="text-slate-500 hover:text-slate-700 dark:text-slate-400 dark:hover:text-slate-200">
            <Close size="20" />
          </button>
        </div>

        <form @submit.prevent="addTag">
          <div class="space-y-4">
            <div>
              <label for="tagName"
                class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">标签名称</label>
              <input type="text" id="tagName" v-model="tagName"
                class="w-full px-3 py-2 bg-white dark:bg-slate-700 border border-slate-300 dark:border-slate-600 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-sky-500 dark:text-white"
                placeholder="输入标签名称" required>
            </div>

            <div>
              <label class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">选择颜色</label>
              <div class="flex flex-wrap gap-2">
                <button v-for="color in colors" :key="color" type="button"
                  :class="['w-8 h-8 rounded-full transition-all', selectedColor === color ? 'ring-2 ring-offset-2 ring-sky-500 dark:ring-offset-slate-800' : 'hover:scale-110']"
                  :style="{ backgroundColor: color }" @click="selectedColor = color"></button>
              </div>
            </div>
          </div>

          <div class="mt-6 flex justify-end gap-3">
            <button type="button" @click="closeModal"
              class="px-4 py-2 border border-slate-300 dark:border-slate-600 rounded-md text-sm font-medium text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-700/50 transition-colors">
              取消
            </button>
            <button type="submit"
              class="px-4 py-2 bg-sky-500 hover:bg-sky-600 text-white rounded-md text-sm font-medium transition-colors">
              添加
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, defineProps, defineEmits } from 'vue';
import { Close } from '@icon-park/vue-next';
import { useTodoStore } from '../stores/todo';

defineProps({
  visible: {
    type: Boolean,
    required: true
  }
});

const emit = defineEmits(['close']);

const todoStore = useTodoStore();
const tagName = ref('');
const selectedColor = ref('#3b82f6'); // 默认蓝色

// 预设颜色选项
const colors = [
  '#3b82f6', '#10b981', '#8b5cf6', '#ef4444', '#f59e0b',
  '#ec4899', '#14b8a6', '#6366f1', '#f97316', '#84cc16'
];

const addTag = () => {
  if (!tagName.value.trim()) return;

  // 使用store的action添加新标签
  todoStore.addTag(tagName.value.trim(), selectedColor.value);
  tagName.value = '';
  closeModal();
};

const closeModal = () => {
  emit('close');
};
</script>