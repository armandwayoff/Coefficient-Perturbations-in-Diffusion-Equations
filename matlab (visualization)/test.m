% t=tiledlayout(1,1,'Padding','tight');
% nexttile
A = 1;
f = 50;
T = 1/f;
w = 2*pi*f;
x1 = linspace(0,T,1000)';
y1 = A.*sin(w.*x1);
x2 = 1:10;
y2 = rand(10);
f1 = figure(1);
% yyaxis left
p1 = plot(x1,y1);
ylabel('Var 1')
% yyaxis right
p2 = plot(x2,y2,'o');
ylabel('Var 2')
xlabel('X var')
c = colorbar;
c.Label.FontSize = 7;
c.Color = [0 0 0];
c.Ticks = [0:0.2:1];
c.Label.String = 'Density (normalised)';
ax = gca;
ax.FontName = 'Garamond';
ax.FontSize = 7;
set(gcf,'units','centimeters','position',[10 10 6.93 6.93/2])
annotation('rectangle','Position',[0 0 1 1],'LineWidth',2) % for highlighting the figure boundary