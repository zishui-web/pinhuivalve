# 部署说明（其他机器）

本站是纯静态前端（Vue 3 + Vite），**没有后端依赖**：构建出的 `dist/` 目录用任何静态服务器都能跑。
唯一需要注意的是路由使用 history 模式，服务器必须把未命中的路径回退到 `index.html`。

---

## 0. 准备

| 场景 | 需要什么 |
|---|---|
| 只想发布站点 | 一台能跑 Nginx/Apache 的服务器，只需 `dist/` 目录 |
| 想在服务器上自己构建 | Node.js ≥ 18（推荐 20 LTS）+ npm |
| 想用容器 | Docker 20+ |

拿到项目时有 `node_modules` 也可以，但换机器建议删掉重装：`rm -rf node_modules package-lock.json && npm install`。

---

## 方案一：本地构建，上传 dist（最简单，推荐）

**在开发机执行：**

```bash
cd pinhuivalve
npm ci                 # 或 npm install
npm run build          # 产物在 dist/
```

**上传到服务器：**

```bash
# 首次
ssh user@your-server "sudo mkdir -p /var/www/pinhuivalve"
rsync -avz --delete dist/ user@your-server:/var/www/pinhuivalve/

# 也可以打包传输
tar czf pinhuivalve-dist.tar.gz -C dist .
scp pinhuivalve-dist.tar.gz user@your-server:/tmp/
ssh user@your-server "sudo tar xzf /tmp/pinhuivalve-dist.tar.gz -C /var/www/pinhuivalve"
```

**Nginx 配置**（文件已附：`deploy/nginx-site.conf`）：

```nginx
server {
    listen 80;
    server_name www.example.com;          # 改成你的域名
    root /var/www/pinhuivalve;
    index index.html;

    gzip on;
    gzip_types text/css application/javascript application/json image/svg+xml;
    gzip_min_length 1024;

    # 带 hash 的静态资源，长期缓存
    location /assets/ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
    location /images/ {
        expires 30d;
        add_header Cache-Control "public";
    }
    # 入口文件不缓存，保证发版立即生效
    location = /index.html {
        add_header Cache-Control "no-cache";
    }

    # history 路由回退
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

```bash
sudo cp deploy/nginx-site.conf /etc/nginx/conf.d/pinhuivalve.conf
sudo nginx -t && sudo systemctl reload nginx
```

**HTTPS**：用 certbot 一条命令即可

```bash
sudo certbot --nginx -d example.com -d www.example.com
```

---

## 方案二：在服务器上构建

```bash
# 服务器安装 Node 20（Ubuntu/Debian 示例）
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# 上传项目（不要带 node_modules）
rsync -avz --exclude node_modules --exclude dist ./ user@your-server:/opt/pinhuivalve/

ssh user@your-server
cd /opt/pinhuivalve
npm ci
npm run build            # 产出 /opt/pinhuivalve/dist
```

Nginx 的 `root` 指到 `/opt/pinhuivalve/dist`，其余同方案一。

---

## 方案三：docker compose 一键启动（推荐）

项目根目录已有 `docker-compose.yml`，一条命令完成构建 + 启动 + 日志挂载：

```bash
cd pinhuivalve
docker compose up -d --build       # 首次构建并后台启动
docker compose ps                  # 看状态（healthy 表示就绪）
docker compose logs -f web         # 实时看容器日志（等于 access.log 的 stdout 副本）
```

默认访问 `http://服务器IP`（80 端口）。改端口：`WEB_PORT=8080 docker compose up -d`（或写进 `.env`）。

常用运维命令：

```bash
docker compose restart web         # 重启
docker compose up -d --build       # 改了代码/配置后重建
docker compose down                # 停止并删除容器（日志文件保留在 ./logs）
docker compose pull && docker compose up -d   # 若改用远程镜像更新
```

`docker-compose.yml` 关键点：

