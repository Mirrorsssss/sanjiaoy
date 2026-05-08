# 三角眼网站 - 部署指南

## 第一步：在GitHub新建仓库

1. 打开 https://github.com
2. 点击右上角 `+` → `New repository`
3. 填写：
   - **Repository name**: `sanjiaoy`
   - **Description**: `三角眼 - 三角洲行动战备工具站`
   - **Public** 选中（必须Public才能用免费托管）
   - ✅ Add a README file
4. 点击 `Create repository`

---

## 第二步：上传网站代码

在终端执行：

```bash
cd C:\Users\11342\WorkBuddy\2026-05-08-task-1

# 初始化git
git init

# 添加远程仓库（把 YOUR_USERNAME 换成你的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/sanjiaoy.git

# 添加所有文件
git add index.html

# 提交
git commit -m "三角眼 v1.0 - MVP上线"

# 推送
git branch -M main
git push -u origin main
```

> ⚠️ 第一次推送会弹出GitHub登录窗口，按提示登录授权即可。

---

## 第三步：开启GitHub Pages（免费托管）

1. 在GitHub仓库页面 → 点击 `Settings`（设置）
2. 左侧菜单 → 找到 `Pages`
3. 配置：
   - **Source**: Deploy from a branch
   - **Branch**: `main` / `(root)` → 点击 `Save`
4. 等待1-2分钟，刷新页面
5. 看到绿色的 `Your site is live at https://YOUR_USERNAME.github.io/sanjiaoy/` 就成功了！

---

## 第四步：绑定域名（可选）

域名审核通过后：
1. 仓库 Settings → Pages → Custom domain → 输入你的域名（如 `sanjiaoy.site`）
2. 去腾讯云控制台 → 域名解析 → 添加记录：
   - 类型：`CNAME`
   - 主机记录：`@`
   - 记录值：`YOUR_USERNAME.github.io`
3. 等待DNS生效（5分钟~24小时），即可用你的域名访问

---

## 验证网站是否正常

打开 https://YOUR_USERNAME.github.io/sanjiaoy/ 查看网站是否正常显示。
