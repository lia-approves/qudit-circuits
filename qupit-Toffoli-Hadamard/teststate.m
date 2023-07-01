%%% Prints out truth table of a multi-qudit state.
function teststate(state, emu, showZeroes)
    global d;
    numChanged = 0;
    if nargin < 3
        showZeroes = false;
    end
    dimstate = numel(state);
    n = round(log(dimstate)/log(d));
    if nargin < 2
        emu = false;
    end
    fstate = find(abs(state) > 1e-10);
    state = state/abs(state(fstate(1)));
    I = eye(d);
    ks = cellfun(@(x) I(:,x),num2cell([1:d]),'UniformOutput',false);
    vals = zeros(1,dimstate);

    for i = 0 : (dimstate-1)
        dits = dec2base(i,d);
        if length(dits) < n
            dits = [repmat('0',round([1 n-length(dits)])) dits];
        end
        ditvecs = cellfun(@(x) ks{base2dec(dits(x),d)+1}, num2cell(1:n), 'UniformOutput', false);
        vals(i+1) = dot(state, tensall(ditvecs));
        if abs(vals(i+1))>1e-10 || showZeroes
            disp([dits dispcomplex(vals(i+1))]);
            if vals(i+1)~=0
                numChanged = numChanged + 1;
            end
        end
    end
end