| 配置 | 作用 |
|---|---|
| `ports: "${WEB_PORT:-80}:80"` | 宿主机端口可覆盖，默认 80 |
| `./logs:/var/log/nginx` | 访问日志/错误日志落盘到项目 `logs/` 目录 |
| `./deploy/logs-auth.conf:/etc/nginx/logs-auth.conf:ro` | 日志页可选密码，改完不用重建镜像，`docker compose restart` 即可 |
| `TZ=Asia/Shanghai` | 日志时间戳为北京时间 |
| `logging: max-size 10m / max-file 3` | 容器 stdout 日志自动切割，最多占 30MB |
| `healthcheck` | 30 秒探活，`docker compose ps` 显示 healthy |

> 跨架构导出镜像（如 M 系列 Mac → x86 服务器）时不要忘记指定平台：
> `DOCKER_DEFAULT_PLATFORM=linux/amd64 docker compose build`，详见下文「导出镜像到其他机器」。

### 等价的 docker 命令（不用 compose）

```bash
cd pinhuivalve

# 构建镜像（多阶段：Node 负责编译，Nginx 负责托管）
docker build -f deploy/Dockerfile -t pinhuivalve:1.0 .

# 运行（注意挂载日志目录，否则日志只在容器里）
mkdir -p logs
docker run -d --name pinhuivalve -p 80:80 --restart unless-stopped \
  -v "$PWD/logs:/var/log/nginx" \
  -v "$PWD/deploy/logs-auth.conf:/etc/nginx/logs-auth.conf:ro" \
  -e TZ=Asia/Shanghai \
  pinhuivalve:1.0
# 访问 http://服务器IP
```

导出镜像拷到**无外网**的机器：

```bash
docker save pinhuivalve:1.0 | gzip > pinhuivalve-1.0.tar.gz
scp pinhuivalve-1.0.tar.gz user@target:/tmp/
ssh user@target "gunzip -c /tmp/pinhuivalve-1.0.tar.gz | docker load && docker run -d -p 80:80 --restart unless-stopped pinhuivalve:1.0"
```

`docker-compose.yml`（可选）：

```yaml
services:
  web:
    image: pinhuivalve:1.0
    ports: ['80:80']
    restart: unless-stopped
```

---

---

## 另一台机器上直接 `docker compose up -d` 能不能起来？

**看目标机上有什么**：

| 目标机上的内容 | 结果 |
|---|---|
| 只有 `docker-compose.yml` | ✗ 起不来。compose 里是 `build:`，缺 `deploy/Dockerfile`、`deploy/nginx.conf`、`src/`、`package.json`，会直接报找不到构建上下文 |
| 完整仓库（可剔除 `node_modules/`、`dist/`） | ✓ 能起来。`docker compose up -d` 会现场构建：拉 `node:20-alpine`、`nginx:1.31.2-alpine`，容器内 `npm ci` + `npm run build` |
| 只有镜像 tar 包 + `deploy/docker-compose.image.yml` | ✓ 最快最稳，不需要 Node/npm/源码/外网（推荐离线、内网、生产） |

### 前置条件（缺一样都会失败）

```bash
docker info                     # Docker 守护进程在运行
docker compose version          # 必须是 v2（docker compose，不是 docker-compose v1）
ss -lntp | grep -E ':(80|8080)' # 端口没被占用，占用就 WEB_PORT=8090
```

- **目录里要有 `docker-compose.yml`**（compose 自动识别这个文件名）
- **`deploy/logs-auth.conf` 必须存在**。它是 `COPY` 源，也被挂载；文件缺失时 Docker 会把挂载点建成**同名目录**，Nginx `include` 一个目录会启动失败
- 构建模式还需要：能访问 Docker Hub（拉基础镜像）与 npm registry（装依赖）。国内网络建议
  `npm config set registry https://registry.npmmirror.com`，或干脆用下面的镜像模式
- 架构要匹配：在目标机上构建 = 架构天然匹配；用别人导出的镜像则要看架构

### 方式 A：有源码，直接起（最省事）

```bash
# 目标机
cd pinhuivalve
docker compose up -d --build
docker compose ps                      # Up (healthy)
curl -sI http://127.0.0.1 | head -1
```

默认端口 80；要换端口 `WEB_PORT=8080 docker compose up -d`。
首次构建 2–5 分钟（取决于网络），之后改代码只需 `docker compose up -d --build`，有缓存会快很多。

### 方式 B：只有镜像，不起 Node（推荐）

