<template>
  <div class="flex h-[90vh] overflow-hidden bg-slate-50 dark:bg-slate-900">
    <!-- 左侧面板 -->
    <aside
      class="w-72 bg-white dark:bg-slate-800/30 shadow-sm border-r border-slate-200 dark:border-slate-800 flex flex-col">
      <div class="p-4 flex items-center gap-3">
        <svg class="h-8 w-8 text-sky-500" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M9 22H15C20 22 22 20 22 15V9C22 4 20 2 15 2H9C4 2 2 4 2 9V15C2 20 4 22 9 22Z" stroke="currentColor"
            stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
          <path d="M7.75 12L10.58 14.83L16.25 9.17" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"
            stroke-linejoin="round"></path>
        </svg>
        <h1 class="text-xl font-bold text-slate-800 dark:text-slate-100">我的任务</h1>
      </div>

      <div class="flex-1 overflow-y-auto min-h-0 pr-2">
        <ul class="menu w-full space-y-1 px-2">
          <li v-for="item in mainMenuItems" :key="item.id">
            <a @click="activeItem = item.id"
              :class="{ 'bg-sky-500/10 dark:bg-sky-500/20 text-sky-600 dark:text-sky-400 font-semibold': activeItem === item.id, 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700/50': activeItem !== item.id }"
              class="flex items-center justify-between transition-all duration-200"
              :aria-current="activeItem === item.id ? 'page' : undefined">
              <div class="flex items-center gap-3">
                <component :is="item.icon" :fill="item.iconColor" theme="outline" size="20" :strokeWidth="3" />
                <span class="font-medium">{{ item.label }}</span>
              </div>
              <div class="flex items-center gap-4 text-sm">
                <span class="opacity-60 group-hover:opacity-100 transition-opacity">{{ item.time }}</span>
                <span v-if="item.count >= 0" class="font-mono text-xs w-8 text-right px-2 py-0.5">{{ item.count
                }}</span>
              </div>
            </a>
          </li>
        </ul>
        <div
          class="divider my-2 before:bg-slate-200 dark:before:bg-slate-700 after:bg-slate-200 dark:after:bg-slate-700">
          <span class="text-xs text-slate-400">分类</span>
        </div>
        <ul class="menu w-full space-y-1 px-2">
          <li>
            <a @click="openCategoryModal()"
              class="flex items-center gap-3 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700/50 transition-all duration-200">
              <ListAdd theme="outline" size="20" stroke="#64748b" :strokeWidth="3" />
              <span class="font-medium">添加分类</span>
            </a>
          </li>
          <li v-for="item in projectItems" :key="item.id">
            <a @click="activeItem = item.id"
              :class="{ 'bg-sky-500/10 dark:bg-sky-500/20 text-sky-600 dark:text-sky-400 font-semibold': activeItem === item.id, 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700/50': activeItem !== item.id }"
              class="flex items-center justify-between transition-all duration-200"
              :aria-current="activeItem === item.id ? 'page' : undefined">
              <div class="flex items-center gap-3">
                <div v-if="item.type === 'dot'" class="h-3 w-3 rounded-full"
                  :style="{ backgroundColor: item.iconColor }"></div>
                <component v-else :is="item.icon" :fill="item.iconColor" theme="outline" size="20" :stroke-width="3" />
                <span class="font-medium">{{ item.label }}</span>
              </div>
              <div class="flex items-center gap-4 text-sm">
                <span class="opacity-60 group-hover:opacity-100 transition-opacity">{{ item.time }}</span>
                <span v-if="item.count >= 0" class="font-mono text-xs w-8 text-right px-2 py-0.5">{{ item.count
                }}</span>
              </div>
            </a>
          </li>
        </ul>
        <div
          class="divider my-2 before:bg-slate-200 dark:before:bg-slate-700 after:bg-slate-200 dark:after:bg-slate-700">
          <span class="text-xs text-slate-400">标签</span>
        </div>
        <ul class="menu w-full space-y-1 px-2">
          <li>
            <a @click="openTagModal()" class="flex items-center gap-3 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700/50 transition-all duration-200">
              <TagOne theme="outline" size="20" stroke="#64748b" :strokeWidth="3" />
              <span class="font-medium">添加标签</span>
            </a>
          </li>
          <li v-for="tag in tags" :key="tag.id">
            <a class="flex items-center justify-between transition-all duration-200">
              <div class="flex items-center gap-3">
                <TagOne theme="filled" :fill="tag.color" />
                <span class="font-medium">{{ tag.name }}</span>
              </div>
              <span class="font-mono text-xs w-8 text-right px-2 py-0.5">{{ todoStore.tagTaskCount(tag.id) }}</span>
            </a>
          </li>
        </ul>
      </div>
    </aside>

    <!-- 右侧主区域 -->
    <main class="flex-1 flex flex-col p-6 overflow-hidden">
      <div class="max-w-4xl mx-auto w-full flex-1 flex flex-col min-h-0">
        <div class="mb-8 flex flex-col md:flex-row md:items-center md:justify-between">
          <div class="text-left">
            <h1 class="text-[clamp(2rem,4vw,2.5rem)] font-extrabold text-slate-800 dark:text-white tracking-tight"><span
                class="bg-clip-text text-transparent bg-gradient-to-br from-sky-500 to-indigo-600">{{ pageTitle
                }}</span></h1>
            <p class="text-slate-500 dark:text-slate-400 mt-2">保持有条理，提高你的工作效率</p>
          </div>
          <div class="grid grid-cols-2 gap-3 mt-4 md:mt-0 flex-shrink-0">
            <div
              class="relative overflow-hidden rounded-lg bg-white dark:bg-slate-800 p-3 shadow-sm border border-transparent hover:border-orange-500/30 transition-all duration-300 group w-40">
              <div
                class="absolute top-0 right-0 -translate-y-1/2 translate-x-1/2 w-32 h-32 bg-gradient-to-br from-orange-400/20 dark:from-orange-500/25 to-transparent rounded-full pointer-events-none">
              </div>
              <div class="relative z-10 flex items-center justify-between">
                <div>
                  <p class="text-xs font-medium text-slate-500 dark:text-slate-400">待完成</p>
                  <p class="text-2xl font-bold text-slate-800 dark:text-white">{{ Math.round(displayPendingCount) }}</p>
                </div>
                <div class="flex h-8 w-8 items-center justify-center rounded-full bg-orange-100 dark:bg-orange-500/20">
                  <AlarmClock theme="outline" size="20" fill="#f97316" :strokeWidth="3" />
                </div>
              </div>
            </div>
            <div
              class="relative overflow-hidden rounded-lg bg-white dark:bg-slate-800 p-3 shadow-sm border border-transparent hover:border-green-500/30 transition-all duration-300 group w-40">
              <div
                class="absolute top-0 right-0 -translate-y-1/2 translate-x-1/2 w-32 h-32 bg-gradient-to-br from-green-400/20 dark:from-green-500/25 to-transparent rounded-full pointer-events-none">
              </div>
              <div class="relative z-10 flex items-center justify-between">
                <div>
                  <p class="text-xs font-medium text-slate-500 dark:text-slate-400">已完成</p>
                  <p class="text-2xl font-bold text-slate-800 dark:text-white">{{ Math.round(displayCompletedCount) }}
                  </p>
                </div>
                <div class="flex h-8 w-8 items-center justify-center rounded-full bg-green-100 dark:bg-green-500/20">
                  <CheckCorrect theme="outline" size="20" fill="#22c55e" :strokeWidth="3" />
                </div>
              </div>
            </div>
          </div>
        </div>

        <div
          class="bg-white dark:bg-slate-800 rounded-xl shadow-md p-4 mb-8 transform transition-all duration-300 hover:shadow-lg">
          <div class="flex flex-col sm:flex-row gap-3">
            <input v-model="newTodoText" @keyup.enter="addTodo" placeholder="添加一个任务，按回车键保存"
              class="input input-bordered flex-1 transition-all focus:ring-2 focus:ring-sky-500 focus:border-sky-500 dark:bg-slate-700 dark:border-slate-600 dark:text-white" />
            <div class="flex gap-3 sm:w-auto w-full">
              <!-- #FIX: 动态绑定分类下拉列表 -->
              <select v-model="selectedCategoryId"
                class="select select-bordered flex-1 transition-all focus:ring-2 focus:ring-sky-500 focus:border-sky-500 dark:bg-slate-700 dark:border-slate-600 dark:text-white">
                <option v-for="cat in todoStore.categories" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
              </select>
              <button @click="addTodo" class="btn btn-primary">添加</button>
            </div>
          </div>
        </div>

        <!-- #FIX: 动态生成筛选按钮 -->
        <div class="mb-6 flex flex-wrap gap-2">
          <button @click="filterCategoryId = 'all'" :class="getFilterButtonClass('all')"
            :style="getFilterButtonStyle('all')">全部</button>
          <button v-for="cat in todoStore.categories" :key="cat.id" @click="filterCategoryId = cat.id"
            :class="getFilterButtonClass(cat.id)" :style="getFilterButtonStyle(cat.id)">
            {{ cat.name }}
          </button>
        </div>

        <div class="flex-1 space-y-3 overflow-y-auto pr-2">
          <div v-if="filteredTodos.length === 0"
            class="text-center py-16 bg-white dark:bg-slate-800/50 rounded-xl shadow-sm border border-dashed border-slate-300 dark:border-slate-700">
            <div
              class="inline-flex items-center justify-center w-20 h-20 rounded-full bg-slate-100 dark:bg-slate-700/50 mb-4">
              <CheckCorrect theme="outline" size="40" fill="#9ca3af" :strokeWidth="2" />
            </div>
            <h3 class="text-lg font-semibold text-slate-700 dark:text-slate-300">暂无任务</h3>
            <p class="text-slate-500 dark:text-slate-400 mt-1">添加一个新的任务，开始高效管理吧！</p>
          </div>

          <transition-group name="todo-item" tag="div" class="space-y-3">
            <div v-for="todo in filteredTodos" :key="todo.id"
              class="bg-white dark:bg-slate-800 rounded-xl shadow-sm hover:shadow-lg transition-all duration-300 transform hover:-translate-y-0.5 overflow-hidden group border border-transparent hover:border-sky-500/30">
              <div class="p-4 flex items-center justify-between cursor-pointer" @click="openTodoDrawer(todo)">
                <div class="flex items-center gap-4 flex-1 min-w-0">
                  <div class="flex-shrink-0">
                    <input type="checkbox" :checked="todo.completed" @click.stop="toggleTodoCompletion(todo.id)"
                      class="checkbox checkbox-primary w-5 h-5 rounded-md" />
                  </div>
                  <div class="flex flex-1 items-center justify-between min-w-0">
                    <span
                      :class="{ 'font-medium text-slate-800 dark:text-slate-100': !todo.completed, 'font-normal text-slate-400 dark:text-slate-500 line-through decoration-2': todo.completed }"
                      class="truncate text-base">{{ todo.text }}</span>
                    <div class="flex-shrink-0 flex items-center gap-4 ml-4">
                      <span v-if="todo.dueDate"
                        class="hidden sm:flex items-center gap-1.5 text-xs text-slate-500 dark:text-slate-400">
                        <Calendar theme="outline" size="14" class="inline-block" />
                        {{ formatDate(todo.dueDate) }}
                      </span>

                      <!-- #FIX: 修正分类标签的渲染方式 -->
                      <span v-if="todo.categoryId" class="inline-block px-2.5 py-1 text-xs rounded-full font-semibold"
                        :style="{ backgroundColor: todoStore.getCategoryColor(todo.categoryId), color: getContrastingTextColor(todoStore.getCategoryColor(todo.categoryId)) }">
                        {{ todoStore.getCategoryName(todo.categoryId) }}
                      </span>
                    </div>
                  </div>
                </div>
                <div class="ml-4 flex-shrink-0 opacity-0 group-hover:opacity-100 transition-opacity">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-slate-400" fill="none" viewBox="0 0 24 24"
                    stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
                  </svg>
                </div>
              </div>
            </div>
          </transition-group>
        </div>
      </div>
    </main>
  </div>
  <CategoryTagModal :visible="categoryModalVisible" @close="categoryModalVisible = false" />
  <TagModal :visible="tagModalVisible" @close="tagModalVisible = false" />
