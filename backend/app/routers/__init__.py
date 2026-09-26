"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import relic as router_relic
from app.routers import diagnosis as router_diagnosis
from app.routers import restore_plan as router_restore_plan
from app.routers import restore_project as router_restore_project
from app.routers import material as router_material
from app.routers import restore_process as router_restore_process
from app.routers import photo_record as router_photo_record
from app.routers import quality_check as router_quality_check
from app.routers import storage_env as router_storage_env
from app.routers import exhibition as router_exhibition
from app.routers import transport_relic as router_transport_relic
from app.routers import environment_monitor as router_environment_monitor
from app.routers import personnel_relic as router_personnel_relic
from app.routers import equipment_relic as router_equipment_relic
from app.routers import budget_relic as router_budget_relic
from app.routers import report_relic as router_report_relic
from app.routers import insurance_relic as router_insurance_relic
from app.routers import access_log as router_access_log

ROUTERS = [router_relic, router_diagnosis, router_restore_plan, router_restore_project, router_material, router_restore_process, router_photo_record, router_quality_check, router_storage_env, router_exhibition, router_transport_relic, router_environment_monitor, router_personnel_relic, router_equipment_relic, router_budget_relic, router_report_relic, router_insurance_relic, router_access_log]
