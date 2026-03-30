import numpy as np
import matplotlib.pyplot as plt

def calculate_metabolic_cost(rho, theta=1.0):
    """
    基于存在补丁主义 (EP) 的核心推导：
    C = theta / (1 - rho)
    当 rho (延迟比率) 接近 1 时，系统代价 C 趋向无穷大，触发熔断。
    """
    # 防止除以零，模拟系统崩溃
    cost = theta / (1 - rho)
    return cost

def run_stability_simulation():
    print("--- 系统动力学稳定性仿真启动 (EP Framework) ---")
    
    # 模拟从 低延迟 到 临界延迟 的过程
    rho_values = np.linspace(0, 0.95, 100) 
    costs = [calculate_metabolic_cost(r) for r in rho_values]
    
    # 判定熔断点 (假设代价超过 10 单位为预警，15 单位为熔断)
    threshold = 10
    melt_point = rho_values[np.where(np.array(costs) > threshold)[0][0]]
    
    print(f"系统正常运行区间: rho < {melt_point:.2f}")
    print(f"临界状态: 当 rho 超过 {melt_point:.2f}，代谢代价 C 将呈指数级激增。")

    # 可视化展示 (这是吸引 GitHub 用户的核心)
    plt.figure(figsize=(10, 6))
    plt.plot(rho_values, costs, label='Metabolic Cost (C)', color='red', linewidth=2)
    plt.axhline(y=threshold, color='gray', linestyle='--', label='System Threshold (Theta)')
    plt.fill_between(rho_values, costs, where=(np.array(costs) > threshold), color='orange', alpha=0.3, label='Risk Zone (Patch Overload)')
    
    plt.title("System Stability Curve: Cost vs. Delay Ratio", fontsize=14)
    plt.xlabel("Delay Ratio (rho) - [Information Lag]", fontsize=12)
    plt.ylabel("Metabolic Cost (C) - [Existence Pain]", fontsize=12)
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.legend()
    
    print("生成稳定性曲线图中...")
    plt.show()

if __name__ == "__main__":
    run_stability_simulation()