</template>

<script setup lang="ts">
import { ref, computed, shallowRef, watch, onMounted } from "vue";
import { storeToRefs } from 'pinia';
import CategoryTagModal from '../components/CategoryTagModal.vue';
import TagModal from '../components/TagModal.vue';
import { useTodoStore, type Todo } from "../stores/todo";
import { Sun, History, Sunrise, Calendar, CalendarThirtyTwo, Flag, CheckCorrect, AllApplication, Inbox, AlarmClock, TagOne, ListAdd } from "@icon-park/vue-next";

const todoStore = useTodoStore();
const { categoryModalVisible, tagModalVisible, tags } = storeToRefs(todoStore);

const openCategoryModal = () => {
  categoryModalVisible.value = true;
};

const openTagModal = () => {
  todoStore.toggleTagModalVisibility(true);
};

const newTodoText = ref("");
// #FIX: 改为 categoryId 并设置默认值
const selectedCategoryId = ref<string>(todoStore.categories[0]?.id || '');
const isDrawerOpen = ref(false);
const currentTodo = ref<Todo | null>(null);
// #FIX: 改为 categoryId
const filterCategoryId = ref<string>("all");

// #FIX: 筛选逻辑基于 categoryId
const filteredTodos = computed(() => {
  if (filterCategoryId.value === "all") {
    return todoStore.todos;
  }
  return todoStore.todos.filter(
    (todo: Todo) => todo.categoryId === filterCategoryId.value
  );
});

