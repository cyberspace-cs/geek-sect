# 极客宗 · 多端 APP 打包指南

## 📱 支持平台
- 🤖 Android (APK)
- 🍎 iOS (需要 Mac + Xcode)
- 🐧 Linux / macOS / Windows (Electron 桌面端)
- 📱 鸿蒙 (HarmonyOS, 需要 DevEco Studio)

---

## 🚀 快速开始（Capacitor 远程加载模式）

这种模式最简单：APP 只是一个 WebView 壳，直接加载 https://hack.taoxie.vip

### 1. 环境准备
```bash
# 安装 Node.js 18+
npm install

# 初始化 Capacitor
npx cap init
```

### 2. 打包 Android APK
```bash
# 添加 Android 平台
npx cap add android

# 同步配置
npx cap sync

# 打开 Android Studio
npx cap open android

# 在 Android Studio 里 Build -> Build APK
```

### 3. 打包 iOS（需要 Mac）
```bash
npx cap add ios
npx cap sync
npx cap open ios
# 在 Xcode 里 Archive -> Export
```

---

## 🖥️ 桌面端打包（Electron）

### 方案一：Electron Builder
```bash
npm install --save-dev electron electron-builder

# 配置 electron 入口
# 打包成 Windows/Mac/Linux 安装包
npx electron-builder
```

### 方案二：Tauri（更轻量）
- 包体积更小（~10MB vs Electron ~100MB）
- 性能更好
- 需要 Rust 环境

---

## 🔧 配置说明

### App ID
```
com.taoxie.geeksect
```

### App 名称
```
极客宗
```

### 背景色
```
#0a0a12 （极夜黑，和 Web 端一致）
```

---

## 📦 发布渠道

| 平台 | 渠道 |
|------|------|
| Android | 酷安、应用宝、华为应用市场、小米应用商店 |
| iOS | App Store（需要 99 美元/年开发者账号） |
| 桌面 | GitHub Releases、官网下载 |
| 鸿蒙 | 华为应用市场 |

---

## 💡 进阶优化

1. **离线缓存**：用 Capacitor 的本地资源模式，把静态文件打包进 APP
2. **推送通知**：接入 Firebase / 极光推送
3. **登录**：微信/QQ/手机号登录
4. **支付**：苹果内购 / 微信支付 / 支付宝
5. **社区**：内置论坛 / 排行榜
