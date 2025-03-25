c = [-1, 0]
A_ub = [[-2, 0], [1, -1]]  # 2p1 ≥ v, -1p1 + 1p2 ≥ v
b_ub = [-1, -1]
res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(0, None)]*2)
v = 1 / res.x.sum()
print(f"Стратегия: {np.round(res.x * v, 2)}")  # [0.5, 0.5]