// --- 以下是统计和动画逻辑 (无需改动) ---
const pendingCount = computed(() => todoStore.todos.filter((todo: Todo) => !todo.completed).length);
const completedCount = computed(() => todoStore.todos.filter((todo: Todo) => todo.completed).length);
const displayPendingCount = ref(0);
const displayCompletedCount = ref(0);

function animateValue(startValue: number, endValue: number, duration: number, onUpdate: (value: number) => void) {
  let startTimestamp: number | null = null;
  const step = (timestamp: number) => {
    if (!startTimestamp) startTimestamp = timestamp;
    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
    const currentValue = progress * (endValue - startValue) + startValue;
    onUpdate(currentValue);
    if (progress < 1) { window.requestAnimationFrame(step); }
  };
  window.requestAnimationFrame(step);
}
watch(pendingCount, (newValue: number, oldValue: number) => { animateValue(oldValue, newValue, 500, (v) => (displayPendingCount.value = v)); });
watch(completedCount, (newValue: number, oldValue: number) => { animateValue(oldValue, newValue, 500, (v) => (displayCompletedCount.value = v)); });
onMounted(() => {
  animateValue(0, pendingCount.value, 500, (v) => (displayPendingCount.value = v));
  animateValue(0, completedCount.value, 500, (v) => (displayCompletedCount.value = v));
});
// --- 统计和动画逻辑结束 ---

