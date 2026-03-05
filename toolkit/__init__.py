"""
AI Productivity Toolkit
核心工具库
"""

from .prompt_optimizer import PromptOptimizer
from .excel_tools import ExcelAutomation
from .data_collector import DataCollector
from .workflow import AIWorkflow

__version__ = "0.1.0"
__author__ = "AI Research Assistant"

__all__ = [
    "PromptOptimizer",
    "ExcelAutomation", 
    "DataCollector",
    "AIWorkflow"
]
