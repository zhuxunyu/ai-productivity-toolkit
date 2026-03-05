"""
示例：使用 Prompt 优化器
"""

from toolkit import PromptOptimizer

def main():
    optimizer = PromptOptimizer()
    
    print("=" * 60)
    print("Prompt 优化器 - 使用示例")
    print("=" * 60)
    
    # 示例 1：通用任务
    print("\n【示例 1：通用任务】")
    prompt1 = "帮我写一个周报"
    optimized1 = optimizer.quick_optimize(prompt1)
    print(f"\n优化前：{prompt1}")
    print(f"\n优化后：\n{optimized1}")
    
    # 示例 2：编程任务
    print("\n" + "=" * 60)
    print("【示例 2：编程任务】")
    prompt2 = "写一个 Python 脚本处理 Excel"
    optimized2 = optimizer.quick_optimize(prompt2)
    print(f"\n优化前：{prompt2}")
    print(f"\n优化后：\n{optimized2}")
    
    # 示例 3：写作任务
    print("\n" + "=" * 60)
    print("【示例 3：写作任务】")
    prompt3 = "写一篇关于 AI 的文章"
    optimized3 = optimizer.optimize(
        prompt3, 
        "writing",
        audience="科技爱好者",
        word_count="1500-2000 字",
        style="专业且有趣"
    )
    print(f"\n优化前：{prompt3}")
    print(f"\n优化后：\n{optimized3}")
    
    # 示例 4：分析任务
    print("\n" + "=" * 60)
    print("【示例 4：分析任务】")
    prompt4 = "分析这个数据集"
    optimized4 = optimizer.optimize(
        prompt4,
        "analysis",
        dimensions="趋势、异常、相关性"
    )
    print(f"\n优化前：{prompt4}")
    print(f"\n优化后：\n{optimized4}")

if __name__ == "__main__":
    main()
