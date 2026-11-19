#!/usr/bin/env python3
"""Gitrule MCP 服务器。

基于 JSON-RPC 2.0，使用标准输入输出逐行通信。
同时兼容新版 server/discover 与旧版 initialize 发现方式。
"""

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "cli"))
import gitrule  # noqa: E402

PROTOCOL_VERSION = "2026-07-28"
SUPPORTED_VERSIONS = ["2026-07-28", "2024-11-05"]
SERVER_INFO = {"name": "gitrule-mcp", "version": "1.0.0"}


def send(message):
    """向标准输出写出一条 JSON-RPC 消息。"""
    sys.stdout.write(json.dumps(message, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def error(message_id, code, text):
    """写出标准 JSON-RPC 错误。"""
    send({
        "jsonrpc": "2.0",
        "id": message_id,
        "error": {"code": code, "message": text},
    })


def text_result(message_id, text, is_error=False):
    """写出文本形式工具结果。"""
    send({
        "jsonrpc": "2.0",
        "id": message_id,
        "result": {
            "content": [{"type": "text", "text": text}],
            "isError": is_error,
        },
    })


def tools():
    """返回工具清单。"""
    return [
        {
            "name": "gitrule_check",
            "title": "检查文档规范",
            "description": "检查断链、孤岛、职责句、占位符、代码围栏与索引计数，返回结构化问题列表。",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "仓库根目录，默认当前目录"},
                    "lang": {"type": "string", "description": "语言码或 all，默认 all"},
                },
            },
        },
        {
            "name": "gitrule_optimize",
            "title": "安全优化文档",
            "description": "默认只报告可安全修复项；fix 为 true 时补齐裸代码块语言标识，backup 可生成备份。",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "仓库根目录，默认当前目录"},
                    "lang": {"type": "string", "description": "语言码或 all，默认 all"},
                    "fix": {"type": "boolean", "description": "是否实际写入，默认 false"},
                    "backup": {"type": "boolean", "description": "写入前是否生成 .bak，默认 false"},
                },
            },
        },
        {
            "name": "gitrule_list_specs",
            "title": "列出规范文件",
            "description": "列出指定语言目录内的全部规范文件名。",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "仓库根目录，默认当前目录"},
                    "lang": {"type": "string", "description": "语言码，默认 zh-CN"},
                },
            },
        },
        {
            "name": "gitrule_get_spec",
            "title": "读取规范全文",
            "description": "按语言码和文件名读取单篇规范全文。",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "仓库根目录，默认当前目录"},
                    "lang": {"type": "string", "description": "语言码，默认 zh-CN"},
                    "name": {"type": "string", "description": "文件名，例如 硬规则.md"},
                },
                "required": ["name"],
            },
        },
        {
            "name": "gitrule_language_status",
            "title": "查看语言适配状态",
            "description": "从根 README 语言表读取每种语言的完成状态。",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "仓库根目录，默认当前目录"},
                },
            },
        },
        {
            "name": "gitrule_xcheck",
            "title": "跨语种结构校验",
            "description": "以某一语种为基准，比对其他语种的标题、围栏、链接、列表、表格行列与占位符是否一致，返回结构化差异列表。",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "仓库根目录，默认当前目录"},
                    "lang": {"type": "string", "description": "待比对语言码或 all，默认 all"},
                    "reference": {"type": "string", "description": "参考语种，默认 zh-CN"},
                },
            },
        },
    ]


def run_tool(name, arguments):
    """执行工具并返回文本结果。"""
    root = os.path.abspath(arguments.get("path", "."))
    if name == "gitrule_check":
        langs = gitrule.SUPPORTED_LANGS if arguments.get("lang", "all") == "all" else (arguments["lang"],)
        issues = []
        for lang in langs:
            issues.extend(gitrule.check_language(root, lang))
        return json.dumps({"languages": langs, "issueCount": len(issues), "issues": issues}, ensure_ascii=False, indent=2)
    if name == "gitrule_optimize":
        langs = gitrule.SUPPORTED_LANGS if arguments.get("lang", "all") == "all" else (arguments["lang"],)
        changes = []
        for lang in langs:
            result = gitrule.optimize(root, lang, bool(arguments.get("fix")), bool(arguments.get("backup")))
            for item in result["changes"]:
                changes.append({"lang": lang, **item})
        return json.dumps({"planned": len(changes), "changes": changes}, ensure_ascii=False, indent=2)
    if name == "gitrule_list_specs":
        return json.dumps(gitrule.list_specs(root, arguments.get("lang", "zh-CN")), ensure_ascii=False, indent=2)
    if name == "gitrule_get_spec":
        return gitrule.get_spec(root, arguments.get("lang", "zh-CN"), arguments.get("name", ""))
    if name == "gitrule_language_status":
        return json.dumps(gitrule.language_status(root), ensure_ascii=False, indent=2)
    if name == "gitrule_xcheck":
        reference = arguments.get("reference", "zh-CN")
        langs = [lang for lang in gitrule.SUPPORTED_LANGS if lang != reference]
        if arguments.get("lang", "all") != "all":
            langs = [arguments["lang"]]
        issues = []
        for lang in langs:
            issues.extend(gitrule.cross_check_language(root, lang, reference))
        return json.dumps(
            {"reference": reference, "compared": langs, "issueCount": len(issues), "issues": issues},
            ensure_ascii=False,
            indent=2,
        )
    raise ValueError(f"未知工具：{name}")


def handle(message):
    """处理单条 JSON-RPC 消息。"""
    if "id" not in message:
        return
    message_id = message["id"]
    method = message.get("method")
    params = message.get("params") or {}

    if method == "server/discover":
        send({
            "jsonrpc": "2.0",
            "id": message_id,
            "result": {
                "supportedVersions": SUPPORTED_VERSIONS,
                "capabilities": {"tools": {"listChanged": False}},
                "_meta": {"io.modelcontextprotocol/serverInfo": SERVER_INFO},
            },
        })
        return

    if method == "initialize":
        send({
            "jsonrpc": "2.0",
            "id": message_id,
            "result": {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {}},
                "serverInfo": SERVER_INFO,
            },
        })
        return

    if method == "tools/list":
        send({
            "jsonrpc": "2.0",
            "id": message_id,
            "result": {
                "tools": tools(),
                "resultType": "complete",
                "ttlMs": 300000,
                "cacheScope": "public",
            },
        })
        return

    if method == "tools/call":
        name = params.get("name")
        arguments = params.get("arguments") or {}
        try:
            text_result(message_id, run_tool(name, arguments))
        except Exception as exc:  # noqa: BLE001 - 向客户端返回可读错误
            text_result(message_id, f"工具执行失败：{exc}", is_error=True)
        return

    error(message_id, -32601, f"不支持的方法：{method}")


def main():
    """标准输入输出主循环。"""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            message = json.loads(line)
        except json.JSONDecodeError:
            error(None, -32700, "JSON 解析失败")
            continue
        try:
            handle(message)
        except Exception as exc:  # noqa: BLE001 - 保证服务不因单条消息退出
            error(message.get("id"), -32603, str(exc))


if __name__ == "__main__":
    main()
