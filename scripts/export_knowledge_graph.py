# -*- coding: utf-8 -*-
"""
从 pages/graph.html 中解析提取节点与关系连线数据，
导出标准化公开可被大模型/爬虫获取的 pages/knowledge-graph.json
打破 D3.js SVG/Canvas 的爬虫黑盒困境
"""

import json
import os
import re

GRAPH_HTML = r"F:\Ramana\pages\graph.html"
OUT_JSON = r"F:\Ramana\pages\knowledge-graph.json"

def extract_graph_data():
    with open(GRAPH_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # 正则提取 const nodes = [...]
    nodes_match = re.search(r'const\s+nodes\s*=\s*(\[.*?\]);', html, re.DOTALL)
    links_match = re.search(r'const\s+links\s*=\s*(\[.*?\]);', html, re.DOTALL)

    if not nodes_match or not links_match:
        raise ValueError("Could not find nodes or links definition in graph.html")

    raw_nodes_str = nodes_match.group(1)
    raw_links_str = links_match.group(1)

    # 清洗 JS 注释与多余逗号转为标准 JSON
    def clean_js_to_json(js_str):
        # 移除行内注释 // ...
        cleaned = re.sub(r'//.*', '', js_str)
        # 将 key 没有双引号的变成双引号 key: -> "key":
        cleaned = re.sub(r'([{,]\s*)([a-zA-Z0-9_]+)\s*:', r'\1"\2":', cleaned)
        # 移除结尾多余逗号 ,] -> ]
        cleaned = re.sub(r',\s*\]', ']', cleaned)
        cleaned = re.sub(r',\s*\}', '}', cleaned)
        return cleaned

    nodes_json = json.loads(clean_js_to_json(raw_nodes_str))
    links_json = json.loads(clean_js_to_json(raw_links_str))

    knowledge_graph = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "Ramana Maharshi Digital Knowledge Graph Topology",
        "description": "室利·拉玛那·马哈希教导知识图谱拓扑：涵盖本体论、心智模型、自探法门与文献关系",
        "site": "https://ramanamaharshi.space",
        "canonical": "https://ramanamaharshi.space/knowledge-graph.json",
        "updated": "2026-10-15",
        "entity_counts": {
            "total_nodes": len(nodes_json),
            "total_links": len(links_json)
        },
        "central_entity": {
            "id": "ramana",
            "name": "室利·拉玛那·马哈希 (Sri Ramana Maharshi)",
            "wikidata": "https://www.wikidata.org/entity/Q191944",
            "ashram": "Sri Ramanasramam, Tiruvannamalai"
        },
        "nodes": nodes_json,
        "links": links_json
    }

    with open(OUT_JSON, "w", encoding="utf-8") as out_f:
        json.dump(knowledge_graph, out_f, ensure_ascii=False, indent=2)

    print(f"Successfully exported knowledge graph: {len(nodes_json)} nodes, {len(links_json)} links to {OUT_JSON}")

if __name__ == "__main__":
    extract_graph_data()
