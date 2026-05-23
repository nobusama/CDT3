"""
Cleaned mockup figures for CDT NeurIPS appendix (v2).
Fixes: annotation positioning, label collisions, horizontal jitter for clusters.
"""
import matplotlib.pyplot as plt

# ============================================================
# Figure 1a: ML landscape (inductive bias × empirical grounding)
# ============================================================

fig, ax = plt.subplots(figsize=(10, 7))

# (x = empirical grounding, y = inductive bias, name, color, size, label_dx, label_dy)
models_a = [
    # Sequence-only, low IB (bottom-left cluster) — slight jitter to separate
    (0.10, 0.08, "Evo (Arc)",         "#999999", 200,  7,  6),
    (0.20, 0.13, "CD-GPT (Tencent)",  "#999999", 200,  7,  6),
    (0.07, 0.18, "DNABERT-2",         "#999999", 200,  7,  6),
    # Structural priors
    (0.22, 0.55, "AlphaFold",         "#8aa6c8", 200,  7,  6),
    # Protein LMs (sequence DB → protein representations)
    (0.30, 0.10, "ESM-2",             "#c8a888", 200,  7,  6),
    (0.10, 0.42, "ESM-3",             "#c8a888", 200,  7,  6),
    # Sequence-to-function family (observational genomic data, DNA → multi-output)
    (0.32, 0.42, "AlphaGenome",       "#7ac8b8", 200,  7,  6),
    (0.32, 0.32, "Enformer",          "#7ac8b8", 200,  7,  6),
    # Single-cell RNA foundation models (slight horizontal jitter)
    (0.45, 0.30, "scGPT",             "#a8d8a8", 200,  7,  6),
    (0.42, 0.18, "scFoundation",      "#a8d8a8", 200,  7,  6),
    (0.58, 0.22, "UCE",               "#a8d8a8", 200,  7,  6),
    (0.55, 0.32, "Geneformer",        "#a8d8a8", 200,  7,  6),
    # Multi-omics integration (VAE / graph) — observational multi-modal data
    (0.65, 0.42, "totalVI",           "#e8a8a8", 200,  7,  6),
    (0.75, 0.48, "MultiVI",           "#e8a8a8", 200,  7,  6),
    (0.68, 0.50, "GLUE",              "#e8a8a8", 200, -34, -16),
    # Scale-driven perturbation
    (0.82, 0.20, "STATE (Arc)",       "#f0b070", 250,  7,  6),
    (0.92, 0.10, "Tahoe-100M",        "#f0b070", 200, -45, -16),
    # High-IB camp
    (0.50, 0.78, "PerturbedVAE",      "#c8a8d8", 200,  7,  6),
    (0.20, 0.88, "Mechanistic\nODE / BoolNet", "#c8a8d8", 180,  7,  -10),
    # CDT
    (0.88, 0.85, "CDT",               "#c8334d", 500, 14, -4),
]

for x, y, name, color, size, dx, dy in models_a:
    if name == "CDT":
        ax.scatter(x, y, s=size + 250, marker="*", c="#ffd24a",
                   edgecolors="#c8334d", linewidth=2.5, zorder=5)
    ax.scatter(x, y, s=size, c=color,
               edgecolors="black",
               linewidth=2.0 if name == "CDT" else 1.0,
               zorder=4)
    weight = "bold" if name == "CDT" else "normal"
    ax.annotate(name, (x, y), xytext=(dx, dy),
                textcoords="offset points",
                fontsize=10 if name != "CDT" else 12,
                fontweight=weight,
                color="#c8334d" if name == "CDT" else "black")

# CDT corner annotation — moved into empty middle-right space, no title overlap
ax.annotate("CDT alone in this corner:\nhigh inductive bias  +  high empirical grounding\n(CRISPRi + CITE-seq experimental data)",
            xy=(0.86, 0.82), xytext=(0.62, 0.62),
            fontsize=9.5, color="#c8334d", fontweight="bold",
            ha="center",
            bbox=dict(boxstyle="round,pad=0.4", fc="white",
                      ec="#c8334d", lw=1.2, alpha=0.95),
            arrowprops=dict(arrowstyle="->", color="#c8334d", lw=1.5))

# Axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel("Empirical grounding  →\n(de novo / sequence DB     →     CRISPRi perturbation data)",
              fontsize=11)
ax.set_ylabel("Inductive bias  →\n(low / scale-driven     →     high / architecturally-driven)",
              fontsize=11)
ax.set_title("Panel a — ML landscape: inductive bias × empirical grounding",
             fontsize=13, fontweight="bold", pad=12)

# Quadrant guides
ax.axhline(0.5, color="gray", linewidth=0.5, linestyle="--", alpha=0.4)
ax.axvline(0.5, color="gray", linewidth=0.5, linestyle="--", alpha=0.4)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_linewidth(1.2)

# Quadrant hint labels — repositioned away from data
ax.text(0.02, 0.02, "sequence-only,\nscale-driven", fontsize=8.5,
        color="gray", style="italic", alpha=0.7)
ax.text(0.98, 0.02, "scale-driven\nperturbation models", fontsize=8.5,
        color="gray", style="italic", alpha=0.7, ha="right")
ax.text(0.02, 0.98, "mechanistic /\nclassical IB",
        fontsize=8.5, color="gray", style="italic", alpha=0.7, va="top")
ax.text(0.98, 0.98, "★ paradigm reference target",
        fontsize=8.5, color="#c8334d", style="italic", alpha=0.95,
        ha="right", va="top", fontweight="bold")

plt.tight_layout()
plt.savefig("landscape_panel_a_ml.png",
            dpi=160, bbox_inches="tight")
