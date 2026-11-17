# 附录B：经典算法与核心公式速查

- MC：用完整实际回报更新价值，少自举偏差，但可能高方差。
- TD：目标为即时奖励加下一状态估计价值。
- Q-learning：目标使用下一状态的最大 Q；终止状态不加后续价值。
- 策略梯度：利用 $\nabla_\theta\log\pi_\theta(a\mid h)$ 与回报/优势的乘积估计改进方向。
- GAE：$\hat A_t=\sum_l(\gamma\lambda)^l\delta_{t+l}$，其中 $\delta_t=r_t+\gamma V(h_{t+1})-V(h_t)$；边界项需按终止语义处理。
- PPO：新旧概率比与裁剪代理目标，见第04章。

GAE 中 $\lambda$ 控制不同跨度误差的权重；它与奖励成本权重是不同概念。[GAE 原论文](https://arxiv.org/abs/1506.02438)
<!-- navigation -->

---

[目录](../README.md) · [上一附录](a-glossary.md) · [下一附录](c-pseudocode.md)
