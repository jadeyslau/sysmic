rng(1);
mat = adj_matrix_sym(100);
degree_in = sum(mat);
histogram(degree_in);
avg_deg = mean(degree_in);

[acc, c] = avgClusteringCoefficient(mat)
histogram(c)