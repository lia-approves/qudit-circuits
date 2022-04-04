%% Implementation of qutrit controlled Clifford+T gates
% accompanying the paper "Constructing all qutrit controlled Clifford+T gates in Clifford+T"
% Lia Yeh and John van de Wetering

%% This code is presently in-progress.  May contain bugs.

%% declare global variables, which are all Clifford
global I II w s h cx x01 x02 x12 swap;

%% identity and zero matrices
I = eye(3);     % single-qutrit identity gate, i.e. 3 x 3 identity matrix
II = eye(3^2);  % two-qutrit identity gate
zero = zeros([3]);  % 3 x 3 zero matrix

%% Z and X basis states
k0 = I(:,1);    % Z-basis states
k1 = I(:,2);    % "
k2 = I(:,3);    % "
w = exp(2*pi*i/3);      % 3rd root of unity
kpl = -i * (k0 + k1 + k2)/sqrt(3);               % X-basis states // Eqs.2-4
kw = -i * (k0 + w * k1 + w^2 * k2)/sqrt(3);      % "
kwsq = -i * (k0 + w^2 * k1 + w * k2)/sqrt(3);    % "

%% qutrit generalization of Pauli gates
x = [0 0 1; 1 0 0; 0 1 0];    % X, i.e. X_{+1} // Def.1
z = [1 0 0; 0 w 0; 0 0 w^2];  % Z, i.e. Z_{+1} // Def.1

