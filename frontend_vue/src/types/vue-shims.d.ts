// 只声明 .vue 文件的类型，不覆盖整个 'vue' 模块
declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}