function tensd = tensall(list)
    tensd = 1;
    for el = 1:numel(list)
        tensd = kron(tensd,list{el});
    end
end