```bash
# 构建机
docker compose build
docker save pinhuivalve:latest | gzip > pinhuivalve-latest.tar.gz    # 约 30MB
# 跨架构（M 系 Mac → x86 服务器）：
# DOCKER_DEFAULT_PLATFORM=linux/amd64 docker compose build

# 目标机（只需要 docker，不需要 node/npm/源码）
gunzip -c pinhuivalve-latest.tar.gz | docker load
cp deploy/docker-compose.image.yml ./docker-compose.image.yml
docker compose -f docker-compose.image.yml up -d
```

`deploy/docker-compose.image.yml` 里没有 `build:`，只有 `image: pinhuivalve:latest`，
挂载 `./logs` 与端口参数化，其余与主 compose 一致。日志页 `/logs` 一样可用。

### 自检（起来了不等于能用）

```bash
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1/                       # 200
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1/products/pz73-pz43     # 200（回退生效）
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1/logs                   # 200
ls -lh logs/access.log                                                                 # 有内容
```

### 常见启动失败对照

| 报错 | 原因 | 处理 |
|---|---|---|
| `no such file or directory: Dockerfile` / `failed to read dockerfile` | 只拷了 compose，没拷 `deploy/` 与源码 | 拷完整仓库，或改走镜像模式 |
| `Bind for 0.0.0.0:80 failed: port is already allocated` | 宿主机 80 被占 | `WEB_PORT=8080 docker compose up -d` |
| `[emerg] open() "/etc/nginx/logs-auth.conf" failed` | 该路径被建成目录（源文件缺失） | `rm -rf deploy/logs-auth.conf` 后重新检出/新建空文件 |
| `nginx: [emerg] unknown directive` / 容器反复 Restarting | 改了 nginx.conf 有语法错 | `docker compose logs web` 看行号，或 `docker run --rm -v $PWD/deploy/nginx.conf:/etc/nginx/nginx.conf nginx:1.31.2-alpine nginx -t` |
| `pwrite() "/var/run/nginx.pid" failed (1: Operation not permitted)` | 宿主对 `/var/run` 写入受限：只读根文件系统、安全加固、SELinux/gVisor 等 | 已修复：pid 与临时目录改到 `/tmp`，compose 加 `tmpfs: /tmp`。拉到旧镜像请 `docker compose build` 重建 |
| `exec format error` | 镜像架构与机器不符 | 见下节「导出镜像到其他机器」 |
| 构建卡在 `npm ci` | 网络访问 npm 慢/被墙 | 配 npmmirror 镜像，或改用镜像模式 |


### 加固环境下为什么要用 `/tmp`

有些服务器开了只读根文件系统、SELinux 强模式、gVisor 沙箱，或 `/var/run` 被以只读方式挂载，
Nginx 默认把 pid 写到 `/var/run/nginx.pid`，于是启动时报：

```
[crit] 1#1: pwrite() "/var/run/nginx.pid" failed (1: Operation not permitted)
```

本项目的做法（已内置，无需你改）：

- `pid /tmp/nginx.pid;`
- `client_body_temp_path` / `proxy_temp_path` 等全部指向 `/tmp/...`
- compose 里 `tmpfs: - /tmp`，只读根文件系统下 `/tmp` 仍是可写的内存盘

实测两种加固场景均能正常启动并访问：`--read-only`（只读根 + tmpfs /tmp）、
`/var/run` 以只读 tmpfs 覆盖。

如果你自己写 `docker run`，记得补上 `--tmpfs /tmp`，否则只读根文件系统下会报
`mkdir() "/tmp/client_temp" failed (30: Read-only file system)`。

### 构建报 `[UNLOADABLE_DEPENDENCY] Could not load src/data/...` 怎么办

先确认是不是本机的内容拦截（安全/加密代理）导致的——stat 尺寸比实际读取长度大（通常正好多 4096 字节）：

```bash
python3 -c "import os;f='src/data/products.js';print('stat',os.stat(f).st_size,'读取',len(open(f,'rb').read()))"
```

如果是，执行仓库自带脚本修复后重新构建：

```bash
bash scripts/unseal.sh        # 用 git 重新写出文件（会丢弃这些文件未提交的修改）
docker compose build
```

