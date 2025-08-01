<template>
  <!-- 容器保持固定高度和自定义滚动条 -->
  <div class="h-[160px] overflow-y-auto pr-2 space-y-2.5 custom-scrollbar">
    <!-- 空状态 (样式微调) -->
    <div v-if="tasks.length === 0"
      class="flex flex-col items-center justify-center h-full text-slate-400 dark:text-slate-500">
      <Inbox class="mb-2 opacity-60" theme="outline" size="40" :stroke-width=3 />
      <p class="text-sm">此象限暂无任务</p>
    </div>

    <!-- 任务列表 -->
    <TransitionGroup v-else tag="div" name="task-item-anim" class="space-y-2.5" appear>
      <!-- 全新设计的任务项 -->
      <div v-for="task in tasks" :key="task.id" @click="todoStore.toggleTodoCompletion(task.id)"
        class="task-item flex justify-between items-center gap-4 p-3 rounded-lg transition-all duration-200 cursor-pointer border"
        :class="[
          task.completed
            ? 'bg-slate-100 dark:bg-slate-800/30 border-transparent'
            : 'bg-white/70 dark:bg-slate-800/50 border-transparent hover:bg-white hover:border-slate-200 dark:hover:bg-slate-700/80 dark:hover:border-slate-600',
        ]">
        <!-- 左侧区域：复选框 + 任务文本 -->
        <div class="flex items-center gap-3 overflow-hidden">
          <!-- 自定义圆形复选框 -->
          <div
            class="flex-shrink-0 w-5 h-5 flex items-center justify-center rounded-full border-2 transition-all duration-200"
            :style="{
              backgroundColor: task.completed ? themeColor : 'transparent',
              borderColor: task.completed
                ? themeColor
                : '#cbd5e1' /* slate-300 */,
            }">
            <Transition name="fade">
              <Check v-if="task.completed" class="text-white" theme="outline" size="14" :stroke-width="5" />
            </Transition>
          </div>

          <!-- 任务文本 (应用文本截断) -->
          <p class="truncate transition-colors duration-200 font-medium" :class="task.completed
            ? 'line-through text-slate-400 dark:text-slate-500'
            : 'text-slate-700 dark:text-slate-200'
            " :title="task.text">
            {{ task.text }}
          </p>
        </div>

        <!-- 右侧区域：分类标签 -->
        <div class="flex-shrink-0">
          <span v-if="task.categoryId" :style="{
            backgroundColor: todoStore.getCategoryColor(task.categoryId),
            color: getContrastingTextColor(
              todoStore.getCategoryColor(task.categoryId)
            ),
          }" class="px-2.5 py-1 rounded-md text-xs font-bold">
            {{ todoStore.getCategoryName(task.categoryId) }}
          </span>
        </div>
      </div>
    </TransitionGroup>
  </div>
</template>

<script setup lang="ts">
import { useTodoStore } from "@/stores/todo";
import { computed } from "vue";
import { Inbox, Check } from "@icon-park/vue-next";

// Props 保持不变
const props = defineProps<{
  category: string;
  themeColor: string;
}>();

const todoStore = useTodoStore();

// 任务过滤逻辑保持不变
const tasks = computed(() => {
  return todoStore.todos.filter((task) => {
    const isImportant = task.tagIds.includes("important");
    const isUrgent = task.tagIds.includes("urgent");
    switch (props.category) {
      case "important-urgent":
        return isImportant && isUrgent;
      case "important-not-urgent":
        return isImportant && !isUrgent;
      case "urgent-not-important":
        return !isImportant && isUrgent;
      case "not-urgent-not-important":
        return !isImportant && !isUrgent;
      default:
        return false;
    }
  });
});

/**
 * [新增] 辅助函数：根据背景色计算最佳对比度的文本颜色（黑或白）。
 * @param hexColor - 背景色的Hex值 (例如 '#RRGGBB')
 * @returns '#ffffff' (白色) 或 '#1e293b' (深灰)
 */
const getContrastingTextColor = (hexColor: string): string => {
  if (!hexColor) return "#1e293b"; // slate-800
  const r = parseInt(hexColor.slice(1, 3), 16);
  const g = parseInt(hexColor.slice(3, 5), 16);
  const b = parseInt(hexColor.slice(5, 7), 16);
  // W3C亮度计算公式
  const luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255;
  return luminance > 0.5 ? "#1e293b" : "#ffffff";
};
</script>

<style scoped>
/* 样式保持不变，但仍是必需的 */
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: rgba(100, 116, 139, 0.3);
  border-radius: 10px;
  border: 2px solid transparent;
  background-clip: content-box;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background-color: rgba(100, 116, 139, 0.5);
}

/* 列表项的动画效果 */
.task-item-anim-enter-active,
.task-item-anim-leave-active {
  transition: all 0.4s ease;
}

.task-item-anim-enter-from,
.task-item-anim-leave-to {
  opacity: 0;
  transform: translateX(-20px);
}

.task-item-anim-move {
  transition: transform 0.4s ease;
}

/* 复选框 'check' 图标的淡入淡出动画 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* 
 * 手动为 `truncate` 类添加一个 title 属性提示。
 * 虽然 Tailwind 的 `truncate` 已经应用了必要的 CSS，
 * 但这里我们通过 :title="task.text" 绑定了完整文本，
 * 这样用户鼠标悬停时可以看到被截断的全部内容。
 * `p.truncate` 的样式由 Tailwind 直接提供。
 */
</style>
