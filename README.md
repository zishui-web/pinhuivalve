# 浙江品汇阀门有限公司 · 企业官网

Vue 3 + Vite 单页应用。视觉参考 `素材/品汇阀门工业官网首页.png`，产品内容全部取自
《温州品汇阀门有限公司样本册单P(刀闸阀)》26 页样本册。

## 快速开始

```bash
npm install      # 安装依赖
npm run dev      # 开发模式 http://localhost:5173
npm run build    # 生产构建 -> dist/
npm run preview  # 预览构建产物
```

## 目录结构

```
pinhuivalve/
├─ public/
│  ├─ favicon.png
│  └─ images/                  # 由 scripts/build-assets.py 生成（webp / 透明底）
├─ scripts/
│  ├─ build-assets.py          # 素材处理：白底产品图抠图、工厂图转 webp、logo 去白底
│  └─ validate-data.mjs        # 数据自检：列数一致性 + 与法兰标准表交叉核对
├─ docs/
│  ├─ PLAN.md                  # 建站规划（信息架构 / 设计系统 / 素材映射）
│  └─ DEPLOY.md                # 部署：Nginx / docker compose / 云托管 / 子目录 / 日志 / 回滚
├─ deploy/
│  ├─ nginx-site.conf          # 宿主机 Nginx 站点配置（含 SPA 回退与缓存）
│  ├─ nginx.conf               # 容器内 Nginx 主配置（日志格式、/logs 查看、缓存）
│  ├─ logs-viewer.html         # /logs 日志查看页（纯静态，直读 access.log）
│  ├─ logs-auth.conf           # 日志页可选 Basic 认证（默认不鉴权）
│  ├─ Dockerfile               # 多阶段构建：Node 编译 + Nginx 托管
│  └─ Dockerfile.runtime       # 只打包 dist 的运行时镜像（跨架构导出用）
├─ docker-compose.yml          # 一键启动：构建 + 端口 + 日志挂载 + 健康检查
├─ logs/                       # 日志目录（容器挂载点；*.log 不入库）
├─ src/
│  ├─ data/
│  │  ├─ company.js            # 企业信息、联系方式、优势、支持入口
│  │  ├─ products.js           # 6 大系列 + 12 个产品（参数 / 材质 / 尺寸表 / 型号一览）
│  │  └─ support.js            # 阀座结构、法兰尺寸表、安装与维护、FAQ
│  ├─ router/index.js          # 路由 + 标题 + 锚点滚动
│  ├─ styles/base.css          # 设计令牌、通用表格、按钮、响应式断点
│  ├─ components/              # Header / Footer / ProductCard / DataTable / CtaBand ...
│  └─ views/                   # Home / Products / ProductDetail / About / Strength / Support / Contact / 404
```

## 页面

| 路由 | 说明 |
|---|---|
| `/` | 首页：首屏、产品中心、关于品汇、应用领域、优势、产品线 CTA、技术支持、联系 CTA |
| `/products` | 产品中心：6 系列筛选 + 12 个产品 + 型号一览 |
| `/products/:slug` | 产品详情：图集、参数、特点、材质、外形连接尺寸表、订货说明 |
| `/about` | 关于我们：企业简介、数据、经营理念、制造能力、应用行业、经营范围 |
| `/strength` | 生产实力：车间、五道工序、设备实景、检验标准 |
| `/support` | 技术支持：阀座结构、法兰尺寸（4 张表）、安装、预防措施、FAQ |
| `/contact` | 联系我们：销售电话、地址、微信二维码、在线询价表单、来厂路线 |

## 内容维护

- 改文案、参数、尺寸表：只动 `src/data/*.js`，无需改组件。
- 新增产品：在 `products.js` 的 `products` 数组追加对象，`slug` 即路由；
  `dimensions` 里每张表的 `columns.length` 必须与每行 `row.length` 相等。
- 改完后运行 `node scripts/validate-data.mjs`，会校验列数，并把尺寸表的
  D1 / D2 / n-m 与 `support.js` 法兰标准表逐行比对（已在白名单中的样本册内部差异会提示）。
- 换图片：把源图放回桌面素材文件夹，修改 `scripts/build-assets.py` 里的映射表后运行
  `python3 scripts/build-assets.py`（需要 Pillow、numpy）。

## 素材处理说明

- 产品图（`品汇63-82`、`品汇1-62`）为白底棚拍图。脚本用「亮度阈值 + 四角洪水填充」只去掉
  与画面边缘连通的背景，避免误删不锈钢高光；再对边缘做 0.6px 羽化并反白（un-premultiply），
  使深色背景上不出现白边。
- 全站图片输出 WebP，产品图为透明底，总体积约 2.0MB。

## 部署

`npm run build` 产物为纯静态文件，可直接托管。由于使用 history 路由，需要配置 SPA 回退：

```nginx
location / {
  try_files $uri $uri/ /index.html;
}
```

换机器部署的完整步骤（Nginx / Docker / 云静态托管 / 子目录部署 / 版本回滚 / 上线自检）
见 `docs/DEPLOY.md`；现成的配置在 `deploy/` 下：

```bash
# 方式一：docker compose（推荐，构建+启动+日志挂载一步到位）
docker compose up -d --build      # http://服务器IP（默认 80 端口）
docker compose logs -f web        # 实时日志

# 方式一·仅镜像（目标机不需要 Node/npm/源码，适合离线、内网、生产）
docker save pinhuivalve:latest | gzip > pinhuivalve-latest.tar.gz   # 构建机导出
gunzip -c pinhuivalve-latest.tar.gz | docker load                   # 目标机导入
cp deploy/docker-compose.image.yml ./docker-compose.image.yml
docker compose -f docker-compose.image.yml up -d

# 方式二：本机构建后上传 dist/
npm run build && rsync -avz --delete dist/ user@server:/var/www/pinhuivalve/

# 方式三：纯 docker 命令
docker build -f deploy/Dockerfile -t pinhuivalve:1.0 .
docker run -d -p 80:80 --restart unless-stopped -v "$PWD/logs:/var/log/nginx" pinhuivalve:1.0
```

## 日志

- 网页查看：`http://服务器IP/logs` —— 表格化展示时间、IP、请求、状态码、大小、耗时、UA，
  带 2xx/4xx/5xx 统计、关键字筛选、仅有错误、5 秒自动刷新（默认对所有 IP 开放）
- 文件查看：`tail -f logs/access.log`、`logs/error.log`
- 容器输出：`docker compose logs -f web`
- 日志切割与鉴权（怎么加密码、怎么只允许内网、怎么关掉）见 `docs/DEPLOY.md`「日志」章节

## 说明

- 表单为前端演示，不提交到服务器；提交后提示用户电话/微信确认。
- 尺寸表按样本册原表录入；样本册中产品尺寸表与附录法兰表在个别规格（如 PN1.6 DN250 密封面直径、
  DN600 螺纹规格）存在印刷差异，页面已注明「订货以产品表与确认图为准」。
