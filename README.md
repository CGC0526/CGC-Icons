# CGC Icons

面向 **Loon / Surge 等 iOS 网络工具**维护的图标资源仓库。

本仓库基于 [Homarr Dashboard Icons](https://github.com/homarr-labs/dashboard-icons) 的 PNG 图标索引，自动转换为适用于 Loon 的 iconset JSON，并通过 GitHub Actions 定时检查上游更新。

---

## 图标集

### 精选版

适合日常策略组使用，收录常见的：

- Apple
- Google
- Microsoft
- AI
- 视频会议
- 社交
- 流媒体
- 游戏
- 支付
- VPN / 网络工具
- 地图与生产力应用

#### Raw

```text
https://raw.githubusercontent.com/CGC0526/CGC-Icons/main/IconSet/Dashboard-Icons-Loon-Selected.json
```

#### jsDelivr

```text
https://cdn.jsdelivr.net/gh/CGC0526/CGC-Icons@main/IconSet/Dashboard-Icons-Loon-Selected.json
```

#### Loon 一键导入

```text
https://www.nsloon.com/openloon/import?iconset=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FCGC0526%2FCGC-Icons%40main%2FIconSet%2FDashboard-Icons-Loon-Selected.json
```

---

### 完整版

包含 Homarr Dashboard Icons 当前提供的全部 PNG 图标。

#### Raw

```text
https://raw.githubusercontent.com/CGC0526/CGC-Icons/main/IconSet/Dashboard-Icons-Loon-Full.json
```

#### jsDelivr

```text
https://cdn.jsdelivr.net/gh/CGC0526/CGC-Icons@main/IconSet/Dashboard-Icons-Loon-Full.json
```

#### Loon 一键导入

```text
https://www.nsloon.com/openloon/import?iconset=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FCGC0526%2FCGC-Icons%40main%2FIconSet%2FDashboard-Icons-Loon-Full.json
```

---

## 自动更新

本仓库使用 GitHub Actions 自动维护图标集。

工作流：

```text
.github/workflows/update-icons.yml
```

生成脚本：

```text
scripts/generate_icons.py
```

精选图标清单：

```text
scripts/selected-icons.txt
```

工作流会：

1. 获取 Dashboard Icons 最新 `tree.json`
2. 读取最新 PNG 图标列表
3. 重新生成 Loon 完整版 iconset
4. 根据 `selected-icons.txt` 重新生成精选版
5. 校验生成后的 JSON
6. 比较仓库中的现有文件
7. 仅在内容发生变化时自动 Commit 并 Push

当前计划任务：

```text
每天 04:17 Asia/Shanghai
```

也可以在 GitHub：

```text
Actions
→ Update Dashboard Icons for Loon
→ Run workflow
```

手动执行更新。

---

## 仓库结构

```text
CGC-Icons/
├── .github/
│   └── workflows/
│       └── update-icons.yml
├── IconSet/
│   ├── Dashboard-Icons-Loon-Full.json
│   └── Dashboard-Icons-Loon-Selected.json
├── scripts/
│   ├── generate_icons.py
│   └── selected-icons.txt
└── README.md
```

---

## 上游项目

图标来源：

```text
https://github.com/homarr-labs/dashboard-icons
```

PNG CDN：

```text
https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/png/
```

本仓库仅负责将上游图标索引整理并转换为适用于 Loon 的 iconset JSON 格式。

---

## 说明

- 推荐日常使用 **精选版**。
- 完整版适合需要搜索大量第三方服务图标的场景。
- 图标文件本身通过 jsDelivr / 上游项目提供，本仓库主要维护索引。
- 如果上游删除或重命名图标，下一次自动更新时会同步反映到生成结果。
- Loon 中已添加的远程图标集无需因普通上游更新而更换 URL。

---

## Repository

```text
https://github.com/CGC0526/CGC-Icons
```
