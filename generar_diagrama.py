import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

capas = [
    ("Input\n8x8x1", "#e8eaf6"),
    ("Conv2D\n32 filtros 3x3\nReLU", "#c5cae9"),
    ("MaxPooling2D\n2x2", "#9fa8da"),
    ("Dropout\n0.3", "#ffe0b2"),
    ("Flatten", "#c5cae9"),
    ("Dense\n64 neuronas\nReLU", "#9fa8da"),
    ("Dropout\n0.3", "#ffe0b2"),
    ("Dense\n10 neuronas\nSoftmax", "#a5d6a7"),
]

fig, ax = plt.subplots(figsize=(14, 3.2))
n = len(capas)
box_w, box_h, gap = 1.5, 1.1, 0.55
total_w = n * box_w + (n - 1) * gap
x = -total_w / 2

centers = []
for i, (texto, color) in enumerate(capas):
    box = FancyBboxPatch((x, -box_h / 2), box_w, box_h,
                          boxstyle="round,pad=0.04,rounding_size=0.08",
                          linewidth=1.3, edgecolor="#37474f", facecolor=color)
    ax.add_patch(box)
    ax.text(x + box_w / 2, 0, texto, ha="center", va="center", fontsize=9.5, fontweight="bold", color="#212121")
    centers.append(x + box_w / 2)
    x += box_w + gap

for i in range(n - 1):
    start = centers[i] + box_w / 2
    end = centers[i + 1] - box_w / 2
    arrow = FancyArrowPatch((start, 0), (end, 0), arrowstyle="-|>", mutation_scale=14,
                             linewidth=1.3, color="#37474f")
    ax.add_patch(arrow)

ax.set_xlim(-total_w / 2 - 0.6, total_w / 2 + 0.6)
ax.set_ylim(-1.3, 1.3)
ax.axis("off")
ax.set_title("Arquitectura del modelo optimizado (CNN)", fontsize=12, fontweight="bold", pad=14)
plt.tight_layout()
plt.savefig("img/diagrama_arquitectura.png", dpi=150, bbox_inches="tight")
print("guardado img/diagrama_arquitectura.png")