该现象只影响「被加密代理处理过的文件」，本地 `npm run build` 往往仍能通过，
但 Docker 构建上下文与镜像内的打包器会读到残缺内容。

### 目标机起不来，按这个顺序查

```bash
# 1) 容器到底什么状态（ExitCode 有意义）
docker compose ps -a
docker inspect pinhuivalve --format '{{.State.Status}} exit={{.State.ExitCode}} err={{.State.Error}}'

# 2) 启动日志（Nginx 的 [emerg]/[crit] 都在这里）
docker compose logs --tail=50 web

# 3) Nginx 配置语法单独验一遍（不启动服务）
docker run --rm -v "$PWD/deploy/nginx.conf":/etc/nginx/nginx.conf:ro nginx:1.31.2-alpine nginx -t

# 4) 文件级错误看宿主机日志目录
tail -n 50 logs/error.log

# 5) 端口/挂载
ss -lntp | grep -E ':(80|8080|8090)'
docker inspect pinhuivalve --format '{{json .Mounts}}' | python3 -m json.tool
```

---

## 导出镜像到其他机器（跨架构必读）

`docker save` 只打包镜像层，**不会改变 CPU 架构**。在 Apple Silicon（M 系列）Mac 上构建出来的是
`linux/arm64` 镜像，拿到 x86_64 的云服务器上直接跑会报：

```
exec /docker-entrypoint.sh: exec format error
# 或
WARNING: The requested image's platform (linux/arm64) does not match the detected host platform (linux/amd64)
```

**绝大多数云服务器是 x86_64**，所以导出的镜像要在 x86 上跑，构建时必须指定平台。

### 推荐做法：先出 dist，再打 amd64 运行时镜像（最快）

不要在模拟环境里跑 `npm ci`（QEMU 模拟下会慢 5–10 倍）。先在任意机器构建静态文件，再打包：

```bash
# 1) 任意机器（arm64 / x86 都可以）构建静态文件
npm run build

# 2) 打 x86_64 运行时镜像（只拷贝 dist，秒级完成）
docker build --platform linux/amd64 -f deploy/Dockerfile.runtime -t pinhuivalve:1.0 .

# 3) 确认架构
docker image inspect pinhuivalve:1.0 --format '{{.Architecture}} / {{.Os}}'
# 期望输出：amd64 / linux

# 4) 导出（含基础镜像层，目标机无需联网拉 nginx）
docker save pinhuivalve:1.0 | gzip > pinhuivalve-1.0-amd64.tar.gz
ls -lh pinhuivalve-1.0-amd64.tar.gz        # 实测 27MB（含 nginx:1.31.2-alpine 全部层）

# 5) 拷到目标机并加载
scp pinhuivalve-1.0-amd64.tar.gz user@target:/tmp/
ssh user@target "gunzip -c /tmp/pinhuivalve-1.0-amd64.tar.gz | docker load"

# 6) 启动并自检
ssh user@target "docker run -d --name pinhuivalve -p 80:80 --restart unless-stopped pinhuivalve:1.0"
ssh user@target "curl -sI http://127.0.0.1/products/pz73-pz43 | head -1"   # HTTP/1.1 200 OK
```

### 想用完整多阶段 Dockerfile 也行

```bash
docker build --platform linux/amd64 -f deploy/Dockerfile -t pinhuivalve:1.0 .
```

依赖会在模拟环境里安装，构建时间明显变长（本机实测 arm64 原生约 20 秒，模拟 amd64 需数分钟）。
如果只是发布静态站，用上面的 `Dockerfile.runtime` 更省事。

### 目标机架构怎么确认

```bash
uname -m                 # x86_64 -> 用 amd64 镜像；aarch64 / arm64 -> 用 arm64 镜像
docker version --format '{{.Server.Arch}}'
```

### 已经导错了怎么办

三种补救，按推荐顺序：

1. 在目标机上重新 `docker build --platform linux/amd64 ...`（架构天然匹配，最稳）
2. 在源机构建时加 `--platform linux/amd64` 重新导出
3. 临时让 x86 服务器模拟 arm64（不推荐上生产，性能损耗大、需要 qemu）：
   `docker run --platform linux/arm64 ...`

### 其它容易忽略的点

