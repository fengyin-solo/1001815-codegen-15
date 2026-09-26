import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Relic = () => import('@/views/relic/index.vue')
const Diagnosis = () => import('@/views/diagnosis/index.vue')
const RestorePlan = () => import('@/views/restore_plan/index.vue')
const RestoreProject = () => import('@/views/restore_project/index.vue')
const Material = () => import('@/views/material/index.vue')
const RestoreProcess = () => import('@/views/restore_process/index.vue')
const PhotoRecord = () => import('@/views/photo_record/index.vue')
const QualityCheck = () => import('@/views/quality_check/index.vue')
const StorageEnv = () => import('@/views/storage_env/index.vue')
const Exhibition = () => import('@/views/exhibition/index.vue')
const TransportRelic = () => import('@/views/transport_relic/index.vue')
const EnvironmentMonitor = () => import('@/views/environment_monitor/index.vue')
const PersonnelRelic = () => import('@/views/personnel_relic/index.vue')
const EquipmentRelic = () => import('@/views/equipment_relic/index.vue')
const BudgetRelic = () => import('@/views/budget_relic/index.vue')
const ReportRelic = () => import('@/views/report_relic/index.vue')
const InsuranceRelic = () => import('@/views/insurance_relic/index.vue')
const AccessLog = () => import('@/views/access_log/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/relic', name: 'relic', component: Relic },
    { path: '/diagnosis', name: 'diagnosis', component: Diagnosis },
    { path: '/restore_plan', name: 'restore_plan', component: RestorePlan },
    { path: '/restore_project', name: 'restore_project', component: RestoreProject },
    { path: '/material', name: 'material', component: Material },
    { path: '/restore_process', name: 'restore_process', component: RestoreProcess },
    { path: '/photo_record', name: 'photo_record', component: PhotoRecord },
    { path: '/quality_check', name: 'quality_check', component: QualityCheck },
    { path: '/storage_env', name: 'storage_env', component: StorageEnv },
    { path: '/exhibition', name: 'exhibition', component: Exhibition },
    { path: '/transport_relic', name: 'transport_relic', component: TransportRelic },
    { path: '/environment_monitor', name: 'environment_monitor', component: EnvironmentMonitor },
    { path: '/personnel_relic', name: 'personnel_relic', component: PersonnelRelic },
    { path: '/equipment_relic', name: 'equipment_relic', component: EquipmentRelic },
    { path: '/budget_relic', name: 'budget_relic', component: BudgetRelic },
    { path: '/report_relic', name: 'report_relic', component: ReportRelic },
    { path: '/insurance_relic', name: 'insurance_relic', component: InsuranceRelic },
    { path: '/access_log', name: 'access_log', component: AccessLog },
  ],
})

export default router
