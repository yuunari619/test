#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ドル円為替レート推移PowerPoint資料作成スクリプト
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# プレゼンテーション作成
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

# 空白レイアウトを使用
blank_slide_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_slide_layout)

# タイトルを追加
title_box = slide.shapes.add_textbox(
    Inches(0.5), Inches(0.3), Inches(9), Inches(0.8)
)
title_frame = title_box.text_frame
title_frame.text = "ドル円為替レート推移分析"
title_para = title_frame.paragraphs[0]
title_para.font.size = Pt(36)
title_para.font.bold = True
title_para.font.color.rgb = RGBColor(0, 51, 102)  # 濃紺
title_para.alignment = PP_ALIGN.CENTER

# サブタイトル（期間）を追加
subtitle_box = slide.shapes.add_textbox(
    Inches(0.5), Inches(1.0), Inches(9), Inches(0.4)
)
subtitle_frame = subtitle_box.text_frame
subtitle_frame.text = "2025年12月16日 〜 2026年1月16日"
subtitle_para = subtitle_frame.paragraphs[0]
subtitle_para.font.size = Pt(20)
subtitle_para.font.color.rgb = RGBColor(100, 100, 100)
subtitle_para.alignment = PP_ALIGN.CENTER

# メッセージライン（Key Message）を追加
message_box = slide.shapes.add_textbox(
    Inches(0.5), Inches(1.6), Inches(9), Inches(1.2)
)
message_frame = message_box.text_frame
message_frame.word_wrap = True

# メッセージラインのタイトル
p1 = message_frame.paragraphs[0]
p1.text = "Key Message"
p1.font.size = Pt(18)
p1.font.bold = True
p1.font.color.rgb = RGBColor(204, 0, 0)  # 赤
p1.space_after = Pt(10)

# メッセージ1
p2 = message_frame.add_paragraph()
p2.text = "• 円安トレンドが明確に継続：1ヶ月間で154.82円から158.78円へ推移"
p2.font.size = Pt(16)
p2.space_after = Pt(8)
p2.level = 0

# メッセージ2
p3 = message_frame.add_paragraph()
p3.text = "• 変動幅：+3.96円（+2.56%）の円安進行"
p3.font.size = Pt(16)
p3.space_after = Pt(8)
p3.level = 0

# メッセージ3
p4 = message_frame.add_paragraph()
p4.text = "• 2026年1月10日に年間高値158.87円を記録、その後も高水準を維持"
p4.font.size = Pt(16)
p4.level = 0

# グラフ画像を追加
img_path = '/home/user/test/usdjpy_chart_2025-12-16_to_2026-01-16.png'
left = Inches(0.8)
top = Inches(3.0)
width = Inches(8.4)
slide.shapes.add_picture(img_path, left, top, width=width)

# フッターを追加
footer_box = slide.shapes.add_textbox(
    Inches(0.5), Inches(7.0), Inches(9), Inches(0.3)
)
footer_frame = footer_box.text_frame
footer_frame.text = "出典: 市場データに基づく分析"
footer_para = footer_frame.paragraphs[0]
footer_para.font.size = Pt(10)
footer_para.font.color.rgb = RGBColor(128, 128, 128)
footer_para.alignment = PP_ALIGN.RIGHT

# ファイル保存
output_file = '/home/user/test/usdjpy_analysis_presentation.pptx'
prs.save(output_file)
print(f"PowerPoint presentation saved to: {output_file}")
print("\n=== Presentation Details ===")
print("Slide 1:")
print("  - Title: ドル円為替レート推移分析")
print("  - Subtitle: 2025年12月16日 〜 2026年1月16日")
print("  - Key Messages: 3つの主要ポイント")
print("  - Chart: USD/JPY exchange rate graph")
