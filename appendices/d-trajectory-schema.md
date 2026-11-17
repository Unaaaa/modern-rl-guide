# 附录D：环境与轨迹记录示例

```json
{
  "task_id": "synthetic-0001",
  "environment_version": "aml-design-v0",
  "policy_version": "blue-demo",
  "steps": [{
    "turn": 0,
    "role": "investigator",
    "observation_ref": "snapshot-0001",
    "action": {"tool": "query_history", "entity": "synthetic-A"},
    "result_ref": "result-0001",
    "cost": 1,
    "reward_parts": {"tool_cost": -1},
    "terminated": false,
    "truncated": false
  }]
}
```

这是字段示例。正式训练需补足终局奖励、行为 log-prob、token 掩码、耗时、权限与完整结束原因。观测引用必须能恢复当时可见内容，同时避免在策略输入中暴露隐藏标签。
<!-- navigation -->

---

[目录](../README.md) · [上一附录](c-pseudocode.md) · [下一附录](e-project-template.md)
