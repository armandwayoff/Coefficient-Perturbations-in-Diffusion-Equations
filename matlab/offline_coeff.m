clear all;
%Add  to the search path
addpath('../ffmatlib');
%Load the mesh
[p,b,t,nv,nbe,nt,labels]=ffreadmesh('../data/meshTh.msh');
[pcb,bcb,tcb,nvcb,nbecb,ntcb,labelscb]=ffreadmesh('../data/meshThcb.msh');

%Load the finite element space connectivity
vhcb=ffreaddata('../data/mesh_vhcb.txt');
%Load scalar data
acoeff=ffreaddata('../data/perfect_coeff.txt');
acoeffp=ffreaddata('../data/perturbed_coeff.txt');

defectscounter = 3;

offlincoeff = cell(0, defectscounter-1);
for k = 1:defectscounter
    offlincoeff{k} = ffreaddata(['../data/offlincoeff' num2str(k) '.txt']); 
end

c = gray;
c = flipud(c);

figure('Resize','on','ToolBar','none','MenuBar','none','Position',[0 0 1800 430]);

subplot(1,defectscounter+2,1);

ffpdeplot(pcb,bcb,tcb, ...^
          'VhSeq',vhcb, ...
          'XYData',acoeffp, ...
          % 'ZStyle','continuous', ...
          'Mesh','off', ...
          % 'CBTitle', '', ...
          'ColorMap', c, ...
          'CBPosition', 'southoutside',...
          'Title','Randomly perturbed coefficient');
grid;
axis on;
box on; 
set(gca, 'LineWidth', 2, 'xtick', [], 'ytick', []);

subplot(1,defectscounter+2,2);

ffpdeplot(pcb,bcb,tcb, ...^
          'VhSeq',vhcb, ...
          'XYData',acoeff, ...
          % 'ZStyle','continuous', ...
          'Mesh','off', ...
          % 'CBTitle', '', ...
          'ColorMap', c, ...
          'CBPosition', 'southoutside',...
          'Title','A_0');
grid;
axis on;
box on; 
set(gca, 'LineWidth', 2, 'xtick', [], 'ytick', []);
    
for k = 1:defectscounter
  subplot(1,defectscounter+2,k+2);

  ffpdeplot(pcb,bcb,tcb, ...^
            'VhSeq',vhcb, ...
            'XYData', offlincoeff{k}, ...
            % 'ZStyle','continuous', ...
            'Mesh','off', ...
            % 'CBTitle', '', ...
            'ColorMap', c,...
            'CBPosition', 'southoutside',...
            'Title', ['A_' num2str(k)]); % ['Offline coefficient n°' num2str(k)]);
  grid;
  axis on;
  box on; 
  set(gca, 'LineWidth', 2, 'xtick', [], 'ytick', []);
end

print("offline_coeff.png", "-dpng", "-r300");