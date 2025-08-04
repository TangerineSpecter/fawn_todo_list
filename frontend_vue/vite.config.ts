import {defineConfig} from 'vite';
import vue from '@vitejs/plugin-vue';
import tailwindcss from '@tailwindcss/vite';
import path from 'path';


// https://vitejs.dev/config/
export default defineConfig({
    base: '/static/',  // 关键：静态资源路径前缀，比如放到python根目录的statis文件夹下
    build: {
        outDir: 'dist',  // 打包输出目录
    },
    plugins: [tailwindcss(), vue()],
    define: {
        //'process.env': { ...process.env }

    },
    resolve: {
        alias: {
            '@': path.resolve(__dirname, 'src'),
            crypto: 'crypto-browserify',
            'vue': 'vue/dist/vue.esm-bundler.js'
        }
    }
})
