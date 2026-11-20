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
SERVER_INFO = {"name": "gitrule-mcp", "version": "1.1.0"}

# JSON-RPC 2.0 标准错误码
PARSE_ERROR = -32700
INVALID_REQUEST = -32600
METHOD_NOT_FOUND = -32601
INVALID_PARAMS = -32602
INTERNAL_ERROR = -32603


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
            "description": "按语言码和文件名读取单篇规范全文；只允许读语种目录下的 .md 文件。",
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
        {
            "name": "gitrule_termcheck",
            "title": "术语矩阵校验",
            "description": "校验术语表的译名矩阵与各语种正文用词是否自洽：矩阵登记的译名是否真在正文出现，变格语言的词干是否匹配。",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "仓库根目录，默认当前目录"},
                    "lang": {"type": "string", "description": "语言码或 all，默认 all"},
                },
            },
        },
    ]


def require_locales(root):
    """校验仓库根目录结构，缺失时抛出可读异常。"""
    locales = Path(root) / "locales"
    if not locales.is_dir():
        raise ValueError(f"未找到 {locales}，请用 path 参数指定仓库根目录")
    return locales


def resolve_langs(arguments):
    """解析 lang 参数，与 CLI 保持同一语义。"""
    lang = arguments.get("lang", "all")
    if lang == "all":
        return gitrule.SUPPORTED_LANGS
    return (lang,)


def run_tool(name, arguments):
    """执行工具并返回文本结果。

    返回体与 CLI 的 JSON 输出保持同一字段语义，便于客户端复用解析逻辑。
    """
    root = os.path.abspath(arguments.get("path") or ".")

    if name == "gitrule_check":
        require_locales(root)
        langs = resolve_langs(arguments)
        issues = []
        for lang in langs:
            issues.extend(gitrule.check_language(root, lang))
        return json.dumps(
            {"kind": "check", "languages": list(langs), "issueCount": len(issues), "issues": issues},
            ensure_ascii=False, indent=2,
        )

    if name == "gitrule_optimize":
        require_locales(root)
        langs = resolve_langs(arguments)
        changes = []
        fixed = 0
        for lang in langs:
            result = gitrule.optimize(root, lang, bool(arguments.get("fix")), bool(arguments.get("backup")))
            fixed += result["fixed"]
            for item in result["changes"]:
                changes.append({"lang": lang, **item})
        return json.dumps(
            {"kind": "optimize", "planned": len(changes), "fixed": fixed, "changes": changes},
            ensure_ascii=False, indent=2,
        )

    if name == "gitrule_list_specs":
        require_locales(root)
        return json.dumps(
            {"kind": "list", "specs": gitrule.list_specs(root, arguments.get("lang", "zh-CN"))},
            ensure_ascii=False, indent=2,
        )

    if name == "gitrule_get_spec":
        require_locales(root)
        spec_name = arguments.get("name", "")
        if not spec_name:
            raise ValueError("缺少必填参数 name")
        return gitrule.get_spec(root, arguments.get("lang", "zh-CN"), spec_name)

    if name == "gitrule_language_status":
        return json.dumps(
            {"kind": "status", "languages": gitrule.language_status(root)},
            ensure_ascii=False, indent=2,
        )

    if name == "gitrule_xcheck":
        require_locales(root)
        reference = arguments.get("reference", "zh-CN")
        if not (Path(root) / "locales" / reference).is_dir():
            raise ValueError(f"参考语种目录不存在：locales/{reference}")
        lang = arguments.get("lang", "all")
        if lang != "all" and lang == reference:
            raise ValueError("待比对语种与参考语种相同，无需比对")
        langs = [code for code in gitrule.SUPPORTED_LANGS if code != reference]
        if lang != "all":
            langs = [lang]
        issues = []
        for code in langs:
            issues.extend(gitrule.cross_check_language(root, code, reference))
        return json.dumps(
            {"kind": "xcheck", "reference": reference, "compared": langs,
             "issueCount": len(issues), "issues": issues},
            ensure_ascii=False, indent=2,
        )

    if name == "gitrule_termcheck":
        require_locales(root)
        langs = resolve_langs(arguments)
        issues = []
        for lang in langs:
            issues.extend(gitrule.term_check_language(root, lang))
        return json.dumps(
            {"kind": "termcheck", "languages": list(langs), "terms": list(gitrule.TERM_MATRIX_TERMS),
             "issueCount": len(issues), "issues": issues},
            ensure_ascii=False, indent=2,
        )

    raise ValueError(f"未知工具：{name}")


def handle(message):
    """处理单条 JSON-RPC 消息。

    通知（带 method 但无 id）按规范不回复；id 与 method 都缺失的畸形
    请求返回 -32600，而不是静默丢弃。
    """
    message_id = message.get("id")
    method = message.get("method")
    if method is None:
        if message_id is None:
            error(None, INVALID_REQUEST, "缺少 method 字段")
        return
    if message_id is None:
        return

    params = message.get("params") or {}
    if not isinstance(params, dict):
        error(message_id, INVALID_PARAMS, "params 必须是对象")
        return

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
        tool_name = params.get("name")
        if not tool_name:
            error(message_id, INVALID_PARAMS, "缺少工具名 name")
            return
        tool_args = params.get("arguments") or {}
        if not isinstance(tool_args, dict):
            error(message_id, INVALID_PARAMS, "arguments 必须是对象")
            return
        try:
            text_result(message_id, run_tool(tool_name, tool_args))
        except ValueError as exc:
            text_result(message_id, f"参数错误：{exc}", is_error=True)
        except (OSError, UnicodeDecodeError) as exc:
            text_result(message_id, f"读取文件失败：{exc}", is_error=True)
        except Exception as exc:  # noqa: BLE001 - 向客户端返回可读错误，不中断服务
            text_result(message_id, f"工具执行失败：{exc}", is_error=True)
        return

    error(message_id, METHOD_NOT_FOUND, f"不支持的方法：{method}")


def main():
    """标准输入输出主循环。"""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            message = json.loads(line)
        except json.JSONDecodeError as exc:
            error(None, PARSE_ERROR, f"JSON 解析失败：{exc.msg}")
            continue
        if not isinstance(message, dict):
            error(None, INVALID_REQUEST, "消息必须是 JSON 对象")
            continue
        try:
            handle(message)
        except Exception as exc:  # noqa: BLE001 - 保证服务不因单条消息退出
            error(message.get("id"), INTERNAL_ERROR, str(exc))


if __name__ == "__main__":
    main()
