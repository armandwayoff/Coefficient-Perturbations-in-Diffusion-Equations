x = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250];
y = [0.00022784, 0.000472128, 0.000250893, 0.000379315, 0.000324754, 0.000255675, 0.000317715, 0.000287517, 0.000310661, 0.000294495, 0.000267172, 0.000296384, 0.000285198]; % not relative error for 27x27 sponge and f = 1
ybis = [0.0230146, 0.281377, 0.231378, 0.227339, 0.26503, 0.284774, 0.27355, 0.29213, 0.302388, 0.29986, 0.304648, 0.305247, 0.310365]; % relative error for 27x27 sponge and f = 1
y2 = [0.00558151, 0.00503027, 0.0044505, 0.00393357, 0.00415212, 0.00396442, 0.00409113, 0.00404088, 0.00407525, 0.00404995, 0.00391827, 0.00400231, 0.00393495]; % not relative error for 7x7 sponge and f = 1
y2bis = [0.27122, 0.434772, 0.433128, 0.477986, 0.501848, 0.475854, 0.494389, 0.503589, 0.492427, 0.49749, 0.504056, 0.495293, 0.503821]; % relative error for 9x9 sponge and f = 1
y3 = [0, 2.34867e-05, 3.37216e-05, 7.26793e-05, 8.53506e-05, 8.25075e-05, 0.000101249, 0.000101065, 0.000111878, 0.000106069, 9.84612e-05, 0.000106946, 0.000105389]; % not relative error for 81x81 sponge and f = 1
y3bis = [0, 0.00531666, 0.0157585, 0.0196188, 0.0303994, 0.0336577, 0.0298715, 0.0408917, 0.0395577, 0.0380809, 0.0447343, 0.0416592, 0.04242]; % relative error for 81x81 sponge and f = 1

cb9non = [0.00249549, 0.00271956, 0.00297835, 0.00308233, 0.00368105, 0.00360019, 0.00355019, 0.00344447, 0.00340327, 0.00345949, 0.00341169, 0.00338502, 0.00332512]; % not relative error for 9x9 checkerboard and f = 1
cb9 = [0.415329, 0.750469, 0.87785, 1.00979, 1.0737, 1.1639, 1.2292, 1.25697, 1.23877, 1.28927, 1.31512, 1.34124, 1.36653]; % relative error for 9x9 checkerboard and f = 1
cb27non = [7.04205e-05, 0.000277071, 0.00034998, 0.000287651, 0.000302144, 0.00042841, 0.000348128, 0.000330848, 0.000399858, 0.0003663, 0.000342329, 0.000392149, 0.000371183]; % not relative error for 27x27 checkerboard and f = 1
cb27 = [0.0120566, 0.139115, 0.201116, 0.220587, 0.249547, 0.277107, 0.277892, 0.292211, 0.326669, 0.32111, 0.334481, 0.348388, 0.357193]; % relative error for 27x27 checkerboard and f = 1
cb81non = [0, 7.82584e-06, 8.66934e-06, 1.20337e-05, 3.0787e-05, 2.49516e-05, 3.23982e-05, 3.89175e-05, 4.367e-05, 3.64198e-05, 3.1963e-05, 3.08995e-05, 3.75521e-05]; % not relative error for 81x81 checkerboard and f = 1
cb81 = [0, 0.00403049, 0.00686261, 0.0129805, 0.0463577, 0.0426124, 0.0632339, 0.0670862, 0.0732636, 0.0785074, 0.0735189, 0.0751279, 0.086052]; % relative error for 81x81 checkerboard and f = 1

#{
plot(x, y, '-o', 'LineWidth', 2, 'color', 'blue');
hold on;
plot(x, y2, '-o', 'LineWidth', 2, 'color', 'red');
hold on;
plot(x, y3, '-o', 'LineWidth', 2, 'color', 'green');
hold on;
#}

linew = 1.5;
cvalr = 1;
cvalg = 0.8;
cvalb = 1;
mfcvalr = 0.7;
mfcvalg = 0.5;
mfcvalb = 0.7;

start1 = 3;
start2 = 4;
start3 = 6;

semilogy(x(start1:end), y2bis(start1:end), '-o', 'LineWidth', linew, 'color', [cvalr 0.0 0.0], 'markerfacecolor', [mfcvalr 0.0 0.0]);
hold on;
semilogy(x(start2:end), ybis(start2:end), '-o', 'LineWidth', linew, 'color', [0.0 0.0 cvalb], 'markerfacecolor', [0.0 0.0 mfcvalb]);
hold on;
semilogy(x(start3:end), y3bis(start3:end), '-o', 'LineWidth', linew, 'color', [0.0 cvalg 0.0], 'markerfacecolor', [0.0 mfcvalg 0.0]);
hold on;
semilogy(x(start1:end), cb9(start1:end), '-s', 'LineWidth', linew, 'color', [cvalr 0.0 0.0], 'markerfacecolor', [mfcvalr 0.0 0.0]);
hold on;
semilogy(x(start2:end), cb27(start2:end), '-s', 'LineWidth', linew, 'color', [0.0 0.0 cvalb], 'markerfacecolor', [0.0 0.0 mfcvalb]);
hold on;
semilogy(x(start3:end), cb81(start3:end), '-s', 'LineWidth', linew, 'color', [0.0 cvalg 0.0], 'markerfacecolor', [0.0 mfcvalg 0.0]);

% xlabel('Number of defects');
xlabel('\textsc{fem} mesh size');
ylabel('Relative error $\norm{\nabla(u_h - \overline{u}_h)}_{L^2(\Omega)} / \norm{\nabla u_h}_{L^2(\Omega)}$');
% title('\textbf{Relative error \textsc{vs} \textsc{fem} mesh size ($1$ defect and $f \equiv 1$)}');
grid on;

lgd = legend(% 'not relative error for 27x27 sponge and f = 1', 
       % 'not relative error for 7x7 sponge and f = 1',
       % 'not relative error for 81x81 sponge and f = 1',
       '$9$',
       '$27$',
       'Sponge : $81$',
       '$9$',
       '$27$',
       'Checkerboard : $81$',
       'location', 'north', % southeastoutside
       'NumColumns', 3,      % , 'Color', 'none'
       "orientation", "horizontal"
);
legend left
% title(lgd,['Sponge pattern' 'Checkerboard']);

% set(gca, 'YScale', 'log'); 

% set x-axis ticks to match the x data
xticks(x);

% print("relative_energy_errors_vs_femsize.png", "-dpng", "-r300");
print("relative_energy_errors_vs_femsize.tex", "-dtex");
