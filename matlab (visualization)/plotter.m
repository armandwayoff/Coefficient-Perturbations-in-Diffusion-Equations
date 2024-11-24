clear all;
%Add  to the search path
addpath('../ffmatlib');
%Load the mesh
[p,b,t,nv,nbe,nt,labels]=ffreadmesh('../data/meshTh.msh');
[pcb,bcb,tcb,nvcb,nbecb,ntcb,labelscb]=ffreadmesh('../data/meshThcb.msh');

%Load the finite element space connectivity
vh=ffreaddata('../data/mesh_vh.txt');
vhcb=ffreaddata('../data/mesh_vhcb.txt');
%Load scalar data
acoeff=ffreaddata('../data/perfect_coeff.txt');
acoeffp=ffreaddata('../data/perturbed_coeff.txt');
uh=ffreaddata('../data/perfect_solution.txt');
uhp=ffreaddata('../data/perturbed_solution.txt');
f=ffreaddata('../data/rhs.txt');   
relative_error=ffreaddata('../data/relative_error.txt');
diff=ffreaddata('../data/diff.txt');

c = gray;
c = flipud(c);

figure('Resize','on','ToolBar','none','MenuBar','none','Position',[0 0 1300 430]);

subplot(1,3,1);

ffpdeplot(pcb,bcb,tcb, ...^
          'VhSeq',vhcb, ...
          'XYData',acoeffp, ...
          % 'ZStyle','continuous', ...
          'Mesh','off', ...
          % 'CBTitle', '', ...
          'ColorMap', c, ...
          'CBPosition', 'southoutside',...
          'Title','Perturbed coefficient');
grid;
axis on;
box on; 
set(gca, 'LineWidth', 2, 'xtick', [], 'ytick', []);
    

subplot(1,3,2);

ffpdeplot(pcb,bcb,tcb, ...^
          'VhSeq',vhcb, ...
          'XYData',f, ...
          % 'ZStyle','continuous', ...
          'Mesh','off', ...
          % 'CBTitle', '', ...
          'ColorMap', c,...
          'CBPosition', 'southoutside',...
          'Title','RHS');
grid;
axis on;
box on; 
set(gca, 'LineWidth', 2, 'xtick', [], 'ytick', []);
    

subplot(1,3,3);

ffpdeplot(p,b,t, ...
          'VhSeq',vh, ...
          'XYData',relative_error, ...
          % 'ZStyle','continuous', ...
          'Mesh','off', ...
          % 'CBTitle', '', ...
          'ColorMap', 'jet',...
          'CBPosition', 'southoutside',...
          'Title', 'Relative energy errors'); % || \nabla(u - u^p) || / || \nabla u||');
grid;
axis on;
box on; 
set(gca, 'LineWidth', 2, 'xtick', [], 'ytick', []);

print("output_image.png", "-dpng", "-r300");