- `docker save` 不含容器的运行状态和挂载卷；本站无状态，直接 `run` 即可。
- 导出文件是 tar，`docker save a:1 b:2` 可一次打包多个 tag。
- 目标机 Docker 版本不要低于构建机太多（建议 20.10+），否则 `--platform` 元数据可能丢失。
- 镜像内 Nginx 监听 80，映射到宿主机别的端口时用 `-p 8080:80`，不要改容器内端口。
- 目标机已装 Nginx 占用了 80，先 `ss -lntp | grep :80` 确认，或改用 `-p 8080:80` + 上层反代。

## 方案四：云静态托管（无需自己维护服务器）

| 平台 | 关键设置 |
|---|---|
| Vercel / Netlify | 构建命令 `npm run build`，输出目录 `dist`；Netlify 另需 `_redirects`：`/* /index.html 200` |
| Cloudflare Pages | 构建命令 `npm run build`，输出 `dist`；自动支持 SPA 回退 |
| 阿里云 OSS / 腾讯云 COS + CDN | 开启「静态网站」并把 **404 页面指向 index.html**；CDN 缓存忽略参数或按目录设置 |

这些平台都只吃 `dist/`，上传产物即可。

---

---

## 日志（目录 / 命令行 / 网页查看）

### 三种看法，任选

| 方式 | 命令 | 说明 |
|---|---|---|
| 网页 | 浏览器打开 `http://服务器IP/logs` | 结构化表格：时间、IP、请求、状态码、大小、耗时、UA，带统计与筛选 |
| 原始文件 | `tail -f logs/access.log` | 宿主机目录，就是完整日志原文 |
| 容器标准输出 | `docker compose logs -f web` | 与文件同一份（Nginx 同时写文件与 stdout） |

`logs/` 目录（已随项目提交，`.gitignore` 里忽略 `*.log`）：

```
logs/
├─ access.log     # 访问日志（每 1 秒 flush，网页 5 秒拉取一次）
├─ error.log      # Nginx 错误日志
└─ .gitkeep
```

日志格式（`deploy/nginx.conf` 里的 `log_format pinhui`）：

```
$remote_addr - [$time_iso8601] "$request" $status $body_bytes_sent ${request_time}s "$http_referer" "$http_user_agent"
# 示例：
1.2.3.4 - [2026-11-17T14:22:31+08:00] "GET /products/pz73-pz43 HTTP/1.1" 200 1530 0.003s "https://example.com/" "Mozilla/5.0 ..."
```

### 网页日志页做了什么

- 直读 `/logs/access.log`，不经过任何后端，纯静态 JS（`deploy/logs-viewer.html`）
- 顶部统计：总请求 / 2xx / 3xx / 4xx / 5xx / 平均耗时
- 可按路径、IP、状态码过滤；「仅有错误」只看 4xx/5xx；5 秒自动刷新（页面隐藏时暂停）
- 「原始 access.log」「error.log」按钮可直接看原文，便于排查
- **默认对全部 IP 开放**（按需求设置）。公网可访问意味着日志（含访客 IP、UA）对外可见

### 想收紧/关闭访问

1. 加密码（推荐，改完 `docker compose restart` 生效，无需重建镜像）：

```bash
sudo apt install -y apache2-utils        # 或 brew install httpd
htpasswd -nb admin 你的密码              # 输出形如 admin:$apr1$xxxx
# 把输出整行粘到 deploy/logs-auth.conf，并放开这两行：
#   auth_basic "PinHui Logs";
#   auth_basic_user_file /etc/nginx/.htpasswd;
docker compose restart web
```

注意：`auth_basic_user_file` 默认指向容器内 `/etc/nginx/.htpasswd`，需要把 htpasswd 文件也挂进去：
在 `docker-compose.yml` 的 volumes 里加 `- ./deploy/.htpasswd:/etc/nginx/.htpasswd:ro`。

2. 只允许内网：在 `deploy/nginx.conf` 的 `location /logs/` 内加回
   `allow 10.0.0.0/8; allow 172.16.0.0/12; allow 192.168.0.0/16; deny all;` 后重建。

3. 完全关闭：把 `location = /logs` 和 `location /logs/` 两段删掉，或改成 `return 404;`。

