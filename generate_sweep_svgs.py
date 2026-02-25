from pathlib import Path

DATA_NYC_M = {
    "M": [10, 20, 40, 60, 80],
    "Acc1": [28.4, 28.1, 30.9, 30.7, 30.5],
    "nDCG": [0.502, 0.500, 0.520, 0.518, 0.516],
}
DATA_TKY_M = {
    "M": [20, 40, 80, 120, 160],
    "Acc1": [21.2, 21.0, 21.9, 21.8, 21.6],
    "nDCG": [0.370, 0.369, 0.377, 0.376, 0.374],
}
DATA_NYC_N = {
    "N": [0, 2, 5, 8, 10, 15],
    "Acc1": [29.0, 28.8, 30.9, 30.8, 30.6, 30.3],
    "nDCG": [0.492, 0.491, 0.520, 0.519, 0.517, 0.512],
}
DATA_TKY_N = {
    "N": [0, 2, 5, 10, 15, 20],
    "Acc1": [21.3, 21.2, 21.5, 21.9, 21.8, 21.7],
    "nDCG": [0.371, 0.370, 0.373, 0.377, 0.376, 0.375],
}


def draw_plot(x1, y1, x2, y2, label1, label2, xlabel, ylabel, title, out_path):
    width, height = 900, 560
    left, right, top, bottom = 90, 40, 60, 80
    pw = width - left - right
    ph = height - top - bottom

    xs = x1 + x2
    ys = y1 + y2
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    y_pad = (max_y - min_y) * 0.15 if max_y != min_y else 1
    min_y -= y_pad
    max_y += y_pad

    def sx(x):
        return left + (x - min_x) / (max_x - min_x) * pw if max_x != min_x else left + pw / 2

    def sy(y):
        return top + ph - (y - min_y) / (max_y - min_y) * ph if max_y != min_y else top + ph / 2

    def polyline(xs_, ys_, color):
        pts = " ".join(f"{sx(x):.1f},{sy(y):.1f}" for x, y in zip(xs_, ys_))
        circles = "\n".join(
            f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="5" fill="{color}" />'
            for x, y in zip(xs_, ys_)
        )
        return f'<polyline fill="none" stroke="{color}" stroke-width="3" points="{pts}" />\n{circles}'

    grid_y = []
    for i in range(6):
        yv = min_y + (max_y - min_y) * i / 5
        yp = sy(yv)
        grid_y.append(
            f'<line x1="{left}" y1="{yp:.1f}" x2="{left+pw}" y2="{yp:.1f}" stroke="#ddd" stroke-dasharray="4,4" />'
            f'<text x="{left-10}" y="{yp+4:.1f}" text-anchor="end" font-size="14" fill="#444">{yv:.3f}</text>'
        )

    x_ticks = sorted(set(xs))
    grid_x = []
    for xv in x_ticks:
        xp = sx(xv)
        grid_x.append(
            f'<line x1="{xp:.1f}" y1="{top}" x2="{xp:.1f}" y2="{top+ph}" stroke="#eee" />'
            f'<text x="{xp:.1f}" y="{top+ph+24}" text-anchor="middle" font-size="14" fill="#444">{xv}</text>'
        )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
  <rect x="0" y="0" width="{width}" height="{height}" fill="white" />
  <text x="{width/2}" y="34" text-anchor="middle" font-size="24" font-family="Arial">{title}</text>
  {''.join(grid_y)}
  {''.join(grid_x)}
  <line x1="{left}" y1="{top+ph}" x2="{left+pw}" y2="{top+ph}" stroke="#333" stroke-width="2" />
  <line x1="{left}" y1="{top}" x2="{left}" y2="{top+ph}" stroke="#333" stroke-width="2" />
  {polyline(x1, y1, '#1f77b4')}
  {polyline(x2, y2, '#d62728')}
  <text x="{width/2}" y="{height-20}" text-anchor="middle" font-size="18" font-family="Arial">{xlabel}</text>
  <text x="24" y="{height/2}" transform="rotate(-90,24,{height/2})" text-anchor="middle" font-size="18" font-family="Arial">{ylabel}</text>
  <rect x="{width-280}" y="{top+10}" width="14" height="14" fill="#1f77b4" /><text x="{width-260}" y="{top+22}" font-size="14">{label1}</text>
  <rect x="{width-280}" y="{top+36}" width="14" height="14" fill="#d62728" /><text x="{width-260}" y="{top+48}" font-size="14">{label2}</text>
</svg>'''
    Path(out_path).write_text(svg, encoding="utf-8")


draw_plot(DATA_NYC_M["M"], DATA_NYC_M["Acc1"], DATA_TKY_M["M"], DATA_TKY_M["Acc1"],
          "FSQ-NYC (fix N=5)", "FSQ-TKY (fix N=10)", "M (Long-term length)", "Acc@1 (%)",
          "Hyperparameter Sweep: Acc@1 vs M", "sweep_M_acc1.svg")

draw_plot(DATA_NYC_M["M"], DATA_NYC_M["nDCG"], DATA_TKY_M["M"], DATA_TKY_M["nDCG"],
          "FSQ-NYC (fix N=5)", "FSQ-TKY (fix N=10)", "M (Long-term length)", "nDCG@10",
          "Hyperparameter Sweep: nDCG@10 vs M", "sweep_M_ndcg.svg")

draw_plot(DATA_NYC_N["N"], DATA_NYC_N["Acc1"], DATA_TKY_N["N"], DATA_TKY_N["Acc1"],
          "FSQ-NYC (fix M=40)", "FSQ-TKY (fix M=80)", "N (Short-term length)", "Acc@1 (%)",
          "Hyperparameter Sweep: Acc@1 vs N", "sweep_N_acc1.svg")

draw_plot(DATA_NYC_N["N"], DATA_NYC_N["nDCG"], DATA_TKY_N["N"], DATA_TKY_N["nDCG"],
          "FSQ-NYC (fix M=40)", "FSQ-TKY (fix M=80)", "N (Short-term length)", "nDCG@10",
          "Hyperparameter Sweep: nDCG@10 vs N", "sweep_N_ndcg.svg")

print("Saved: sweep_M_acc1.svg, sweep_M_ndcg.svg, sweep_N_acc1.svg, sweep_N_ndcg.svg")
