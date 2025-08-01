<template>
  <!-- 1. 整体背景使用非常浅的灰色，提供一个干净的画布 -->
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <!-- 
      卡片入场动画: 
      - 使用 isMounted ref 来控制动画触发
      - 'opacity-0 scale-95' 是初始状态
      - 'opacity-100 scale-100' 是结束状态
      - 'transform transition-all duration-700 ease-out' 定义了动画曲线和时长
    -->
    <div
      class="max-w-3xl w-full bg-white rounded-2xl shadow-lg overflow-hidden transform transition-all duration-700 ease-out"
      :class="isMounted ? 'opacity-100 scale-100' : 'opacity-0 scale-95'"
    >
      <!-- 卡片悬停动效 -->
      <div
        class="transition-all duration-300 hover:shadow-xl hover:-translate-y-1"
      >
        <!-- ========================== -->
        <!--        头部区域 (Header)      -->
        <!-- ========================== -->
        <div
          class="relative p-8 text-center bg-gradient-to-br from-cyan-400 to-teal-500 text-white overflow-hidden"
        >
          <!-- 装饰性背景光晕效果 -->
          <div
            class="absolute top-0 left-1/2 -translate-x-1/2 w-48 h-48 bg-white/10 rounded-full blur-2xl"
          ></div>

          <div class="relative z-10">
            <!-- 图标容器: 使用高亮色透明度渐变制造科技感 -->
            <div
              class="w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center bg-white/20 backdrop-blur-sm ring-1 ring-white/30"
            >
              <!-- 2. 使用 @icon-park/vue-next 图标库 -->
              <Stopwatch theme="outline" size="32" fill="#ffffff" />
            </div>
            <h1 class="text-3xl font-bold tracking-tight">Todo番茄清单</h1>
            <p class="mt-2 text-white/80">高效任务管理与时间规划工具</p>
          </div>
        </div>

        <!-- ========================== -->
        <!--        内容区域 (Content)     -->
        <!-- ========================== -->
        <div class="p-8 space-y-8">
          <!-- 关于应用介绍 -->
          <div>
            <h2
              class="text-xl font-bold text-slate-800 flex items-center gap-2"
            >
              <Info theme="outline" size="22" class="text-teal-500" />
              关于本应用
            </h2>
            <p class="mt-3 text-slate-600 leading-relaxed">
              Todo番茄清单是一款结合了任务管理与番茄工作法的 productivity
              工具，旨在帮助用户更高效地规划时间、管理任务，提升工作与学习效率。
            </p>
            <p class="mt-3 text-slate-600 leading-relaxed">
              通过直观的界面设计和实用的功能，您可以轻松创建任务、设置优先级、分类管理，并使用番茄钟专注工作。应用支持四象限任务分类法，帮助您区分任务的轻重缓急，优先处理重要事项。
            </p>
          </div>

          <!-- 核心功能列表 -->
          <div>
            <h3
              class="text-xl font-bold text-slate-800 flex items-center gap-2"
            >
              <ApplicationOne theme="outline" size="22" class="text-teal-500" />
              核心功能
            </h3>
            <!-- 3. 使用 Grid 布局，并为每个功能项添加交错入场动画 -->
            <div class="mt-4 grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- 功能项 -->
              <div
                v-for="(feature, index) in features"
                :key="feature.text"
                class="flex items-start gap-4 p-4 rounded-lg bg-gray-50/80 transition-all duration-500 ease-out"
                :class="
                  isMounted
                    ? 'opacity-100 translate-y-0'
                    : 'opacity-0 translate-y-4'
                "
                :style="{ transitionDelay: `${100 * index}ms` }"
              >
                <div
                  class="flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center bg-gradient-to-br from-cyan-400/20 to-teal-500/20"
                >
                  <component
                    :is="feature.icon"
                    theme="outline"
                    size="18"
                    class="text-teal-600"
                  />
                </div>
                <span class="text-slate-700 pt-1">{{ feature.text }}</span>
              </div>
            </div>
          </div>

          <!-- ========================== -->
          <!--       页脚区域 (Footer)      -->
          <!-- ========================== -->
          <div class="text-center pt-6 border-t border-gray-200">
            <p class="text-sm text-slate-500">作者：丢失的猫咪</p>
            <div
              class="inline-flex items-center gap-1.5 mt-2 bg-red-50 text-red-700 text-xs font-semibold px-3 py-1 rounded-full"
            >
              <Tag theme="outline" size="14" />
              <span>版本号：0.0.1</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, shallowRef } from "vue";
// 导入所有需要的图标
import {
  Stopwatch,
  Info,
  ApplicationOne,
  List,
  WaterfallsH,
  TagOne,
  AlarmClock,
  ChartProportion,
} from "@icon-park/vue-next";

// 控制入场动画的响应式引用
const isMounted = ref(false);

// 在组件挂载后触发动画
onMounted(() => {
  // 使用 setTimeout 确保在下一帧触发，让 CSS 过渡生效
  setTimeout(() => {
    isMounted.value = true;
  }, 100);
});

// 核心功能列表数据，将内容与图标绑定
const features = ref([
  {
    text: "直观的任务管理界面，支持添加、编辑、删除任务",
    icon: shallowRef(List),
  },
  { text: "四象限分类法，清晰区分任务优先级", icon: shallowRef(WaterfallsH) },
  { text: "自定义分类与标签，灵活组织任务", icon: shallowRef(TagOne) },
  { text: "番茄钟计时功能，提升专注度", icon: shallowRef(AlarmClock) },
  {
    text: "数据统计与分析，了解您的任务完成情况",
    icon: shallowRef(ChartProportion),
  },
]);
</script>

<!-- 
  [说明]
  - 无需 <style scoped> 块，所有样式均由 Tailwind CSS 实现，保持代码整洁。
  - 使用 shallowRef 存储组件定义可以略微优化性能，因为 Vue 不需要对组件本身进行深度响应式处理。
-->
