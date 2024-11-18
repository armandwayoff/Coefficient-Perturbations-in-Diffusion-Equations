clear all;

% stiffoffline0 : perfect coeff (A_0)

defectscounter = 3;  % But there are defectscounter+1 stiffness matrices (A_0, A_1, ..., A_defectscounter)

filename = '../data/stiffoffline0.txt';
fileID = fopen(filename, 'r');
N = fscanf(fileID, '%d', 1);
data = fscanf(fileID, '%f');
fclose(fileID);
stiffoffline0 = reshape(data, N, N)';

stiffoffline = cell(1, defectscounter+1);
stiffoffline{1} = stiffoffline0;

Atilde = zeros(N, N);

for k = 2:defectscounter+1
    filename = ['../data/stiffoffline' num2str(k-1) '.txt'];
    fileID = fopen(filename, 'r');
    N = fscanf(fileID, '%d', 1);
    data = fscanf(fileID, '%f');
    fclose(fileID);
    stiffoffline{k} = reshape(data, N, N)';
    % stiffofflinek = reshape(data, N, N)';
    Atilde = Atilde + stiffoffline{k}^-1;
end 

alphas = ones(1, defectscounter+1);
alphas(1) = 1-defectscounter;  % alpha_0
delta = 0;
for i = 1:defectscounter+1
  for j = 1:defectscounter+1
    temp = sqrt(abs(alphas(i)*alphas(j))) * norm((stiffoffline{i} - stiffoffline{j}) * stiffoffline{j}^-1);
    if temp > delta
      delta = temp;
    endif
  end
end

delta
Atilde = Atilde + (1 - defectscounter) * stiffoffline0^-1;
error = norm(stiffoffline0*Atilde - eye(N))