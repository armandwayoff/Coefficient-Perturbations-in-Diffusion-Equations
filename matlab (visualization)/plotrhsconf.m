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
acoeffp=ffreaddata('../data/perturbed_coeff.txt');
f1=ffreaddata('../data/rhs1.txt');  
f2=ffreaddata('../data/rhs2.txt');   
f3=ffreaddata('../data/rhs3.txt');   
 
c = gray;
c = flipud(c);

figure('Resize','on','ToolBar','none','MenuBar','none','Position',[0 0 1800 430]);

subplot(1,4,1);

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
    

subplot(1,4,2);

ffpdeplot(pcb,bcb,tcb, ...^
          'VhSeq',vhcb, ...
          'XYData',f1, ...
          % 'ZStyle','continuous', ...
          'Mesh','off', ...
          % 'CBTitle', '', ...
          'ColorMap', c,...
          'CBPosition', 'southoutside',...
          'Title','\textsc{rhs} exactly in the defect block');
grid;
axis on;
box on; 
set(gca, 'LineWidth', 2, 'xtick', [], 'ytick', []);
    

subplot(1,4,3);

ffpdeplot(pcb,bcb,tcb, ...^
          'VhSeq',vhcb, ...
          'XYData',f2, ...
          % 'ZStyle','continuous', ...
          'Mesh','off', ...
          % 'CBTitle', '', ...
          'ColorMap', c,...
          'CBPosition', 'southoutside',...
          'Title', '\textsc{rhs} far away from the defect block'); 
grid;
axis on;
box on; 
set(gca, 'LineWidth', 2, 'xtick', [], 'ytick', []);

subplot(1,4,4);

ffpdeplot(pcb,bcb,tcb, ...^
          'VhSeq',vhcb, ...
          'XYData',f3, ...
          % 'ZStyle','continuous', ...
          'Mesh','off', ...
          % 'CBTitle', '', ...
          'ColorMap', c,...
          'CBPosition', 'southoutside',...
          'Title', 'Global \textsc{rhs}');
grid;
axis on;
box on; 
set(gca, 'LineWidth', 2, 'xtick', [], 'ytick', []);

print("rhsconf.png", "-dpng", "-r300");
print("rhsconf.tex", "-dtex");