%% qutrit S, H, and CX, which generate the Clifford group
zeta = exp(i*2*pi/9);
s = zeta' * [1 0 0; 0 1 0; 0 0 w];  % S // Def.3
h = (kron(kpl, k0') + kron(kw, k1') + kron(kwsq, k2'));   % H // Def.4
cx = [I zero zero; zero x zero; zero zero x'];   % CX, i.e. tau(10 11 12)(20 22 21) // Def.7

%% various other Clifford gates
x01 = [0 1 0; 1 0 0; 0 0 1]; % X permutation gate that permutes |0> and |1>
x02 = [0 0 1; 0 1 0; 1 0 0]; % X permutation gate that permutes |0> and |2>
x12 = [1 0 0; 0 0 1; 0 1 0]; % X permutation gate that permutes |1> and |2>
swap = II(:, [1 4 7 2 5 8 3 6 9]);  % two-qutrit SWAP gate

%% the T gate
t = [1 0 0; 0 w^(1/3) 0; 0 0 w^(-1/3)]; % T // Def.8

%%  Controlled gates from the paper "Factoring with Qutrits: Shor’s
%   Algorithm on Ternary and Metaplectic Quantum Architectures"
qubitCqutritZe = cx * kron(I,t) * cx * kron(I,t) * cx * kron(I,t);
tcz = kron(x',I) * qubitCqutritZe * kron(x,I);  % |2>-controlled Z gate
tcx = kron(I,h') * tcz * kron(I,h); % tau(20 21 22) // Lem.17
ocx = kron(x',I) * tcx * kron(x,I); % tau(10 11 12)
socxs = swap * ocx * swap; % tau(01 11 21)
tau02_20 = swap * socxs * ocx * socxs * ocx * socxs; % tau(02 20)
map21_22to02_20 = swap * cx' * swap * kron(I,x01);
tctau1_2 = map21_22to02_20' * tau02_20 * map21_22to02_20;   % |2>-controlled tau(1 2), i.e. tau(21 22) // Lem.18

%% |2>-controlled s gate
tcs = tcx' * kron(I,x01*t*x01) * tcx * kron(I,x01*t'*x01);

%% qutrit Z and X phase gates, which are Clifford whenever a and b are both integers
function gate = zphase(a, b)            % Z phase gate // Def.5
    gate = diag([1 exp(i*a) exp(i*b)]);
end
function gate = xphase(a, b)            % X phase gate // Def.6
    gate = h * zphase(a, b) * h';
end

%% The below two functions are modified from paper "Factoring with Qutrits:
% Shor’s Algorithm on Ternary and Metaplectic Quantum Architectures"
% singly-controlled X gate, where ctrl \in {0,1,2} is the control value
function scx = scx(ctrl)
    if nargin < 1
        ctrl = 2;
    end
    zcz = cx * kron(I,t) * cx * kron(I,t) * cx * kron(I,t); % |0>-controlled Z // Eq.9
    tcx = kron(x',h') * zcz * kron(x,h);                    % |2>-controlled X
    prefix = kron(ctrl_prefix(ctrl),I);
    scx = prefix' * tcx * prefix;
end
% singly-controlled D gate, where ctrl \in {0,1,2} is the control value,
% and two targets (both \in {0,1,2}) are the two values being exchanged
function scd = scd(ctrl,target)
    if nargin < 2
        target = [1 2];
    end
    if nargin < 1
        ctrl = 2;
    end
    ocx = kron(x',I) * scx * kron(x,I);
    socxs = swap * ocx * swap; % tau(01 11 21), where tau is permutation notation
    tau02_20 = swap * socxs * ocx * socxs * ocx * socxs; % tau(02 20)
    map21_22to02_20 = swap * cx' * swap * kron(I,x12);
    tcx01 = map20_21to02_20' * tau02_20 * map20_21to02_20;   % |2>-controlled x01, i.e. tau(20 21)
    prefix = kron(ctrl_prefix(ctrl),target_prefix(target));
    scd = prefix' * kron(I,x) * tcx01 * kron(I,x') * prefix;
end

%% Qutrit version of Sleator-Weinfurter trick, to build |21>-controlled V^2 * |22>-controlled V gate
function gate = vvsqtrick(tcv, tcvdag)
    if nargin == 1
        tcvdag = tcv';
    end
    cd = kron(zphase(0,pi),zphase(4*pi/3,4*pi/3)) * twoctrlcphase(4*pi/3,4*pi/3, false) * kron(I, zphase(4*pi/3,4*pi/3))/27/9 * twoctrlcphase(4*pi/3,4*pi/3) * twoctrlcphase(4*pi/3,4*pi/3, false) * kron(I, zphase(4*pi/3,4*pi/3))/27;
    cd01 = kron(I,x') * cd * kron(I,x);
    gate = kron(I,kron(x',I)*tcv*kron(x,I))*kron(cd01,I)*kron(I,kron(x',I)*tcvdag*kron(x,I))*kron(cd01,I)*kron(swap,I)*kron(I,tcv)*kron(swap,I);    % Lemma 1
end

%% permutation and tensor helper functions
% permutation gate.  the old qubit indices and mapped to the new indices
% listed in mappedtolist
function gate = perm(mappedtolist)
    I = eye(3);
    k0 = I(:,1);
    k1 = I(:,2);
    k2 = I(:,3);
    gate = eye(3^length(mappedtolist));
    for id = 1:length(mappedtolist)
        if id ~= mappedtolist(id)
            gate = swapfunc(id,mappedtolist(id),length(mappedtolist))*gate;
            mappedtolist([id mappedtolist(id)]) = mappedtolist([mappedtolist(id) id]);
        end
    end
end

function gate = swapfunc(i,j,n)
    if j < i
        tmp = i;
        i = j;
        j = tmp;
    end
    gate = eye(3^n);
    if i == j
        return;
    end
    I = eye(3);
    k0 = I(:,1);
    k1 = I(:,2);
    k2 = I(:,3);
    gate = zeros(3^n);
    ks = {k0,k1,k2};
    for a = 1:3
        for b = 1:3
            gate = gate + tensall({tenpow(I,i-1),ks{a},tenpow(I,j-i-1),ks{b},tenpow(I,n-j)}) * tensall({tenpow(I,i-1),ks{b},tenpow(I,j-i-1),ks{a},tenpow(I,n-j)})';
        end
    end
end

% returns everything in the list tensored together
function tensd = tensall(list)
    tensd = 1;
    for el = 1:numel(list)
        tensd = kron(tensd,list{el});
    end
end

% tensor to the power.  returns base^{\otimes n}
function powd = tenpow(base,n)
    powd = 1;
    for i = 1:n
        powd = kron(base,powd);
    end
end
