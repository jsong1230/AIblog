#!/usr/bin/env python3
"""
영어 포스트의 태그를 주제별로 통합하는 스크립트
"""
import frontmatter
from pathlib import Path
from collections import Counter

# 태그 통합 매핑
TAG_CONSOLIDATION = {
    # AI 자동화 관련
    'AI YouTube Automated Channel': 'AI Automation',
    'AI Reels Automation': 'AI Automation',
    'AI Vlog Generation': 'AI Automation',
    'AI Report Automation': 'AI Automation',
    'AI PDF eBook': 'AI Automation',
    'AI Discord Summary Bot': 'AI Automation',
    'The Rise of AI Tool Sales': 'AI Automation',
    'AI TikTok Automation': 'AI Automation',
    'AI Passive Income System': 'AI Automation',
    'SERP AI Automation': 'AI Automation',
    'K-Content AI Automation': 'AI Automation',
    
    # 개발 관련
    'API Development Guide': 'Development',
    'React Development': 'Development',
    'Database Design': 'Development',
    'Refactoring Techniques': 'Development',
    'Developer Roadmap': 'Development',
    'Performance Monitoring': 'Development',
    'Backend Security': 'Development',
    'Software Architecture': 'Development',
    'Mobile App Development': 'Development',
    'Tech Interview Preparation': 'Development',
    'Docker Container Usage': 'Development',
    'Cloud Service Comparison': 'Development',
    'Participating in Developer Community': 'Development',
    
    # 학습 관련
    'Algorithm Learning Methods': 'Learning',
    'Coding Learning Methods': 'Learning',
    'ChatGPT Usage': 'Learning',
    'Contributing to Open Source': 'Learning',
    
    # 온라인 비즈니스
    'Starting an Online Business': 'Online Business',
    'Online shopping tips': 'Online Business',
    'Digital Marketing Strategy': 'Online Business',
    'Mastering Subscription Service Operation': 'Online Business',
    'Selling Digital Products': 'Online Business',
    'The First Steps to Starting an Online Business': 'Online Business',
    
    # 블록체인/암호화폐
    'Understanding On-Chain Bridge Risks': 'Blockchain',
    'SOL On-chain Analysis': 'Blockchain',
    'NUPL Indicator AI': 'Blockchain',
    'Bitcoin On-chain Analysis': 'Blockchain',
    'AI ETF On-chain Analysis': 'Blockchain',
    '5 Essential Checklists to Avoid DeFi Risks': 'Blockchain',
    'LLM On-chain Analysis': 'Blockchain',
    'Glassnode AI Analysis': 'Blockchain',
    'AI DEX Analysis': 'Blockchain',
    'On-Chain Peak Prediction': 'Blockchain',
    'Understanding Blockchain': 'Blockchain',
    
    # 라이프스타일/생산성
    'Stress Management': 'Lifestyle',
    'Habit Formation': 'Lifestyle',
    'Remote Work Tips': 'Lifestyle',
    'Mastering Notion Template Utilization': 'Productivity',
    
    # 금융
    'Financial Planning': 'Finance',
    'Real Estate Investment': 'Finance',
    'Startup Funding': 'Finance',
    
    # 기타
    'Turning Your Side Project into a Full-Time Career': 'Career',
    'Core Principles of Mobile UI/UX Design': 'Design',
    'Key Principles of Mobile UI/UX Design': 'Design',
    'The Best Time to Start Coding Education for Your Children': 'Education',
    'How to Double Your Algorithm Study Efficiency': 'Learning',
    'How to Build a 10,000 Subscriber List with AI Newsletters': 'Marketing',
    'Increasing Your Followers by 10x with Social Media Strategy': 'Marketing',
    'Your Ultimate Guide to the Developer Roadmap': 'Development',
    'Mastering Refactoring Techniques': 'Development',
}

def consolidate_tags(tags):
    """태그 리스트를 통합된 태그로 변환"""
    consolidated = []
    for tag in tags:
        tag_str = str(tag).strip()
        # 고정 태그는 그대로 유지
        if tag_str in ['AI', 'Automation']:
            consolidated.append(tag_str)
        # 통합 매핑에 있으면 통합된 태그로 변경
        elif tag_str in TAG_CONSOLIDATION:
            new_tag = TAG_CONSOLIDATION[tag_str]
            if new_tag not in consolidated:
                consolidated.append(new_tag)
        # 매핑에 없으면 그대로 유지 (새로운 태그)
        else:
            if tag_str not in consolidated:
                consolidated.append(tag_str)
    return consolidated

def consolidate_english_post(file_path):
    """영어 포스트의 태그 통합"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        original_tags = post.metadata.get('tags', [])
        consolidated_tags = consolidate_tags(original_tags)
        
        # 변경사항이 있으면 저장
        if original_tags != consolidated_tags:
            post.metadata['tags'] = consolidated_tags
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))
            return True, original_tags, consolidated_tags
        return False, original_tags, consolidated_tags
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False, [], []

def main():
    """메인 함수"""
    post_dir = Path("content/post")
    en_files = list(post_dir.glob("*.en.md"))
    
    print(f"📚 총 {len(en_files)}개의 영어 포스트 파일 발견\n")
    
    modified_count = 0
    tag_changes = []
    
    for file_path in sorted(en_files):
        modified, original, consolidated = consolidate_english_post(file_path)
        if modified:
            modified_count += 1
            tag_changes.append({
                'file': file_path.name,
                'original': original,
                'consolidated': consolidated
            })
            print(f"✅ {file_path.name}")
            print(f"   이전: {original}")
            print(f"   이후: {consolidated}\n")
    
    print(f"\n✨ 완료! {modified_count}개 파일의 태그 통합됨")
    
    # 통합 후 태그 통계
    all_consolidated_tags = []
    for change in tag_changes:
        all_consolidated_tags.extend(change['consolidated'])
    
    tag_counts = Counter(all_consolidated_tags)
    print(f"\n📊 통합 후 태그 분포:")
    for tag, count in tag_counts.most_common():
        print(f"  {tag}: {count}회")

if __name__ == "__main__":
    main()
