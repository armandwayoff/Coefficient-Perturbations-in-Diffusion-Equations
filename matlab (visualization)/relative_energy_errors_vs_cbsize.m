x = [9, 15, 21, 25, 31, 37, 41, 53, 63, 73, 81];

y2 = [0.96955, 0.569886, 0.403971, 0.336314, 0.257441, 0.219014, 0.195993, 0.145214, 0.11383, 0.102295, 0.0907943];  % sponge pattern f exactly in the defect block
y3 = [4.76016e+08, 0.602729, 2.46625, 0.830233, 0.258869, 0.225821, 0.320712, 0.110813, 0.109032, 0.412448, 8.88536e+07]; % sponge pattern f=1
y4 = [0.481949, 0.28411, 0.20221, 0.16354, 0.123732, 0.101429, 0.093669, 0.0651953, 0.0510991, 0.0476644, 0.0488627]; % sponge pattern f far away from the defect block
y5 = [0.322697, 0.190411, 0.132675, 0.11221, 0.0885265, 0.0734998, 0.0669462, 0.0482137, 0.0382324, 0.0350658, 0.0298518]; % checkerboard pattern f far away from the defect block
y6 = [0.99866, 0.591164, 0.408771, 0.346439, 0.264211, 0.220872, 0.19985, 0.149747, 0.109593, 0.0980356, 0.0899418]; % checkerboard pattern f exactly in the defect block
y7 = [3.0017, 1.18449, 1.6402, 0.595692, 0.375667, 1.81017, 0.365562, 0.192765, 0.179254, 0.141179, 0.118998]; % checkerboard pattern f=1

linew = 1.5;

semilogy(x, y2, '-o', 'LineWidth', linew, 'color', 'blue');
hold on;
semilogy(x, y4, '-o', 'LineWidth', linew, 'color', 'red');
hold on;
semilogy(x, y3, '-o', 'LineWidth', linew, 'color', 'green');
hold on;
semilogy(x, y6, '-x', 'LineWidth', linew, 'color', 'blue');  
hold on;
semilogy(x, y5, '-x', 'LineWidth', linew, 'color', 'red'); 
hold on;
semilogy(x, y7, '-x', 'LineWidth', linew, 'color', 'green');

xlabel('Pattern size');
ylabel('Relative energy errors');
title('Relative energy errors VS  size (1 defect, FEM mesh size : $243 \times 243$)');

grid on;

legend('S, $f$ exactly in the defect block', 
       'S, $f$ far away from the defect block', 
       'S, $f \equiv 1$', 
       'CB, $f$ exactly in the defect block',
       'CB, $f$ far away from the defect block',
       'CB, $f \equiv 1$',
       'location', 'northeast', % north
       'NumColumns', 1,
       'Color', 'none'
);

% set(gca, 'YScale', 'log'); 

% set x-axis ticks to match the x data
xticks(x);

% print("relative_energy_errors_vs_cbsize.png", "-dpng", "-r300");
print("relative_energy_errors_vs_cbsize.tex", "-dtex");
