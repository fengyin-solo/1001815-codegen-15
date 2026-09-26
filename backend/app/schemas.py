"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class RelicEntry(BaseModel):
    """文物明细结构。"""

    field_0: str | None = None  # 文物编号
    field_1: str | None = None  # 文物名称
    field_2: str | None = None  # 文物类别
    field_3: str | None = None  # 年代判定
    field_4: str | None = None  # 质地材料
    field_5: str | None = None  # 尺寸规格
    field_6: str | None = None  # 来源信息
    field_7: str | None = None  # 文物等级

class DiagnosisEntry(BaseModel):
    """病害记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 文物编号
    field_2: str | None = None  # 病害类型
    field_3: str | None = None  # 病害部位
    field_4: str | None = None  # 严重程度
    field_5: str | None = None  # 检测方法
    field_6: str | None = None  # 诊断日期
    field_7: str | None = None  # 诊断人员

class RestorePlanEntry(BaseModel):
    """修复方案明细结构。"""

    field_0: str | None = None  # 方案编号
    field_1: str | None = None  # 文物编号
    field_2: str | None = None  # 方案名称
    field_3: str | None = None  # 修复周期
    field_4: str | None = None  # 材料清单
    field_5: str | None = None  # 工艺路线
    field_6: str | None = None  # 编制人员
    field_7: str | None = None  # 方案状态

class RestoreProjectEntry(BaseModel):
    """修复项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 文物编号
    field_2: str | None = None  # 采用方案
    field_3: str | None = None  # 开工日期
    field_4: str | None = None  # 计划周期
    field_5: str | None = None  # 项目组长
    field_6: str | None = None  # 助理人数
    field_7: str | None = None  # 项目状态

class MaterialEntry(BaseModel):
    """修复材料明细结构。"""

    field_0: str | None = None  # 材料编号
    field_1: str | None = None  # 材料名称
    field_2: str | None = None  # 材料规格
    field_3: str | None = None  # 用途分类
    field_4: str | None = None  # 供应商
    field_5: str | None = None  # 入库日期
    field_6: str | None = None  # 有效期限
    field_7: str | None = None  # 材料状态

class RestoreProcessEntry(BaseModel):
    """修复工序明细结构。"""

    field_0: str | None = None  # 工序编号
    field_1: str | None = None  # 所属项目
    field_2: str | None = None  # 工序名称
    field_3: str | None = None  # 前置工序
    field_4: str | None = None  # 计划工时
    field_5: str | None = None  # 实际工时
    field_6: str | None = None  # 执行人员
    field_7: str | None = None  # 工序状态

class PhotoRecordEntry(BaseModel):
    """影像档案明细结构。"""

    field_0: str | None = None  # 影像编号
    field_1: str | None = None  # 文物编号
    field_2: str | None = None  # 拍摄类型
    field_3: str | None = None  # 拍摄部位
    field_4: str | None = None  # 拍摄日期
    field_5: str | None = None  # 拍摄人员
    field_6: str | None = None  # 存储路径
    field_7: str | None = None  # 影像状态

class QualityCheckEntry(BaseModel):
    """验收记录明细结构。"""

    field_0: str | None = None  # 验收编号
    field_1: str | None = None  # 所属项目
    field_2: str | None = None  # 验收节点
    field_3: str | None = None  # 验收标准
    field_4: str | None = None  # 验收人员
    field_5: str | None = None  # 验收日期
    field_6: str | None = None  # 是否合格
    field_7: str | None = None  # 验收状态

class StorageEnvEntry(BaseModel):
    """环境记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 存放处所
    field_2: str | None = None  # 温度值
    field_3: str | None = None  # 相对湿度
    field_4: str | None = None  # 光照强度
    field_5: str | None = None  # 记录时间
    field_6: str | None = None  # 调控设备
    field_7: str | None = None  # 环境状态

class ExhibitionEntry(BaseModel):
    """借展申请明细结构。"""

    field_0: str | None = None  # 申请编号
    field_1: str | None = None  # 文物编号
    field_2: str | None = None  # 借展单位
    field_3: str | None = None  # 展览名称
    field_4: str | None = None  # 借出日期
    field_5: str | None = None  # 归还日期
    field_6: str | None = None  # 押运方式
    field_7: str | None = None  # 申请状态

class TransportRelicEntry(BaseModel):
    """运输任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 文物编号
    field_2: str | None = None  # 出发地
    field_3: str | None = None  # 目的地
    field_4: str | None = None  # 承运单位
    field_5: str | None = None  # 押运人员
    field_6: str | None = None  # 预计到达
    field_7: str | None = None  # 任务状态

class EnvironmentMonitorEntry(BaseModel):
    """监控设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 监测点位
    field_2: str | None = None  # 设备类型
    field_3: str | None = None  # 温湿度量程
    field_4: str | None = None  # 上次校准
    field_5: str | None = None  # 下次校准
    field_6: str | None = None  # 当前读数
    field_7: str | None = None  # 设备状态

class PersonnelRelicEntry(BaseModel):
    """修复师明细结构。"""

    field_0: str | None = None  # 员工编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 修复专长
    field_3: str | None = None  # 职称等级
    field_4: str | None = None  # 从业年限
    field_5: str | None = None  # 执业证书号
    field_6: str | None = None  # 当前任务
    field_7: str | None = None  # 人员状态

class EquipmentRelicEntry(BaseModel):
    """修复设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 设备名称
    field_2: str | None = None  # 设备类型
    field_3: str | None = None  # 规格型号
    field_4: str | None = None  # 所属科室
    field_5: str | None = None  # 上次维保
    field_6: str | None = None  # 下次维保
    field_7: str | None = None  # 设备状态

class BudgetRelicEntry(BaseModel):
    """预算科目明细结构。"""

    field_0: str | None = None  # 科目编号
    field_1: str | None = None  # 科目名称
    field_2: str | None = None  # 预算类型
    field_3: str | None = None  # 批复金额
    field_4: str | None = None  # 已支出金额
    field_5: str | None = None  # 可用余额
    field_6: str | None = None  # 预算年度
    field_7: str | None = None  # 科目状态

class ReportRelicEntry(BaseModel):
    """修复报告明细结构。"""

    field_0: str | None = None  # 报告编号
    field_1: str | None = None  # 所属项目
    field_2: str | None = None  # 报告类型
    field_3: str | None = None  # 编写人
    field_4: str | None = None  # 编制日期
    field_5: str | None = None  # 报告摘要
    field_6: str | None = None  # 结论描述
    field_7: str | None = None  # 报告状态

class InsuranceRelicEntry(BaseModel):
    """保单明细结构。"""

    field_0: str | None = None  # 保单编号
    field_1: str | None = None  # 文物编号
    field_2: str | None = None  # 保险类型
    field_3: str | None = None  # 保险金额
    field_4: str | None = None  # 起保日期
    field_5: str | None = None  # 到期日期
    field_6: str | None = None  # 承保机构
    field_7: str | None = None  # 保单状态

class AccessLogEntry(BaseModel):
    """出入记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 文物编号
    field_2: str | None = None  # 操作类型
    field_3: str | None = None  # 经办人
    field_4: str | None = None  # 进出时间
    field_5: str | None = None  # 事由说明
    field_6: str | None = None  # 审批人
    field_7: str | None = None  # 记录状态
