<template>
  <!-- 
    页面根元素:
    - 使用微妙的噪点纹理背景增加质感 (noise-bg)
    - 整体布局和内外边距设置
  -->
  <div class="w-full h-[90vh] noise-bg py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto">
      <!-- 页面标题 -->
      <header class="mb-12 text-center">
        <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-slate-800 dark:text-slate-100 tracking-tight">
          <span class="relative inline-block">
            四象限
            <!-- 标题下划线辉光效果 -->
            <span
              class="absolute bottom-[-8px] left-0 w-full h-1 bg-indigo-500/50 dark:bg-indigo-400/50 rounded-full blur-sm"></span>
            <span
              class="absolute bottom-[-8px] left-1/2 -translate-x-1/2 w-1/2 h-1 bg-indigo-500 dark:bg-indigo-400 rounded-full"></span>
          </span>
          任务矩阵
        </h1>
        <p class="mt-6 max-w-2xl mx-auto text-lg text-slate-600 dark:text-slate-400">
          运用艾森豪威尔矩阵，清晰划分任务优先级，专注核心要务。
        </p>
      </header>

      <!-- 
        四象限网格:
        - 使用 <TransitionGroup> 实现列表交错动画
        - 使用 v-for 动态渲染四个象限卡片，优化代码结构
      -->
      <TransitionGroup tag="div" class="grid grid-cols-1 md:grid-cols-2 gap-6 lg:gap-8" @before-enter="onBeforeEnter"
        @enter="onEnter" appear>
        <div v-for="(quadrant, index) in quadrants" :key="quadrant.category" :data-index="index"
          class="quadrant-card relative overflow-hidden bg-white/60 dark:bg-slate-800/60 backdrop-blur-xl border border-slate-200/80 dark:border-slate-700/80 rounded-2xl shadow-lg transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
          <!-- 辉光效果: 使用绝对定位的伪元素或div，通过放射状渐变实现 -->
          <div class="absolute -top-1/4 -left-1/4 w-1/2 h-1/2 blur-3xl opacity-60 dark:opacity-40 rounded-full"
            :class="quadrant.glowClass"></div>

          <div class="relative p-6 h-full flex flex-col">
            <!-- 卡片头部: 图标 + 标题 -->
            <div class="flex items-center gap-4 mb-4">
              <div class="w-12 h-12 rounded-xl flex items-center justify-center" :class="quadrant.iconBgClass">
                <component :is="quadrant.icon" :class="quadrant.colorClass" theme="outline" size="28"
                  :stroke-width="3" />
              </div>
              <div>
                <h2 class="text-xl font-bold" :class="quadrant.colorClass">
                  {{ quadrant.title }}
                </h2>
                <p class="text-sm text-slate-500 dark:text-slate-400">
                  {{ quadrant.description }}
                </p>
              </div>
            </div>

            <!-- 任务列表区域 -->
            <div class="flex-grow">
              <QuadrantTasks :category="quadrant.category" :theme-color="quadrant.colorClass"
                :border-color-class="quadrant.borderColorClass" />
            </div>
          </div>
        </div>
      </TransitionGroup>
    </div>
  </div>
</template>

<script setup lang="ts">
import QuadrantTasks from "@/components/QuadrantTasks.vue";

// 引入 @icon-park/vue-next 的图标
import { Fire, Target, PhoneTelephone, CupFour } from "@icon-park/vue-next";
import type { Icon } from "@icon-park/vue-next/lib/runtime";

// 定义象限卡片的数据结构类型
interface Quadrant {
  title: string;
  description: string;
  category:
  | "important-urgent"
  | "important-not-urgent"
  | "urgent-not-important"
  | "not-urgent-not-important";
  icon: Icon;
  colorClass: string;
  iconBgClass: string;
  glowClass: string;
  borderColorClass: string;
}

// 象限数据数组: 将重复的结构抽象为数据，便于维护和渲染
const quadrants: Quadrant[] = [
  {
    title: "重要且紧急",
    description: "立即处理，优先完成",
    category: "important-urgent",
    icon: Fire,
    colorClass: "text-rose-500 dark:text-rose-400",
    iconBgClass: "bg-rose-100 dark:bg-rose-500/10",
    glowClass: "bg-rose-500/40",
    borderColorClass: "border-rose-500 dark:border-rose-400",
  },
  {
    title: "重要不紧急",
    description: "制定计划，持续推进",
    category: "important-not-urgent",
    icon: Target,
    colorClass: "text-sky-500 dark:text-sky-400",
    iconBgClass: "bg-sky-100 dark:bg-sky-500/10",
    glowClass: "bg-sky-500/40",
    borderColorClass: "border-sky-500 dark:border-sky-400",
  },
  {
    title: "紧急不重要",
    description: "快速处理，或授权他人",
    category: "urgent-not-important",
    icon: PhoneTelephone,
    colorClass: "text-amber-500 dark:text-amber-400",
    iconBgClass: "bg-amber-100 dark:bg-amber-500/10",
    glowClass: "bg-amber-500/40",
    borderColorClass: "border-amber-500 dark:border-amber-400",
  },
  {
    title: "不紧急不重要",
    description: "减少或在空闲时处理",
    category: "not-urgent-not-important",
    icon: CupFour,
    colorClass: "text-teal-500 dark:text-teal-400",
    iconBgClass: "bg-teal-100 dark:bg-teal-500/10",
    glowClass: "bg-teal-500/40",
    borderColorClass: "border-teal-500 dark:border-teal-400",
  },
];

// --- Vue TransitionGroup 动画钩子 ---
// 关于 Framer Motion:
// 注意：您的依赖项中未包含 'framer-motion'。
// 以下使用 Vue 内置的 TransitionGroup 功能，结合 CSS 动效，
// 实现了轻量级且高性能的列表交错动画，这是在 Vue 项目中的推荐做法。

const onBeforeEnter = (el: Element) => {
  (el as HTMLElement).style.opacity = "0";
  (el as HTMLElement).style.transform = "translateY(30px)";
};

const onEnter = (el: Element, done: () => void) => {
  const index = parseInt((el as HTMLElement).dataset.index || "0");
  const delay = index * 100; // 每个元素延迟100ms
  done(); // 调用done回调以完成过渡

  setTimeout(() => {
    (el as HTMLElement).style.opacity = "1";
    (el as HTMLElement).style.transform = "translateY(0)";
    (el as HTMLElement).style.transition =
      "opacity 0.5s ease, transform 0.5s ease";
    // 动画结束后调用 done()，但对于纯CSS动画通常不是必须的
  }, delay);
};
</script>

<style>
/* 
  添加一个细微的噪点背景纹理。
  这是一个轻量级的方式来增加页面的视觉质感。
*/
.noise-bg {
  background-image: linear-gradient(rgba(255, 255, 255, 0.92),
      rgba(255, 255, 255, 0.92)),
    url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.2' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  background-blend-mode: overlay;
}

/* 暗色模式下的噪点背景 */
.dark .noise-bg {
  background-image: linear-gradient(rgba(15, 23, 42, 0.95),
      rgba(15, 23, 42, 0.95)),
    url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
}

/*
  确保在 TransitionGroup 的 enter/leave 过程中，
  元素保持其在grid布局中的位置，防止布局坍塌。
*/
.quadrant-card {
  transition: opacity 0.5s ease, transform 0.5s ease;
}
</style>
