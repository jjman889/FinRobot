from autogen import register_function, ConversableAgent
from .data_source import *
from .functional.coding import CodingUtils
from .functional.financial_analysis import calculate_financial_ratios
from .functional.text_analysis import analyze_text

from typing import List, Callable
from functools import wraps
from pandas import DataFrame


def stringify_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, DataFrame):
            return result.to_string()
        else:
            return str(result)

    return wrapper


def register_toolkits(
    config: List[dict | Callable | type],
    caller: ConversableAgent,
    executor: ConversableAgent,
    **kwargs
):
    """Register tools from a configuration list."""

    for tool in config:

        if isinstance(tool, type):
            register_tookits_from_cls(caller, executor, tool, **kwargs)
            continue

        tool_dict = {"function": tool} if callable(tool) else tool
        if "function" not in tool_dict or not callable(tool_dict["function"]):
            raise ValueError(
                "Function not found in tool configuration or not callable."
            )

        tool_function = tool_dict["function"]
        name = tool_dict.get("name", tool_function.__name__)
        description = tool_dict.get("description", tool_function.__doc__)
        register_function(
            stringify_output(tool_function),
            caller=caller,
            executor=executor,
            name=name,
            description=description,
        )


def register_code_writing(caller: ConversableAgent, executor: ConversableAgent):
    """Register code writing tools."""

    register_toolkits(
register_tookits_from_cls(caller, executor, SECUtils)
register_tookits_from_cls(caller, executor, SECUtils)
{
                "function": analyze_text,
                "name": "analyze_text",
                "description": "Analyzes the text of a document, performing sentiment analysis and keyword extraction.",
            },
{
                "function": calculate_financial_ratios,
                "name": "calculate_financial_ratios",
                "description": "Calculates key financial ratios from a company's financial data.",
            },
        [
            {
                "function": CodingUtils.list_dir,
                "name": "list_files",
                "description": "List files in a directory.",
            },
            {
                "function": CodingUtils.see_file,
                "name": "see_file",
                "description": "Check the contents of a chosen file.",
            },
            {
                "function": CodingUtils.modify_code,
                "name": "modify_code",
                "description": "Replace old piece of code with new one.",
            },
            {
                "function": CodingUtils.create_file_with_code,
                "name": "create_file_with_code",
                "description": "Create a new file with provided code.",
            },
        ],
        caller,
        executor,
    )


def register_tookits_from_cls(
    caller: ConversableAgent,
    executor: ConversableAgent,
    cls: type,
    include_private: bool = False,
):
    """Register all methods of a class as tools."""
    if include_private:
        funcs = [
            func
            for func in dir(cls)
            if callable(getattr(cls, func)) and not func.startswith("__")
        ]
    else:
        funcs = [
            func
            for func in dir(cls)
            if callable(getattr(cls, func))
            and not func.startswith("__")
            and not func.startswith("_")
        ]
    register_toolkits([getattr(cls, func) for func in funcs], caller, executor)
