%% Implementation of the R = diag(1,1,-1) gate unitarily in qutrit Clifford+T
% accompanying the paper "The qutrit metaplectic gate is Clifford+T"

%% identity and zero matrices
I = eye(3);     % single-qutrit identity gate, i.e. 3 x 3 identity matrix
II = eye(3^2);  % two-qutrit identity gate
zero = zeros([3]);  % 3 x 3 zero matrix

%% Z and X basis states
k0 = I(:,1);    % Z-basis states
k1 = I(:,2);    % "
k2 = I(:,3);    % "
w = exp(2*pi*i/3);      % 3rd root of unity
kpl = (k0 + k1 + k2)/sqrt(3);               % X-basis states
kw = (k0 + w * k1 + w^2 * k2)/sqrt(3);      % "
kwsq = (k0 + w^2 * k1 + w * k2)/sqrt(3);    % "

%% qutrit generalization of Pauli gates
x = [0 0 1; 1 0 0; 0 1 0];    % X, i.e. tau(0 1 2)
z = [1 0 0; 0 w 0; 0 0 w^2];  % Z = H * X * H'

%% qutrit S, H, and CX, which generate the Clifford group
s = [1 0 0; 0 1 0; 0 0 w];  % S
h = i * (kron(kpl, k0') + kron(kw, k1') + kron(kwsq, k2'));   % H
cx = [I zero zero; zero x zero; zero zero x'];   % CX, i.e. tau(10 11 12)(20 22 21)

%% various other Clifford gates
tau0_1 = [0 1 0; 1 0 0; 0 0 1]; % tau(0 1)
tau0_2 = [0 0 1; 0 1 0; 1 0 0]; % tau(0 2)
tau1_2 = [1 0 0; 0 0 1; 0 1 0]; % tau(1 2) = H * H up to a global phase of -1
zww = tau1_2 * s * tau1_2 * s; % = [1 0 0; 0 w 0; 0 0 w];
swap = II(:, [1 4 7 2 5 8 3 6 9]);  % two-qutrit SWAP gate

%% the T gate
t = [1 0 0; 0 w^(1/3) 0; 0 0 w^(-1/3)]; % T

%%  Controlled gates from the paper "Factoring with Qutrits: Shor’s
%   Algorithm on Ternary and Metaplectic Quantum Architectures"
p9 = x * t * x';    % the P9 gate, which is Clifford equivalent to T
qubitCqutritZe = cx * kron(I,p9) * cx * kron(I,p9) * cx * kron(I,p9);
tcx = kron(x',h'*x') * qubitCqutritZe * kron(x,x*h); % tau(20 21 22)
ocx = kron(x',I) * tcx * kron(x,I); % tau(10 11 12)
socxs = swap * ocx * swap; % tau(01 11 21)
tau02_20 = swap * socxs * ocx * socxs * ocx * socxs; % tau(02 20)
map21_22to02_20 = swap * cx' * swap * kron(I,tau0_1);
tctau1_2 = map21_22to02_20' * tau02_20 * map21_22to02_20;   % |2>-controlled tau(1 2), i.e. tau(21 22)

%% |2>-controlled zww gate, up to a global phase of w^(1/3)
tczwwphase = kron(x',x') * cx' * kron(I,x*t*x') * cx' * kron(I,x*t*x') * cx' * kron(x,tau0_2*s'*tau0_1) * tcx' * kron(I,tau0_1*t'*tau0_1) * tcx;
%% |2>-controlled -tau(1 2) gate, i.e. tctau1_2 but when the control is |2>, the target gains a -1 phase
tcmtau1_2 = kron(tau0_2*z*tau0_2*z*s',tau0_2*z*tau0_2*z*zww*h') * tczwwphase * kron(I,h*zww) * tczwwphase * kron(I,h') * tczwwphase * kron(I,h*zww);
%% the below two-qutrit Clifford+T unitary is the R gate on one qutrit and the identity gate on the other
rtensorid = tcmtau1_2 * tctau1_2;
%% to verify: subtracting the R gate tensor the single-qutrit identity from it equals zero
r = [1 0 0; 0 1 0; 0 0 -1];
assert(all(all(round(rtensorid,10) - kron(r,I) == 0))) % rounding to the 10^(-10) decimal place due to floating point error
