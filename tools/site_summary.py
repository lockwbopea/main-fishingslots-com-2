import sys
import json
import datetime

SITE_DATA = [
    {
        "title": "捕鱼游戏大全",
        "url": "https://main-fishingslots.com",
        "tags": ["捕鱼", "街机", "休闲"],
        "description": "汇集各类捕鱼主题游戏，提供在线试玩与攻略。"
    },
    {
        "title": "深海猎手",
        "url": "https://main-fishingslots.com/deep-sea",
        "tags": ["捕鱼", "深海", "射击"],
        "description": "潜入深海捕捉稀有鱼种，赢取丰厚奖励。"
    },
    {
        "title": "渔王争霸",
        "url": "https://main-fishingslots.com/fishing-king",
        "tags": ["捕鱼", "竞技", "多人"],
        "description": "与其他玩家实时比拼捕鱼技巧，争夺渔王称号。"
    }
]

KEYWORDS = ["捕鱼游戏", "街机捕鱼", "深海捕鱼", "捕鱼达人"]

def build_summary_entry(entry):
    tags_str = ", ".join(entry["tags"])
    return {
        "name": entry["title"],
        "url": entry["url"],
        "keywords": tags_str,
        "brief": entry["description"]
    }

def generate_summary(data):
    summary_list = []
    for item in data:
        summary_list.append(build_summary_entry(item))
    return summary_list

def format_output(summary_data, keywords):
    lines = []
    lines.append("=" * 50)
    lines.append("SITE SUMMARY REPORT")
    lines.append(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 50)
    lines.append("")
    lines.append("Core Keywords:")
    lines.append(f"  - {' | '.join(keywords)}")
    lines.append("")
    lines.append("Site Entries:")
    for idx, entry in enumerate(summary_data, 1):
        lines.append(f"  [{idx}] {entry['name']}")
        lines.append(f"       URL: {entry['url']}")
        lines.append(f"       Tags: {entry['keywords']}")
        lines.append(f"       Desc: {entry['brief']}")
        lines.append("")
    lines.append("=" * 50)
    lines.append("End of summary.")
    return "\n".join(lines)

def main():
    summary = generate_summary(SITE_DATA)
    report = format_output(summary, KEYWORDS)
    print(report)

if __name__ == "__main__":
    main()