"""
Prompt 优化器
自动优化 AI 提示词，提升输出质量
"""

class PromptOptimizer:
    """Prompt 优化器 - 让 AI 理解更准确，输出更优质"""
    
    def __init__(self):
        self.templates = {
            "general": self._general_template(),
            "coding": self._coding_template(),
            "writing": self._writing_template(),
            "analysis": self._analysis_template(),
        }
    
    def _general_template(self):
        return """你是一位专业的{role}。请完成以下任务：

【任务要求】
1. 输出专业、准确、有条理
2. 考虑全面，包含必要的细节
3. 提供实用的建议/方案
4. 如有必要，给出示例

【任务内容】
{task}

【输出格式】
{format}"""

    def _coding_template(self):
        return """你是一位资深{language}开发者。请编写代码：

【代码要求】
1. 功能完整，逻辑清晰
2. 遵循最佳实践和代码规范
3. 包含必要的注释和文档字符串
4. 考虑边界情况和错误处理
5. 提供使用示例

【功能需求】
{task}

【技术栈】
{tech_stack}

【输出内容】
- 完整可运行的代码
- 使用说明
- 测试示例"""

    def _writing_template(self):
        return """你是一位专业的内容创作者。请撰写：

【内容要求】
1. 主题明确，重点突出
2. 结构清晰，逻辑连贯
3. 语言生动，引人入胜
4. 符合目标受众的阅读习惯

【主题】
{topic}

【目标受众】
{audience}

【字数要求】
{word_count}

【风格要求】
{style}"""

    def _analysis_template(self):
        return """你是一位资深数据分析师。请分析以下内容：

【分析要求】
1. 客观、全面、深入
2. 数据驱动，有依据
3. 给出可执行的建议
4. 指出潜在风险和机会

【分析对象】
{content}

【分析维度】
{dimensions}

【输出格式】
1. 核心发现
2. 详细分析
3. 结论建议"""

    def optimize(self, prompt: str, task_type: str = "general", **kwargs) -> str:
        """
        优化提示词
        
        Args:
            prompt: 原始提示词
            task_type: 任务类型 (general/coding/writing/analysis)
            **kwargs: 额外参数
            
        Returns:
            优化后的提示词
        """
        template = self.templates.get(task_type, self.templates["general"])
        
        # 智能填充参数
        params = {
            "role": self._detect_role(task_type),
            "task": prompt,
            "format": kwargs.get("format", "清晰、结构化"),
            "topic": prompt,
            "audience": kwargs.get("audience", "普通读者"),
            "word_count": kwargs.get("word_count", "1000-2000 字"),
            "style": kwargs.get("style", "专业且易懂"),
            "language": kwargs.get("language", "Python"),
            "tech_stack": kwargs.get("tech_stack", "最新最佳实践"),
            "content": prompt,
            "dimensions": kwargs.get("dimensions", "趋势、问题、机会"),
        }
        
        return template.format(**params)
    
    def _detect_role(self, task_type: str) -> str:
        """根据任务类型检测角色"""
        role_map = {
            "general": "助手",
            "coding": "开发者",
            "writing": "内容创作者",
            "analysis": "分析师",
        }
        return role_map.get(task_type, "专家")
    
    def quick_optimize(self, prompt: str) -> str:
        """
        快速优化 - 自动检测任务类型
        
        Args:
            prompt: 原始提示词
            
        Returns:
            优化后的提示词
        """
        # 简单关键词检测
        prompt_lower = prompt.lower()
        
        if any(kw in prompt_lower for kw in ["代码", "编程", "python", "script", "code"]):
            return self.optimize(prompt, "coding")
        elif any(kw in prompt_lower for kw in ["写文章", "文案", "内容", "writing"]):
            return self.optimize(prompt, "writing")
        elif any(kw in prompt_lower for kw in ["分析", "数据", "趋势", "analysis"]):
            return self.optimize(prompt, "analysis")
        else:
            return self.optimize(prompt, "general")


# 使用示例
if __name__ == "__main__":
    optimizer = PromptOptimizer()
    
    # 示例 1：通用任务
    prompt1 = "帮我写一个周报"
    optimized1 = optimizer.quick_optimize(prompt1)
    print("优化前:", prompt1)
    print("优化后:", optimized1)
    print("-" * 50)
    
    # 示例 2：编程任务
    prompt2 = "写一个 Python 脚本处理 Excel"
    optimized2 = optimizer.quick_optimize(prompt2)
    print("优化前:", prompt2)
    print("优化后:", optimized2)
