# 多阶段构建：Node 编译 -> Nginx 托管静态文件（含访问日志落盘 + /logs 查看页）
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci || npm install
COPY . .
RUN npm run build

FROM nginx:alpine

# 时区：让日志时间戳显示为北京时间（$time_iso8601 用容器本地时区）
RUN apk add --no-cache tzdata \
 && mkdir -p /usr/share/nginx/logs-viewer /var/log/nginx \
 && chown -R nginx:nginx /var/log/nginx

COPY deploy/nginx.conf /etc/nginx/nginx.conf
RUN rm -f /etc/nginx/conf.d/*.conf

COPY deploy/logs-viewer.html /usr/share/nginx/logs-viewer/index.html
COPY deploy/logs-auth.conf /etc/nginx/logs-auth.conf
COPY --from=build /app/dist /usr/share/nginx/html

ENV TZ=Asia/Shanghai
EXPOSE 80
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s CMD wget -qO- http://127.0.0.1/ >/dev/null || exit 1
CMD ["nginx", "-g", "daemon off;"]
