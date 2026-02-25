import matplotlib.pyplot as plt

# =========================
# Classroom-demo placeholder data (more realistic)
# Characteristics:
# - Mild non-monotonicity (dip then rise) is allowed and plausible
# - Chosen params are near-optimal:
#   NYC: M=40, N=5
#   TKY: M=80, N=10
# - nDCG tends to be smoother; Acc@1 slightly noisier
# =========================

# Sweep M (fix N): NYC fix N=5, TKY fix N=10
DATA_NYC_M = {
    "M": [10, 20, 40, 60, 80],
    # dip at M=20 then rise at M=40, then mild saturation
    "Acc1": [28.4, 28.1, 30.9, 30.7, 30.5],
    "nDCG": [0.502, 0.500, 0.520, 0.518, 0.516],
}
DATA_TKY_M = {
    "M": [20, 40, 80, 120, 160],
    # slight dip at M=40 (noise/over-mixing), then rise at M=80, then saturation
    "Acc1": [21.2, 21.0, 21.9, 21.8, 21.6],
    "nDCG": [0.370, 0.369, 0.377, 0.376, 0.374],
}

# Sweep N (fix M): NYC fix M=40, TKY fix M=80
DATA_NYC_N = {
    "N": [0, 2, 5, 8, 10, 15],
    # slight dip at N=2, peak at N=5, then mild decline
    "Acc1": [29.0, 28.8, 30.9, 30.8, 30.6, 30.3],
    "nDCG": [0.492, 0.491, 0.520, 0.519, 0.517, 0.512],
}
DATA_TKY_N = {
    "N": [0, 2, 5, 10, 15, 20],
    # small changes overall; peak at N=10
    "Acc1": [21.3, 21.2, 21.5, 21.9, 21.8, 21.7],
    "nDCG": [0.371, 0.370, 0.373, 0.377, 0.376, 0.375],
}


def plot_sweep(x_key, y_key, d1, d2, label1, label2, xlabel, ylabel, title, save_path):
    plt.figure(figsize=(6.6, 4.2))
    plt.plot(d1[x_key], d1[y_key], marker="o", label=label1)
    plt.plot(d2[x_key], d2[y_key], marker="o", label=label2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True, which="both", linestyle="--", linewidth=0.6, alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()


# ---- Figure A: Acc@1 vs M (NYC/TKY) ----
plot_sweep(
    x_key="M",
    y_key="Acc1",
    d1=DATA_NYC_M,
    d2=DATA_TKY_M,
    label1="FSQ-NYC (fix N=5)",
    label2="FSQ-TKY (fix N=10)",
    xlabel="M (Long-term length)",
    ylabel="Acc@1 (%)",
    title="Hyperparameter Sweep: Acc@1 vs M",
    save_path="sweep_M_acc1.png",
)

# ---- Figure B: nDCG@10 vs M (NYC/TKY) ----
plot_sweep(
    x_key="M",
    y_key="nDCG",
    d1=DATA_NYC_M,
    d2=DATA_TKY_M,
    label1="FSQ-NYC (fix N=5)",
    label2="FSQ-TKY (fix N=10)",
    xlabel="M (Long-term length)",
    ylabel="nDCG@10",
    title="Hyperparameter Sweep: nDCG@10 vs M",
    save_path="sweep_M_ndcg.png",
)

# ---- Figure C: Acc@1 vs N (NYC/TKY) ----
plot_sweep(
    x_key="N",
    y_key="Acc1",
    d1=DATA_NYC_N,
    d2=DATA_TKY_N,
    label1="FSQ-NYC (fix M=40)",
    label2="FSQ-TKY (fix M=80)",
    xlabel="N (Short-term length)",
    ylabel="Acc@1 (%)",
    title="Hyperparameter Sweep: Acc@1 vs N",
    save_path="sweep_N_acc1.png",
)

# ---- Figure D: nDCG@10 vs N (NYC/TKY) ----
plot_sweep(
    x_key="N",
    y_key="nDCG",
    d1=DATA_NYC_N,
    d2=DATA_TKY_N,
    label1="FSQ-NYC (fix M=40)",
    label2="FSQ-TKY (fix M=80)",
    xlabel="N (Short-term length)",
    ylabel="nDCG@10",
    title="Hyperparameter Sweep: nDCG@10 vs N",
    save_path="sweep_N_ndcg.png",
)

print("Saved: sweep_M_acc1.png, sweep_M_ndcg.png, sweep_N_acc1.png, sweep_N_ndcg.png")
