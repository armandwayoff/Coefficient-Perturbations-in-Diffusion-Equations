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

f1=ffreaddata('../data/rhs1.txt');  
f2=ffreaddata('../data/rhs2.txt');   
f3=ffreaddata('../data/rhs3.txt');  

defectscounter = 3;

offlincoeff = cell(0, defectscounter-1);
for k = 1:defectscounter
    offlincoeff{k} = ffreaddata(['../data/offlincoeff' num2str(k) '.txt']); 
end

c = gray;
c = flipud(c);

figure('Resize','on','ToolBar','none','MenuBar','none','Position',[0 0 430 430]);

ffpdeplotbis(pcb,bcb,tcb, ...^ % ffpdeplotbis
          'VhSeq',acoeffp, ...
          % 'XYData', uh, ...
          % 'ZStyle','continuous', ...
          'Mesh','off', ...
          % 'CBTitle', '', ...
          'ColorMap', 'jet', ...
          'CBPosition', '',...
          'Title',''); % Perturbed coefficient');

set(gcf,'Position',[0 0 500 500]); % [0 0 500 500]
set(gca,'units','pixels');
set(gca,'units','normalized','position',[0.025 0.025 0.95 0.95]); % [0.025 0.025 0.95 0.95]
box on; 
set(gca, 'LineWidth', 3, 'xtick', [], 'ytick', []);

print("default_27.png", "-dpng", "-r300"); % crisscross_27_relative_error
print("example_random_coeff_27sponge.tex", "-dtex");  % config_perturbed_coeff

% crisscrossmesh_27