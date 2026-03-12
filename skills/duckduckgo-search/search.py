#!/usr/bin/env python3
"""
简单的 DuckDuckGo 搜索脚本
使用 HTML 解析方式，无需额外依赖
"""

import argparse
import sys
import re
import urllib.parse
import urllib.request


def search_duckduckgo(query, limit=5):
    """
    使用 DuckDuckGo HTML 搜索
    
    Args:
        query: 搜索关键词
        limit: 返回结果数量
    
    Returns:
        搜索结果列表
    """
    results = []
    
    # 构建搜索 URL
    encoded_query = urllib.parse.quote(query)
    url = f"https://html.duckduckgo.com/html/?q={encoded_query}"
    
    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode("utf-8")
            
            # 简单的 HTML 解析（不使用 BeautifulSoup 避免依赖）
            # 查找结果链接和标题
            result_pattern = r'<a[^>]*class="result__a"[^>]*href="([^"]+)"[^>]*>([^<]+)</a>'
            snippet_pattern = r'<a[^>]*class="result__snippet"[^>]*>([^<]+)</a>'
            
            links = re.findall(result_pattern, html)
            snippets = re.findall(snippet_pattern, html)
            
            for i, (url, title) in enumerate(links[:limit]):
                # 解码 URL（DuckDuckGo 会重定向）
                if url.startswith("/"):
                    url = "https://duckduckgo.com" + url
                
                snippet = snippets[i] if i < len(snippets) else ""
                
                # 清理 HTML 实体
                title = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))), title)
                snippet = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))), snippet)
                
                results.append({
                    "title": title,
                    "url": url,
                    "snippet": snippet
                })
                
    except Exception as e:
        print(f"搜索出错: {e}", file=sys.stderr)
    
    return results


def print_results(results):
    """
    打印搜索结果
    """
    if not results:
        print("未找到搜索结果")
        return
    
    print(f"\n找到 {len(results)} 条结果:\n")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['title']}")
        print(f"   链接: {result['url']}")
        if result['snippet']:
            print(f"   摘要: {result['snippet']}")
        print()


def main():
    parser = argparse.ArgumentParser(description="DuckDuckGo 网页搜索")
    parser.add_argument("query", help="搜索关键词")
    parser.add_argument("--limit", type=int, default=5, help="返回结果数量 (默认: 5)")
    
    args = parser.parse_args()
    
    results = search_duckduckgo(args.query, args.limit)
    print_results(results)


if __name__ == "__main__":
    main()