plt.close()

# ============================================================
# Figure 1b: Biology landscape (modality breadth × architectural integration)
# ============================================================

fig, ax = plt.subplots(figsize=(10, 7))

# Spread the 1-modality cluster horizontally (they're all "single" architecture,
# but jitter to avoid label collisions). Group by family for color readability.
models_b = [
    # DNA-only single-modality (gray) — far-left jitter
    (0.04, 0.18, "Evo",            "#999999", 200,  7,  6),
    (0.04, 0.30, "DNABERT-2",      "#999999", 200,  7,  6),
    # Protein-only single (blue)
    (0.04, 0.42, "AlphaFold",      "#8aa6c8", 200,  7,  6),
    # Protein LMs (1 biological modality)
    (0.20, 0.46, "ESM-2",          "#c8a888", 200,  7,  6),
    (0.42, 0.10, "ESM-3 (intra-protein concat)", "#c8a888", 200,  7,  6),
    # Sequence-to-function family (DNA → multi-output predictions, 1 input modality)
    (0.04, 0.06, "Enformer",       "#7ac8b8", 200,  7,  6),
    (0.10, 0.40, "AlphaGenome",    "#7ac8b8", 200,  7,  6),
    # RNA-only single-cell foundation models (green) — slightly right jitter
    (0.14, 0.16, "scFoundation",   "#a8d8a8", 200,  7,  6),
    (0.18, 0.22, "scGPT",          "#a8d8a8", 200,  7,  6),
    (0.14, 0.30, "UCE",            "#a8d8a8", 200,  7,  6),
    (0.18, 0.36, "Geneformer",     "#a8d8a8", 200,  7,  6),
    # Arc perturbation (orange) — slight right of green cluster
    (0.28, 0.20, "STATE (Arc)",    "#f0b070", 250,  7,  6),
    (0.32, 0.14, "Tahoe-100M",     "#f0b070", 200,  7,  6),
    # 2-modality concat (multi-omics integration camp) — within new 2-modality band (0.50-0.78)
    (0.40, 0.58, "totalVI (RNA+Protein)",  "#e8a8a8", 200,  7,  6),
    (0.42, 0.66, "MultiVI (RNA+ATAC)",      "#e8a8a8", 200,  7,  6),
    (0.58, 0.62, "GLUE (RNA+ATAC)",         "#e8a8a8", 200,  7,  6),
    # 3-modality concat (CD-GPT)
    (0.55, 0.85, "CD-GPT\n(DNA+RNA+Protein, concat)", "#c8a8d8", 230,  7, 6),
    # CDT — top-right, alone
    (0.92, 0.88, "CDT",            "#c8334d", 500, 14, -4),
]

for x, y, name, color, size, dx, dy in models_b:
    if name == "CDT":
        ax.scatter(x, y, s=size + 250, marker="*", c="#ffd24a",
                   edgecolors="#c8334d", linewidth=2.5, zorder=5)
    ax.scatter(x, y, s=size, c=color,
               edgecolors="black",
               linewidth=2.0 if name == "CDT" else 1.0,
               zorder=4)
    weight = "bold" if name == "CDT" else "normal"
    ax.annotate(name, (x, y), xytext=(dx, dy),
                textcoords="offset points",
                fontsize=10 if name != "CDT" else 12,
                fontweight=weight,
                color="#c8334d" if name == "CDT" else "black")

# CDT annotation — moved to upper-left empty zone, clear of multi-omics band
ax.annotate("CDT alone in this corner:\n3 experimental modalities (DNA + RNA + Protein)\n+ architectural cascade (VCE-N → VCE-C,\n  reflecting the central dogma)",
            xy=(0.91, 0.88), xytext=(0.28, 0.78),
            fontsize=9.5, color="#c8334d", fontweight="bold", ha="center",
            bbox=dict(boxstyle="round,pad=0.4", fc="white",
                      ec="#c8334d", lw=1.2, alpha=0.95),
            arrowprops=dict(arrowstyle="->", color="#c8334d", lw=1.5,
                            connectionstyle="arc3,rad=-0.10"))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel("Architectural integration  →\n(single modality    →    concatenation    →    architectural cascade)",
              fontsize=11)
ax.set_ylabel("Modality breadth (experimental data)  →\n(1    →    2    →    3 modalities; DNA+RNA+Protein)",
              fontsize=11)
ax.set_title("Panel b — Biology landscape: modality breadth × architectural integration",
             fontsize=13, fontweight="bold", pad=12)

# Tier guidelines for modality count (1-mod: 0-0.50, 2-mod: 0.50-0.78, 3-mod: 0.78-1.0)
for ytick in [0.50, 0.78]:
    ax.axhline(ytick, color="gray", linewidth=0.4, linestyle=":", alpha=0.35)
ax.text(0.985, 0.25, "1 modality", fontsize=9, color="gray",
        style="italic", alpha=0.7, ha="right")
ax.text(0.985, 0.64, "2 modalities", fontsize=9, color="gray",
        style="italic", alpha=0.7, ha="right")
ax.text(0.985, 0.92, "3 modalities", fontsize=9, color="gray",
        style="italic", alpha=0.7, ha="right")

ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_linewidth(1.2)

ax.text(0.02, 0.96, "single-modality\nfoundation models", fontsize=8.5,
        color="gray", style="italic", alpha=0.7, va="top")

plt.tight_layout()
plt.savefig("landscape_panel_b_biology.png",
            dpi=160, bbox_inches="tight")
plt.close()

print("Saved v2:")
print("  landscape_panel_a_ml.png")
print("  landscape_panel_b_biology.png")
