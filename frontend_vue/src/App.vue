<template>
  <div class="navbar bg-base-100 shadow-sm">
    <div class="navbar-start">
      <h1 class="text-[clamp(1.8rem,4vw,0.5rem)] font-bold text-slate-800 dark:text-white tracking-tight p-2">
        <span class="bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-indigo-600">Todo</span>
        测试更新
      </h1>
    </div>
    <div class="navbar-center hidden lg:flex">
      <ul class="menu menu-horizontal px-1">
        <li>
          <router-link to="/" class="router-link-exact-active:bg-primary/10">
            <Home theme="outline" size="20" strokeLinejoin="round" strokeLinecap="round" />
            主页
          </router-link>
        </li>
        <li>
          <router-link to="/quadrant" class="router-link-exact-active:bg-primary/10">
            <!-- 更新路由链接 -->
            <WaterfallsH theme="outline" size="20" strokeLinejoin="round" strokeLinecap="round" />
            四象限
          </router-link>
        </li>
        <li>
          <router-link to="/calendar" class="router-link-exact-active:bg-primary/10">
            <Calendar theme="outline" size="20" strokeLinejoin="round" strokeLinecap="round" />
            日历
          </router-link>
        </li>
        <li>
          <router-link to="/statistics" class="router-link-exact-active:bg-primary/10">
            <Ranking theme="outline" size="20" strokeLinejoin="round" strokeLinecap="round" />
            统计
          </router-link>
        </li>
        <li>
          <router-link to="/about" class="router-link-exact-active:bg-primary/10">
            <info theme="outline" size="20" strokeLinejoin="round" strokeLinecap="round" />
            关于
          </router-link>
        </li>
      </ul>
    </div>

    <div class="navbar-end">
      <div class="flex-none">
        <div class="dropdown dropdown-end">
          <input type="text" placeholder="搜索任务" class="input input-bordered w-24 md:w-auto" />
          <button class="btn btn-ghost">
            <div class="indicator">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
              </svg>
              <span class="badge badge-xs badge-secondary indicator-item">99+</span>
            </div>
          </button>
        </div>

        <div class="dropdown dropdown-end">
          <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
            <div class="w-10 rounded-full">
              <img alt="Tailwind CSS Navbar component"
                src="https://roadshow-dev-1302949722.file.myqcloud.com/avatar/cat.jpg" />
            </div>
          </div>
          <ul tabindex="0" class="menu menu-sm dropdown-content bg-base-100 rounded-box z-1 mt-3 w-52 p-2 shadow">
            <li>
              <a class="justify-between"> 个人中心 </a>
            </li>
            <li><a>设置</a></li>
            <li><a>登出</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <!-- 添加路由视图容器 -->
  <router-view class="p-4" />
</template>

<script setup lang="ts">
import {
  Home,
  WaterfallsH,
  Info,
  Ranking,
  Calendar,
} from "@icon-park/vue-next";
</script>

<style scoped></style>