# Quantum Computing Basic Background Information

## Contents

- [Qubit Notation](#Qubit-Notation)

## Qubit Notation

Qubits can be represented using
[bra-ket notation](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Quantum_Mechanics/03._The_Tools_of_Quantum_Mechanics/Bra-Ket_Notation).

Equivalently, qubits can be represented using vectors.

**Example**

<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny |A\rangle=(\langle A|)^\dagger=\begin{pmatrix}A_1\\A_2\\\vdots\\A_n\end{pmatrix}">

<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny \langle A|=(|A\rangle)^\dagger=\begin{pmatrix}A_1&A_2&\cdots&A_n\end{pmatrix}">

† is the
[Hermitian conjugate (or the conjugate transpose)](https://mathworld.wolfram.com/ConjugateTranspose.html)
which is the transpose of the conjugate matrix.  The 

[comment]: <> (Example kets)
<details>
    <summary>Example kets</summary>

<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny\newline|A\rangle\otimes|B\rangle\otimes|C\rangle=(|A\rangle\otimes|B\rangle)\otimes|C\rangle=|AB\rangle\otimes|C\rangle=|ABC\rangle\newline|A\rangle\otimes|B\rangle\otimes|C\rangle=|A\rangle\otimes(|B\rangle\otimes|C\rangle)=|A\rangle\otimes|BC\rangle=|ABC\rangle">

⊕ is the
[Kronecker product](https://mathworld.wolfram.com/KroneckerProduct.html)
which is the matrix generalization of the vector
[outer product](https://en.wikipedia.org/wiki/Outer_product).

[comment]: <> (0 ket)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny |0\rangle=\begin{pmatrix}1\\0\end{pmatrix}">
<br />

[comment]: <> (1 ket)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny |1\rangle=\begin{pmatrix}0\\1\end{pmatrix}">
<br />

[comment]: <> (00 ket)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny |00\rangle=|0\rangle\otimes|0\rangle=\begin{pmatrix}1\\0\end{pmatrix}\otimes\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}1\\0\\0\\0\end{pmatrix}">
<br />

[comment]: <> (01 ket)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny |01\rangle=|0\rangle\otimes|1\rangle=\begin{pmatrix}1\\0\end{pmatrix}\otimes\begin{pmatrix}0\\1\end{pmatrix}=\begin{pmatrix}0\\1\\0\\0\end{pmatrix}">
<br />

[comment]: <> (10 ket)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny |10\rangle=|0\rangle\otimes|1\rangle=\begin{pmatrix}0\\1\end{pmatrix}\otimes\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}0\\0\\1\\0\end{pmatrix}">
<br />

[comment]: <> (11 ket)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny |11\rangle=|1\rangle\otimes|1\rangle=\begin{pmatrix}0\\1\end{pmatrix}\otimes\begin{pmatrix}0\\1\end{pmatrix}=\begin{pmatrix}0\\0\\0\\1\end{pmatrix}">
<br />

[comment]: <> (000 ket)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny |000\rangle=|0\rangle\otimes|0\rangle\otimes|0\rangle=|00\rangle\otimes|0\rangle=\begin{pmatrix}1\\0\\0\\0\end{pmatrix}\otimes\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}1\\0\\0\\0\\0\\0\\0\\0\end{pmatrix}">
<br />

[comment]: <> (001 ket)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny |001\rangle=|0\rangle\otimes|0\rangle\otimes|1\rangle=|00\rangle\otimes|1\rangle=\begin{pmatrix}1\\0\\0\\0\end{pmatrix}\otimes\begin{pmatrix}0\\1\end{pmatrix}=\begin{pmatrix}0\\1\\0\\0\\0\\0\\0\\0\end{pmatrix}">
<br />

[comment]: <> (010 ket)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny |010\rangle=|0\rangle\otimes|1\rangle\otimes|0\rangle=|01\rangle\otimes|0\rangle=\begin{pmatrix}0\\1\\0\\0\end{pmatrix}\otimes\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}0\\0\\1\\0\\0\\0\\0\\0\end{pmatrix}">
<br />

