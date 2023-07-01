%%% Prints out truth table of a unitary U.
function [outstrs, vals, numChanged] = testU(u, emu, showIds, showZeroes)
    global d;
    numChanged = 0;
    if nargin < 3
        showIds = false;
    end
    if nargin < 4
        showZeroes = false;
    end
    dimU = size(u);
    n = round(log(dimU(1))/log(d));
    if nargin < 2
        emu = false;
    end
    fu = find(abs(u) > 1e-10);
    u = u/abs(u(fu(1)));
    I = eye(d);
    ks = cellfun(@(x) I(:,x),num2cell([1:d]),'UniformOutput',false);
    outstrs = cell(1,dimU(1));
    vals = zeros(1,dimU(1));
    
    for i = 0 : (dimU(1)-1)
        dits = dec2base(i,d);
        if length(dits) < n
            dits = [repmat('0',[1 n-length(dits)]) dits];
        end
        ditvecs = cellfun(@(x) ks{base2dec(dits(x),d)+1}, num2cell(1:n), 'UniformOutput',false);
        uk = u * tensall(ditvecs);
        outstrs{i+1} = dec2base(find(round(abs(uk))>1e-10)-1,d,n);
        vals(i+1) = uk(find(round(abs(uk))));
        if (vals(i+1)~=0 || showZeroes) && (find(round(abs(uk)))-1 ~= i || abs(vals(i+1)-1) > 1e-10 || showIds)
            disp([dits ' --> ' outstrs{i+1} dispcomplex(vals(i+1))]);
            if vals(i+1)~=0 || find(round(abs(uk)))-1 ~= i || abs(vals(i+1)-1) > 1e-10
                numChanged = numChanged + 1;
            end
        end
    end
end