# 文物修复项目管理平台

面向文物建档、病害诊断、修复方案编制、修复工序管理、质量验收与展览借出的一体化文物修复项目管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 文物档案 | `relic` | 文物 | 文物编号、文物名称、文物类别 |
| 病害诊断 | `diagnosis` | 病害记录 | 记录编号、文物编号、病害类型 |
| 修复方案 | `restore_plan` | 修复方案 | 方案编号、文物编号、方案名称 |
| 修复项目 | `restore_project` | 修复项目 | 项目编号、文物编号、采用方案 |
| 修复材料 | `material` | 修复材料 | 材料编号、材料名称、材料规格 |
| 修复工序 | `restore_process` | 修复工序 | 工序编号、所属项目、工序名称 |
| 影像记录 | `photo_record` | 影像档案 | 影像编号、文物编号、拍摄类型 |
| 质量验收 | `quality_check` | 验收记录 | 验收编号、所属项目、验收节点 |
| 存放环境 | `storage_env` | 环境记录 | 记录编号、存放处所、温度值 |
| 展览借出 | `exhibition` | 借展申请 | 申请编号、文物编号、借展单位 |
| 文物运输 | `transport_relic` | 运输任务 | 任务编号、文物编号、出发地 |
| 环境监控 | `environment_monitor` | 监控设备 | 设备编号、监测点位、设备类型 |
| 修复人员 | `personnel_relic` | 修复师 | 员工编号、姓名、修复专长 |
| 修复设备 | `equipment_relic` | 修复设备 | 设备编号、设备名称、设备类型 |
| 经费预算 | `budget_relic` | 预算科目 | 科目编号、科目名称、预算类型 |
| 修复报告 | `report_relic` | 修复报告 | 报告编号、所属项目、报告类型 |
| 文物保险 | `insurance_relic` | 保单 | 保单编号、文物编号、保险类型 |
| 出入记录 | `access_log` | 出入记录 | 记录编号、文物编号、操作类型 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