[comment]: <> (011 ket)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny |011\rangle=|0\rangle\otimes|1\rangle\otimes|1\rangle=|01\rangle\otimes|1\rangle=\begin{pmatrix}0\\1\\0\\0\end{pmatrix}\otimes\begin{pmatrix}0\\1\end{pmatrix}=\begin{pmatrix}0\\0\\0\\1\\0\\0\\0\\0\end{pmatrix}">
<br />

[comment]: <> (100 ket)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny |100\rangle=|1\rangle\otimes|0\rangle\otimes|0\rangle=|10\rangle\otimes|0\rangle=\begin{pmatrix}0\\0\\1\\0\end{pmatrix}\otimes\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}0\\0\\0\\0\\1\\0\\0\\0\end{pmatrix}">
<br />

[comment]: <> (101 ket)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny |101\rangle=|1\rangle\otimes|0\rangle\otimes|1\rangle=|10\rangle\otimes|1\rangle=\begin{pmatrix}0\\0\\1\\0\end{pmatrix}\otimes\begin{pmatrix}0\\1\end{pmatrix}=\begin{pmatrix}0\\0\\0\\0\\0\\1\\0\\0\end{pmatrix}">
<br />

[comment]: <> (110 ket)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny |110\rangle=|1\rangle\otimes|1\rangle\otimes|0\rangle=|11\rangle\otimes|0\rangle=\begin{pmatrix}0\\0\\0\\1\end{pmatrix}\otimes\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}0\\0\\0\\0\\0\\0\\1\\0\end{pmatrix}">

[comment]: <> (111 ket)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny |111\rangle=|1\rangle\otimes|1\rangle\otimes|1\rangle=|11\rangle\otimes|1\rangle=\begin{pmatrix}0\\0\\0\\1\end{pmatrix}\otimes\begin{pmatrix}0\\1\end{pmatrix}=\begin{pmatrix}0\\0\\0\\0\\0\\0\\0\\1\end{pmatrix}">

</details>

[comment]: <> (Example bras)
<details>
    <summary>Example bras</summary>

