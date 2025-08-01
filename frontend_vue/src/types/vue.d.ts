// src/types/vue.d.ts
/// <reference types="vue/client" />

import type { DefineComponent } from 'vue';

// 声明 Vue 模块
declare module 'vue' {
  export * from 'vue/dist/vue'; // 指向实际的类型文件
}

// 声明 .vue 文件类型
declare module '*.vue' {
  const component: DefineComponent<{}, {}, any>;
  export default component;
}