### 日志切割

- 容器 stdout：已由 compose 的 `logging` 限制（10MB × 3）。
- 文件日志不会自己切，建议宿主机加 logrotate：

```bash
sudo tee /etc/logrotate.d/pinhuivalve >/dev/null <<'EOF'
/var/www/pinhuivalve/logs/*.log {
    daily
    rotate 14
    compress
    delaycompress
    missingok
    notifempty
    copytruncate
}
EOF
```

（路径换成你实际的 `logs` 目录；`copytruncate` 避免 Nginx 需要重开文件。）

### 常见问题

**打开 /logs 是空白表格** → 还没有访问记录，刷新几次首页即可；或容器没挂载 `./logs`（`docker inspect pinhuivalve | grep -A3 Mounts` 确认）。

**日志时间差 8 小时** → 镜像已装 tzdata 并设 `TZ=Asia/Shanghai`；若自己改过 `docker run`，补上 `-e TZ=Asia/Shanghai`。

**access.log 一直是空的** → 检查 `docker compose logs web` 是否有 Nginx 启动报错；`/var/log/nginx` 被别的卷覆盖也会导致写不进去。

**宿主机 logs/*.log 属主是 root（Linux）** → Nginx 以 root 写文件，属主为 root 属正常；只想自己看就 `sudo chown -R $USER logs`，或把 compose 里加 `user: "0:0"` 保持默认。

## 部署到子目录（如 https://example.com/pinhuivalve/）

需要同时改两个地方，否则资源 404：

1. `vite.config.js`

```js
export default defineConfig({
  base: '/pinhuivalve/',
  plugins: [vue()]
})
```

2. `src/router/index.js`

```js
const router = createRouter({
  history: createWebHistory('/pinhuivalve/'),
  routes,
  scrollBehavior(to, from, savedPosition) { /* 保持原样 */ }
})
```

3. Nginx 用 alias

```nginx
location /pinhuivalve/ {
    alias /var/www/pinhuivalve/;
    try_files $uri $uri/ /pinhuivalve/index.html;
}
```

然后重新 `npm run build`。

---

## 发版与回滚

```bash
# 版本化目录 + 软链接，切流量即回滚
sudo mkdir -p /var/www/pinhuivalve/releases/20261117
rsync -avz --delete dist/ user@server:/var/www/pinhuivalve/releases/20261117/
ssh user@server "ln -sfn /var/www/pinhuivalve/releases/20261117 /var/www/pinhuivalve/current && sudo nginx -s reload"
```

Nginx 的 `root` 用 `/var/www/pinhuivalve/current`。
回滚只需把软链接指回上一个 release 目录。

---

## 上线后自检

```bash
curl -I  https://example.com/                       # 200
curl -I  https://example.com/products               # 200（不能 404，否则回退没配好）
curl -I  https://example.com/products/pz73-pz43     # 200
curl -s  https://example.com/ | grep -o '<title>[^<]*'  # 标题应为 浙江品汇阀门有限公司…
```

浏览器里再确认三件事：

1. 直接粘贴 `https://域名/products/ggg40-slurry` 能打开（不是白屏 / 404）
2. 刷新任意内页不报错（history 回退生效）
3. 手机宽度下导航抽屉、产品筛选、尺寸表横向滑动正常

---

## 常见问题

**内页刷新 404** → Nginx 少了 `try_files $uri $uri/ /index.html;`。

**页面能开但样式全丢** → 部署在子目录却没设 `base`，见上文「部署到子目录」。

**改了文案线上没变化** → `index.html` 被缓存，按上文给它加 `no-cache`；带 hash 的 `assets/` 可以放心长缓存。

**构建报 `COPY failed: stat dist: file does not exist`** → `.dockerignore` 里不能排除 `dist`
（`Dockerfile.runtime` 直接拷贝它）；本项目已在 `.dockerignore` 中保留 dist 并注明原因。

**图片 404** → `dist/images/` 没上传全；`public/images` 里的文件由 `scripts/build-assets.py` 生成，构建时会整体复制到 `dist/`。

**留言表单收不到** → 本站为纯静态站点，表单不提交服务器，只做前端校验与电话引导；如需真实收集，需接入表单服务或自建接口。
