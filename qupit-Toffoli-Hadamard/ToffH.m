global d;
global I;
global H;
global ZCX;
global k0;

d = 3;
I = eye(d);
H = getH();
ZCX = getZCX();
k0 = I(:,1);

II = kron(I,I);
X = kron(k0',I) * ZCX * kron(k0,I);
CX = multAll(arrayfun(@(j) kron(X^j,I) * ZCX^j * kron(X^(d-1)^j,I), 1:d-1, 'UniformOutput', false));
ZCXupsidedown = getZCX(true);
CXupsidedown = multAll(arrayfun(@(j) kron(I,X^j) * ZCXupsidedown^j * kron(I,X^(d-1)^j), 1:d-1, 'UniformOutput', false));
swap = kron(I,H^2)*CX * kron(H^2,I)*CXupsidedown * kron(I,H^2)*CX;

P3 = swap*ZCX*swap * ZCX * swap*ZCX^(d-1)*swap * ZCX^(d-1);
Z_OCX01 = P3*swap*CX*swap*P3*swap*CX^(d-1)*swap;
X01 = kron(k0',I)*Z_OCX01*kron(k0,I);
ZCX01 = kron(X,X01) * (Z_OCX01* kron(X^2,I))^((d-1)/2);
CX01 = kron(X,I) * (ZCX01*kron(X^2,I))^((d-1)/2);
ZZCX01 = kron(I,CX01) * kron(ZCX,I) * kron(I,CX01) * kron(ZCX^(d-1),I) * kron(swap,I)*kron(I,ZCX01)*kron(swap,I);
ZZCX = (ZZCX01 * kron(II,X))^(d-1) * kron(II,X);

Q0 = kron(I,k0'*X^(d-1)*H) * ZCX * kron(I,H^3*X*k0);

%if d = 3
    ZZCw = (kron(II,H^3)*ZZCX*kron(II,H) * kron(II,X^(d-1) * X01 * X))^2;
    %ZZCwdag = (kron(II,H)*ZZCX*kron(II,H^3) * kron(II,X^(d-1) * X01 * X))^2;
    ZCS = kron(kron(I,X^(d-1)),k0') * ZZCw * kron(kron(I,X),k0);
    TCiHdag = kron(X^(d-1),H^2) * ZCS * kron(I,H^2) * ZCS * kron(I,H^3) * ZCS * kron(I,H^2) * ZCS * kron(I,H) * ZCS * kron(I,H^2) * ZCS * kron(X,I);
    %TCminusiH = kron(X^(d-1),H^2) * ZCS^2 * kron(I,H^2) * ZCS^2 * kron(I,H^3) * ZCS^2 * kron(I,H^2) * ZCS^2 * kron(I,H) * ZCS^2 * kron(I,H^2) * ZCS^2 * kron(X,I);
    RtensI = TCiHdag^2 * kron(X^(d-1),X)*ZCX01*kron(X,X^(d-1));
    R = kron(I,k0') * RtensI * kron(I,k0);
%end

1;

function H = getH()
    global d;
    w = exp(1i*2*pi/d);
    H = 1i*( w .^ mod( arrayfun(@(x,y) x*y, repmat((0:d-1).',1,d), repmat(0:d-1,d,1)), d) )/sqrt(d);
end

function ZCX = getZCX(upsidedown)
    if nargin < 1
        upsidedown = false;
    end
    global d;
    global I;
    global H;
    X = I(:,[2:end,1]);
    a = exp(1i*2*pi/d^2);
    drtZ = diag(arrayfun(@(k) a^k, 0:d-1));
    CX = cellfun(@(k) X^k,num2cell([0:d-1]),'UniformOutput',false);
    CX = blkdiag(CX{:});
    A = (kron(I,drtZ) * CX)^d;
    P0 = drtZ'*X*drtZ*X';
    CGP = P0^((d-1)/2);
    ZCX = kron(CGP,H')*A*kron(eye(d),H);
    ZCX = ZCX/ZCX(end);
    
    if upsidedown
        list = arrayfun(@(x,y) kron(kron(I(:,y+1),I(:,x+1)),kron(I(:,x+1),I(:,y+1))'), repmat((0:d-1).',1,d), repmat(0:d-1,d,1), 'UniformOutput', false);
        swap = list{1};
        for i = 2:numel(list)
            swap = swap + list{i};
        end
        ZCX = swap * ZCX * swap;
    end
end

function prod = multAll(list)
    prod = list{1};
    for i = 2:numel(list)
        prod = list{i} * prod;
    end
end
