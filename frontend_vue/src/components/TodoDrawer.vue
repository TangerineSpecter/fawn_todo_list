<!-- src/components/TodoDrawer.vue -->
<template>
  <Teleport to="body">
    <Transition name="drawer-fade">
      <!-- 遮罩层 -->
      <div v-if="isOpen" @click="closeDrawer" class="fixed inset-0 bg-slate-900/50 z-40 backdrop-blur-sm"></div>
    </Transition>
    <Transition name="drawer-slide">
      <!-- 抽屉面板 -->
      <div v-if="isOpen"
        class="fixed top-0 right-0 h-full w-full max-w-md bg-slate-50 dark:bg-slate-800 shadow-2xl z-50 flex flex-col">
        <template v-if="editableTodo">
          <!-- 头部 -->
          <header
            class="flex items-center justify-between p-4 border-b border-slate-200 dark:border-slate-700 flex-shrink-0">
            <h2 class="text-lg font-semibold text-slate-800 dark:text-slate-100">任务详情</h2>
            <button @click="closeDrawer" class="btn btn-sm btn-ghost btn-circle">
              <Close theme="outline" size="20" />
            </button>
          </header>

          <!-- 主体内容区 -->
          <main class="flex-grow p-6 overflow-y-auto">
            <div class="space-y-6">
              <!-- 任务标题 -->
              <input v-model="editableTodo.text"
                class="w-full text-2xl font-bold bg-transparent focus:outline-none text-slate-900 dark:text-white" />

              <!-- 分类选择 -->
              <div class="flex items-center gap-4">
                <div
                  class="flex h-10 w-10 items-center justify-center rounded-lg bg-sky-100 dark:bg-sky-500/20 text-sky-500">
                  <AllApplication theme="outline" size="20" :strokeWidth="3" />
                </div>
                <div>
                  <label class="text-sm font-medium text-slate-500 dark:text-slate-400">分类</label>
                  <select v-model="editableTodo.category" class="select select-sm select-ghost -ml-2 dark:text-white">
                    <option value="work">工作</option>
                    <option value="life">生活</option>
                    <option value="study">学习</option>
                    <option value="daily">日常</option>
                  </select>
                </div>
              </div>

              <!-- 标签管理 -->
              <div class="flex items-start gap-4">
                <div
                  class="flex h-10 w-10 items-center justify-center rounded-lg bg-violet-100 dark:bg-violet-500/20 text-violet-500 flex-shrink-0">
                  <TagOne theme="outline" size="20" :strokeWidth="3" />
                </div>
                <div class="flex-1">
                  <label class="text-sm font-medium text-slate-500 dark:text-slate-400">标签</label>
                  <div class="mt-2 flex flex-wrap gap-2">
                    <span v-for="tag in editableTodo.tags" :key="tag" class="badge badge-info badge-outline gap-2">
                      {{ tag }}
                      <button @click="removeTag(tag)" class="opacity-50 hover:opacity-100">
                        <Close theme="outline" size="12" />
                      </button>
                    </span>
                    <input v-model="newTag" @keyup.enter="addTag" placeholder="+ 添加标签"
                      class="input input-xs input-ghost bg-transparent focus:outline-none flex-1 min-w-[80px]" />
                  </div>
                </div>
              </div>

              <!-- 备注 -->
              <div class="flex items-start gap-4">
                <div
                  class="flex h-10 w-10 items-center justify-center rounded-lg bg-amber-100 dark:bg-amber-500/20 text-amber-500 flex-shrink-0">
                  <Memo theme="outline" size="20" :strokeWidth="3" />
                </div>
                <div class="flex-1">
                  <label class="text-sm font-medium text-slate-500 dark:text-slate-400">备注</label>
                  <textarea v-model="editableTodo.notes"
                    class="textarea textarea-bordered w-full mt-2 h-32 dark:bg-slate-700"
                    placeholder="添加一些备注信息..."></textarea>
                </div>
              </div>
            </div>
          </main>

          <!-- 底部操作栏 -->
          <footer
            class="flex items-center justify-between p-4 border-t border-slate-200 dark:border-slate-700 flex-shrink-0">
            <button @click="handleDeleteTask" class="btn btn-error btn-outline btn-sm gap-2">
              <Delete theme="outline" size="16" />
              删除任务
            </button>
            <button @click="handleSaveChanges" class="btn btn-primary btn-sm">保存更改</button>
          </footer>
        </template>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import type { PropType } from 'vue';
import { Close, Delete, AllApplication, TagOne } from '@icon-park/vue-next';
import Todo from './TheMain.vue'; // 调整为你的主组件路径

const props = defineProps({
  isOpen: {
    type: Boolean,
    required: true,
  },
  todo: {
    type: Object as PropType<InstanceType<typeof Todo> | null>,
    default: null,
  },
});

const emit = defineEmits(['update:isOpen', 'update-todo', 'delete-todo']);

const editableTodo = ref<InstanceType<typeof Todo> | null>(null);
const newTag = ref('');

// 监听抽屉的打开状态，当打开时，深度拷贝传入的 todo 对象
// 这样可以避免直接修改 prop，并在用户取消时不保存更改
watch(
  () => props.isOpen,
  (newVal) => {
    if (newVal && props.todo) {
      editableTodo.value = JSON.parse(JSON.stringify(props.todo));
    } else {
      // 清空数据，避免下次打开时闪烁旧数据
      editableTodo.value = null;
    }
  }
);

const closeDrawer = () => {
  emit('update:isOpen', false);
};

const handleSaveChanges = () => {
  if (editableTodo.value) {
    emit('update-todo', editableTodo.value);
    closeDrawer();
  }
};

const handleDeleteTask = () => {
  if (editableTodo.value) {
    // 可以在这里加一个确认弹窗
    if (confirm(`确定要删除任务 "${editableTodo.value.text}" 吗？`)) {
      emit('delete-todo', editableTodo.value.id);
      closeDrawer();
    }
  }
};

const addTag = () => {
  if (newTag.value.trim() && editableTodo.value && !editableTodo.value.tags.includes(newTag.value.trim())) {
    editableTodo.value.tags.push(newTag.value.trim());
    newTag.value = '';
  }
}

const removeTag = (tagToRemove: string) => {
  if (editableTodo.value) {
    editableTodo.value.tags = editableTodo.value.tags.filter((tag: string) => tag !== tagToRemove);
  }
}
</script>

<style scoped>
/* 抽屉背景遮罩层动画 */
.drawer-fade-enter-active,
.drawer-fade-leave-active {
  transition: opacity 0.3s ease;
}

.drawer-fade-enter-from,
.drawer-fade-leave-to {
  opacity: 0;
}

/* 抽屉面板滑入动画 */
.drawer-slide-enter-active,
.drawer-slide-leave-active {
  transition: transform 0.3s cubic-bezier(0.22, 1, 0.36, 1);
}

.drawer-slide-enter-from,
.drawer-slide-leave-to {
  transform: translateX(100%);
}
</style>
