# 三角眼统计配置指南

## 概述

为了更好地了解用户行为和网站流量，我们建议配置网站统计工具。以下是推荐方案：

## 1. Google Analytics 4 (推荐)

### 优点
- 免费
- 数据准确
- 强大的用户行为分析
- 支持中国访问

### 配置步骤

1. 访问 [Google Analytics](https://analytics.google.com/)
2. 使用 Google 账号登录
3. 创建账号和媒体资源
4. 获取 Measurement ID (格式: G-XXXXXXXXXX)
5. 在 index.html 中取消注释并填入你的 ID

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

## 2. 友盟统计 (UMeng)

### 优点
- 专为中文网站优化
- 支持小游戏统计
- 详细的事件追踪

### 配置步骤

1. 访问 [友盟统计](https://www.umeng.com/)
2. 注册并登录
3. 创建应用获取 AppKey
4. 在 index.html 中添加 SDK

## 3. Umami (自托管 - 隐私友好)

### 优点
- 开源免费
- 隐私友好 (GDPR合规)
- 可自托管
- 轻量级

### 配置步骤

1. 在自己的服务器上部署 Umami
2. 创建网站获取 Website ID
3. 在 index.html 中添加脚本

```html
<script defer src="https://your-umami-server.com/umami.js"></script>
<script>umami.track();</script>
```

## 重要提示

- 统计代码已添加到 index.html 中，但是**被注释掉**的
- 请根据需要取消注释对应代码并填入你的 ID
- 确保在部署前完成配置

## 数据追踪建议

建议追踪以下事件：

1. **工具使用** - 用户使用哪个工具
2. **页面停留** - 用户在页面停留时间
3. **跳出率** - 用户是否快速离开
4. **转化目标** - 用户是否点击了推广链接

## 当前状态

- [ ] Google Analytics 已配置
- [ ] 友盟统计已配置
- [ ] Umami 已配置