// #FIX: addTodo 方法使用新的数据结构
const addTodo = () => {
  if (newTodoText.value.trim() && selectedCategoryId.value) {
    todoStore.addTodo({
      text: newTodoText.value,
      categoryId: selectedCategoryId.value,
    });
    newTodoText.value = "";
  }
};

const openTodoDrawer = (todo: Todo) => {
  currentTodo.value = { ...todo };
  isDrawerOpen.value = true;
};

const toggleTodoCompletion = (id: string) => {
  todoStore.toggleTodoCompletion(id);
};

// #ADD: 新增辅助函数，根据背景色计算最佳对比度文本色（黑或白）
const getContrastingTextColor = (hexColor: string): string => {
  if (!hexColor) return '#1e293b'; // slate-800 as fallback
  const r = parseInt(hexColor.slice(1, 3), 16);
  const g = parseInt(hexColor.slice(3, 5), 16);
  const b = parseInt(hexColor.slice(5, 7), 16);
  const luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255;
  return luminance > 0.5 ? '#1e293b' : '#ffffff'; // black or white
};

// #FIX: 筛选按钮的样式逻辑
const getFilterButtonClass = (categoryId: string) => {
  const baseClass = "px-4 py-2 rounded-full text-sm font-medium transition-all duration-200";
  if (filterCategoryId.value === categoryId) {
    return `${baseClass} shadow-md`;
  }
  return `${baseClass} bg-white dark:bg-slate-700/50 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700`;
};

