x = [1, 3, 5, 7, 9, 11, 13];
ysponge81 = [8.88536e+07, 1.43075e+08, 1.50897e+08, 1.50781e+08, 1.49965e+08, 1.4936e+08, 1.48981e+08];
ysponge27 = [0.316576, 0.401247, 0.44604, 0.480961, 0.511415, 0.538523, 0.560387];
ysponge19 = [0.455477, 0.55728, 0.619774, 0.66171, 0.693402];
ysponge11 = [0.792301, 0.996414, 1.09567];

% ycb81 = [1.84506e+08, 
ycb27 = [42.0444, 41.3739, 41.4596, 41.5174, 41.5561, 41.5854, 41.6156];
ycb19 = [0.786222, 0.803607, 0.821298, 0.835003, 0.859145];
ycb11 = [2.90335, 2.87926, 2.91387];

linew = 1.5;
cvalr = 1;
cvalg = 0.8;
cvalb = 1;
mfcvalr = 0.7;
mfcvalg = 0.5;
mfcvalb = 0.7;

start1 = 1;

semilogy(x(start1:3), ysponge11(start1:end), '-o', 'LineWidth', linew, 'color', [cvalr 0.0 0.0], 'markerfacecolor', [mfcvalr 0.0 0.0]);
hold on;
semilogy(x(start1:5), ysponge19(start1:end), '-o', 'LineWidth', linew, 'color', [0.0 0.0 cvalb], 'markerfacecolor', [0.0 0.0 mfcvalb]);
hold on;
semilogy(x(start1:end), ysponge27(start1:end), '-o', 'LineWidth', linew, 'color', [0.0 cvalg 0.0], 'markerfacecolor', [0.0 mfcvalg 0.0]);
hold on;
semilogy(x(start1:end), ysponge81(start1:end), '-o', 'LineWidth', linew, 'color', [0.0 cvalg 0.0], 'markerfacecolor', [0.0 mfcvalg 0.0]);
hold on;
semilogy(x(start1:3), ycb11(start1:end), '-s', 'LineWidth', linew, 'color', [cvalr 0.0 0.0], 'markerfacecolor', [mfcvalr 0.0 0.0]);
hold on;
semilogy(x(start1:5), ycb19(start1:end), '-s', 'LineWidth', linew, 'color', [0.0 0.0 cvalb], 'markerfacecolor', [0.0 0.0 mfcvalb]);
hold on;
semilogy(x(start1:end), ycb27(start1:end), '-s', 'LineWidth', linew, 'color', [0.0 cvalg 0.0], 'markerfacecolor', [0.0 mfcvalg 0.0]);

xlabel('Number of defects');
ylabel('Relative error $\norm{\nabla(u_h - \overline{u}_h)}_{L^2(\Omega)} / \norm{\nabla u_h}_{L^2(\Omega)}$');
title('Relative error \textsc{vs} Number of defects (\textsc{fem} mesh size $243 \times 243$ and $f \equiv 1$)');
grid on;


legend('$11$ sponge pattern',
       '$19$',
       '$27$',
       '$81$',
       '$11$ checkerboard',
       '$19$',
       '$27$',
       'location', 'southeast', % southeastoutside
       'NumColumns', 2,
       'Color', 'none'
);

% set(gca, 'YScale', 'log'); 

% set x-axis ticks to match the x data
xticks(x);

print("relative_energy_errors_vs_numdefects.png", "-dpng", "-r300");
print("relative_energy_errors_vs_numdefects.tex", "-dtex");
