function s = dispcomplex(c)
    if abs(real(c)) <= 1e-5
        s = sprintf('\t\t\t%6.3f i',imag(c));
    elseif abs(imag(c)) <= 1e-5
        s = sprintf('\t%6.3f\t\t\t',real(c));
    else
        s = sprintf('\t%6.3f +%6.3f i',real(c),imag(c));
    end
end