const getFilterButtonStyle = (categoryId: string) => {
  if (filterCategoryId.value === categoryId) {
    const color = categoryId === 'all' ? '#64748b' : todoStore.getCategoryColor(categoryId); // slate-500 for 'all'
    return {
      backgroundColor: color,
      color: getContrastingTextColor(color),
    };
  }
  return {};
};

const formatDate = (dateString?: string): string => {
  if (!dateString) return "";
  const date = new Date(dateString);
  return date.toLocaleDateString("zh-CN", { month: "short", day: "numeric" });
};

// --- 以下是左侧菜单逻辑 (无需改动) ---
const activeItem = ref("today");
interface MenuItem { id: string; label: string; icon: any; iconColor: string; time: string; count: number; type?: "icon" | "dot"; }
const mainMenuItems = shallowRef<MenuItem[]>([{ id: "today", label: "今天", icon: Sun, iconColor: "#22c55e", time: "0m", count: 1, }, { id: "overdue", label: "过期", icon: History, iconColor: "#ef4444", time: "0m", count: 15, }, { id: "tomorrow", label: "明天", icon: Sunrise, iconColor: "#f97316", time: "0m", count: 0, }, { id: "this-week", label: "本周", icon: Calendar, iconColor: "#a855f7", time: "0m", count: 0, }, { id: "next-7-days", label: "最近7天", icon: CalendarThirtyTwo, iconColor: "#14b8a6", time: "0m", count: 0, }, { id: "priority", label: "高优先级", icon: Flag, iconColor: "#ef4444", time: "0m", count: 2, }, { id: "planned", label: "已计划", icon: CheckCorrect, iconColor: "#3b82f6", time: "0m", count: 15, }, { id: "all", label: "全部", icon: AllApplication, iconColor: "#f59e0b", time: "0m", count: 13, }, { id: "inbox", label: "收集箱", icon: Inbox, iconColor: "#6b7280", time: "0m", count: 12, },]);
// 从todoStore获取分类数据
const projectItems = computed<MenuItem[]>(() => {
  return todoStore.categories.map(category => ({
    id: category.id,
    label: category.name,
    icon: Inbox,
    iconColor: category.color,
    type: "dot" as const,
    time: "0m",
    count: todoStore.categoryTaskCount(category.id)
  }));
});
// 从store中获取tags数据，无需硬编码
const pageTitle = computed(() => { const allMenuItems = [...mainMenuItems.value, ...projectItems.value]; const activeMenu = allMenuItems.find((item) => item.id === activeItem.value); return activeMenu ? `${activeMenu.label}任务` : "我的任务"; });
// --- 左侧菜单逻辑结束 ---

</script>

<style scoped>
.todo-item-enter-from,
.todo-item-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

.todo-item-enter-active,
.todo-item-leave-active {
  transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}

.todo-item-move {
  transition: transform 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}

::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background-color: rgba(156, 163, 175, 0.4);
  border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
  background-color: rgba(156, 163, 175, 0.7);
}

.menu li>a {
  padding-top: 0.6rem;
  padding-bottom: 0.6rem;
  border-radius: 0.5rem;
}
</style>