![Kronecker product example](https://latex.codecogs.com/png.latex?\dpi{300}%20\bg_black%20\tiny\newline\langle%20A|\otimes\langle%20B|\otimes\langle%20C|=(\langle%20A|\otimes\langle%20B|)\otimes\langle%20C|=\langle%20AB|\otimes\langle%20C|=\langle%20ABC|\newline\langle%20A|\otimes\langle%20B|\otimes\langle%20C|=\langle%20A|\otimes(\langle%20B|\otimes\langle%20C|)=\langle%20A|\otimes\langle%20BC|=\langle%20ABC|)

[comment]: <> (<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny\newline\langle A|\otimes\langle B|\otimes\langle C|=&#40;\langle A|\otimes\langle B|&#41;\otimes\langle C|=\langle AB|\otimes\langle C|=\langle ABC|\newline\langle A|\otimes\langle B|\otimes\langle C|=\langle A|\otimes&#40;\langle B|\otimes\langle C|&#41;=\langle A|\otimes\langle BC|=\langle ABC|">)

⊕ is the
[Kronecker product](https://mathworld.wolfram.com/KroneckerProduct.html)
which is the matrix generalization of the vector
[outer product](https://en.wikipedia.org/wiki/Outer_product).

[comment]: <> (0 bra)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny \langle0|=\begin{pmatrix}1&0\end{pmatrix}">
<br />

[comment]: <> (1 bra)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny \langle1|=\begin{pmatrix}0&1\end{pmatrix}">
<br />

[comment]: <> (00 bra)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny \langle00|=\langle0|\otimes\langle0|=\begin{pmatrix}1&0\end{pmatrix}\otimes\begin{pmatrix}1&0\end{pmatrix}=\begin{pmatrix}1&0&0&0\end{pmatrix}">
<br />

[comment]: <> (01 bra)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny \langle01|=\langle0|\otimes\langle1|=\begin{pmatrix}1&0\end{pmatrix}\otimes\begin{pmatrix}0&1\end{pmatrix}=\begin{pmatrix}0&1&0&0\end{pmatrix}">
<br />

[comment]: <> (10 bra)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny \langle10|=\langle0|\otimes\langle1|=\begin{pmatrix}0&1\end{pmatrix}\otimes\begin{pmatrix}1&0\end{pmatrix}=\begin{pmatrix}0&0&1&0\end{pmatrix}">
<br />

[comment]: <> (11 bra)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny \langle11|=\langle1|\otimes\langle1|=\begin{pmatrix}0&1\end{pmatrix}\otimes\begin{pmatrix}0&1\end{pmatrix}=\begin{pmatrix}0&0&0&1\end{pmatrix}">
<br />

[comment]: <> (000 bra)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny \langle000|=\langle0|\otimes\langle0|\otimes\langle0|=\langle00|\otimes\langle0|=\begin{pmatrix}1&0&0&0\end{pmatrix}\otimes\begin{pmatrix}1&0\end{pmatrix}=\begin{pmatrix}1&0&0&0&0&0&0&0\end{pmatrix}">
<br />

[comment]: <> (001 bra)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny \langle001|=\langle0|\otimes\langle0|\otimes\langle1|=\langle00|\otimes\langle1|=\begin{pmatrix}1&0&0&0\end{pmatrix}\otimes\begin{pmatrix}0&1\end{pmatrix}=\begin{pmatrix}0&1&0&0&0&0&0&0\end{pmatrix}">
<br />

[comment]: <> (010 bra)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny \langle010|=\langle0|\otimes\langle1|\otimes\langle0|=\langle01|\otimes\langle0|=\begin{pmatrix}0&1&0&0\end{pmatrix}\otimes\begin{pmatrix}1&0\end{pmatrix}=\begin{pmatrix}0&0&1&0&0&0&0&0\end{pmatrix}">
<br />

[comment]: <> (011 bra)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny \langle011|=|0\rangle\otimes\langle1|\otimes\langle1|=\langle01|\otimes\langle1|=\begin{pmatrix}0&1&0&0\end{pmatrix}\otimes\begin{pmatrix}0&1\end{pmatrix}=\begin{pmatrix}0&0&0&1&0&0&0&0\end{pmatrix}">
<br />

[comment]: <> (100 bra)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny \langle100|=\langle1|\otimes\langle0|\otimes\langle0|=\langle10|\otimes\langle0|=\begin{pmatrix}0&0&1&0\end{pmatrix}\otimes\begin{pmatrix}1&0\end{pmatrix}=\begin{pmatrix}0&0&0&0&1&0&0&0\end{pmatrix}">
<br />

[comment]: <> (101 bra)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny \langle101|=\langle1|\otimes\langle0|\otimes\langle1|=\langle10|\otimes\langle1|=\begin{pmatrix}0&0&1&0\end{pmatrix}\otimes\begin{pmatrix}0&1\end{pmatrix}=\begin{pmatrix}0&0&0&0&0&1&0&0\end{pmatrix}">
<br />

[comment]: <> (110 bra)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny \langle110|=\langle1|\otimes\langle1|\otimes\langle0|=\langle11|\otimes\langle0|=\begin{pmatrix}0&0&0&1\end{pmatrix}\otimes\begin{pmatrix}1&0\end{pmatrix}=\begin{pmatrix}0&0&0&0&0&0&1&0\end{pmatrix}">

[comment]: <> (111 bra)
<img src="https://latex.codecogs.com/png.latex?\dpi{300} \bg_black \tiny \langle111|=\langle1|\otimes\langle1|\otimes\langle1|=\langle11|\otimes\langle1|=\begin{pmatrix}0&0&0&1\end{pmatrix}\otimes\begin{pmatrix}0&1\end{pmatrix}=\begin{pmatrix}0&0&0&0&0&0&0&1\end{pmatrix}">

</details>





<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>