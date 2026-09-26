<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">文物修复项目管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向文物建档、病害诊断、修复方案编制、修复工序管理、质量验收与展览借出的一体化文物修复项目管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "文物档案", path: "/relic" }, { label: "病害诊断", path: "/diagnosis" }, { label: "修复方案", path: "/restore_plan" }, { label: "修复项目", path: "/restore_project" }, { label: "修复材料", path: "/material" }, { label: "修复工序", path: "/restore_process" }, { label: "影像记录", path: "/photo_record" }, { label: "质量验收", path: "/quality_check" }, { label: "存放环境", path: "/storage_env" }, { label: "展览借出", path: "/exhibition" }, { label: "文物运输", path: "/transport_relic" }, { label: "环境监控", path: "/environment_monitor" }, { label: "修复人员", path: "/personnel_relic" }, { label: "修复设备", path: "/equipment_relic" }, { label: "经费预算", path: "/budget_relic" }, { label: "修复报告", path: "/report_relic" }, { label: "文物保险", path: "/insurance_relic" }, { label: "出入记录", path: "/access_log" }]
</script>
