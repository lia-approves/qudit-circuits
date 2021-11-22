# Quantum Computing Basic Background Information

## Contents

- [Qubit Notation](#Qubit-Notation)

***

## Qubit Notation

Qubits can be represented using
[bra-ket notation](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Quantum_Mechanics/03._The_Tools_of_Quantum_Mechanics/Bra-Ket_Notation).

Equivalently, qubits can be represented using vectors.

**Bra Notation**

<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left\langle%20A\right|=\left(\left|A\right\rangle\right)^\dagger=\begin{pmatrix}A_1%26A_2%26\cdots%26A_n\end{pmatrix}">

</div>


**Ket Notation**

<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left|A\right\rangle=\left(\left\langle{A}\right|\right)^\dagger=\begin{pmatrix}A_1\\A_2\\%0A\vdots\\A_n\end{pmatrix}">

</div>


† is the
[Hermitian conjugate (or the conjugate transpose)](https://mathworld.wolfram.com/ConjugateTranspose.html)
which is the transpose of the conjugate matrix.  The
[conjugate matrix](https://mathworld.wolfram.com/ConjugateMatrix.html)
is the matrix obtained by taking the complex conjugate of each element of the
matrix.

⊕ is the
[Kronecker product](https://mathworld.wolfram.com/KroneckerProduct.html)
which is the matrix generalization of the vector
[outer product](https://en.wikipedia.org/wiki/Outer_product).

[comment]: <> (Example bras)
<details>
    <summary>Example bras</summary>

<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\newline\left\langle%20A\right|\otimes\left\langle%20B\right|\otimes\left\langle%20C\right|=(\left\langle%20A\right|\otimes\left\langle%20B\right|)\otimes\left\langle%20C\right|=\left\langle%20AB\right|\otimes\left\langle%20C\right|=\left\langle%20ABC\right|\newline\left\langle%20A\right|\otimes\left\langle%20B\right|\otimes\left\langle%20C\right|=\left\langle%20A\right|\otimes(\left\langle%20B\right|\otimes\left\langle%20C\right|)=\left\langle%20A\right|\otimes\left\langle%20BC\right|=\left\langle%20ABC\right|">

</div>


[comment]: <> (0 bra)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left\langle0\right|=\begin{pmatrix}1%260\end{pmatrix}">

</div>

<br />

[comment]: <> (1 bra)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left\langle1\right|=\begin{pmatrix}0%261\end{pmatrix}">

</div>

<br />

[comment]: <> (00 bra)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left\langle00\right|=\left\langle0\right|\otimes\left\langle0\right|=\begin{pmatrix}1%260\end{pmatrix}\otimes\begin{pmatrix}1%260\end{pmatrix}=\begin{pmatrix}1%260%260%260\end{pmatrix}">

</div>

<br />

[comment]: <> (01 bra)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left\langle01\right|=\left\langle0\right|\otimes\left\langle1\right|=\begin{pmatrix}1%260\end{pmatrix}\otimes\begin{pmatrix}0%261\end{pmatrix}=\begin{pmatrix}0%261%260%260\end{pmatrix}">

</div>

<br />

[comment]: <> (10 bra)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left\langle10\right|=\left\langle1\right|\otimes\left\langle0\right|=\begin{pmatrix}0%261\end{pmatrix}\otimes\begin{pmatrix}1%260\end{pmatrix}=\begin{pmatrix}0%260%261%260\end{pmatrix}">

</div>

<br />

[comment]: <> (11 bra)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left\langle11\right|=\left\langle1\right|\otimes\left\langle1\right|=\begin{pmatrix}0%261\end{pmatrix}\otimes\begin{pmatrix}0%261\end{pmatrix}=\begin{pmatrix}0%260%260%261\end{pmatrix}">

</div>

<br />

[comment]: <> (000 bra)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left\langle000\right|=\left\langle0\right|\otimes\left\langle0\right|\otimes\left\langle0\right|=\left\langle00\right|\otimes\left\langle0\right|=\begin{pmatrix}1%260%260%260\end{pmatrix}\otimes\begin{pmatrix}1%260\end{pmatrix}=\begin{pmatrix}1%260%260%260%260%260%260%260\end{pmatrix}">

</div>

<br />

[comment]: <> (001 bra)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left\langle001\right|=\left\langle0\right|\otimes\left\langle0\right|\otimes\left\langle1\right|=\left\langle00\right|\otimes\left\langle1\right|=\begin{pmatrix}1%260%260%260\end{pmatrix}\otimes\begin{pmatrix}0%261\end{pmatrix}=\begin{pmatrix}0%261%260%260%260%260%260%260\end{pmatrix}">

</div>

<br />

[comment]: <> (010 bra)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left\langle010\right|=\left\langle0\right|\otimes\left\langle1\right|\otimes\left\langle0\right|=\left\langle01\right|\otimes\left\langle0\right|=\begin{pmatrix}0%261%260%260\end{pmatrix}\otimes\begin{pmatrix}1%260\end{pmatrix}=\begin{pmatrix}0%260%261%260%260%260%260%260\end{pmatrix}">

</div>

<br />

[comment]: <> (011 bra)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left\langle011\right|=\left|0\right\rangle\otimes\left\langle1\right|\otimes\left\langle1\right|=\left\langle01\right|\otimes\left\langle1\right|=\begin{pmatrix}0%261%260%260\end{pmatrix}\otimes\begin{pmatrix}0%261\end{pmatrix}=\begin{pmatrix}0%260%260%261%260%260%260%260\end{pmatrix}">

</div>

<br />

[comment]: <> (100 bra)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left\langle100\right|=\left\langle1\right|\otimes\left\langle0\right|\otimes\left\langle0\right|=\left\langle10\right|\otimes\left\langle0\right|=\begin{pmatrix}0%260%261%260\end{pmatrix}\otimes\begin{pmatrix}1%260\end{pmatrix}=\begin{pmatrix}0%260%260%260%261%260%260%260\end{pmatrix}">

</div>

<br />

[comment]: <> (101 bra)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left\langle101\right|=\left\langle1\right|\otimes\left\langle0\right|\otimes\left\langle1\right|=\left\langle10\right|\otimes\left\langle1\right|=\begin{pmatrix}0%260%261%260\end{pmatrix}\otimes\begin{pmatrix}0%261\end{pmatrix}=\begin{pmatrix}0%260%260%260%260%261%260%260\end{pmatrix}">

</div>

<br />

[comment]: <> (110 bra)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left\langle110\right|=\left\langle1\right|\otimes\left\langle1\right|\otimes\left\langle0\right|=\left\langle11\right|\otimes\left\langle0\right|=\begin{pmatrix}0%260%260%261\end{pmatrix}\otimes\begin{pmatrix}1%260\end{pmatrix}=\begin{pmatrix}0%260%260%260%260%260%261%260\end{pmatrix}">

</div>

<br />

[comment]: <> (111 bra)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left\langle111\right|=\left\langle1\right|\otimes\left\langle1\right|\otimes\left\langle1\right|=\left\langle11\right|\otimes\left\langle1\right|=\begin{pmatrix}0%260%260%261\end{pmatrix}\otimes\begin{pmatrix}0%261\end{pmatrix}=\begin{pmatrix}0%260%260%260%260%260%260%261\end{pmatrix}">

</div>

</details>

<br />

[comment]: <> (Example kets)
<details>
    <summary>Example kets</summary>

<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\newline\left|A\right\rangle\otimes\left|B\right\rangle\otimes\left|C\right\rangle=(\left|A\right\rangle\otimes\left|B\right\rangle)\otimes\left|C\right\rangle=\left|AB\right\rangle\otimes\left|C\right\rangle=\left|ABC\right\rangle\newline\left|A\right\rangle\otimes\left|B\right\rangle\otimes\left|C\right\rangle=\left|A\right\rangle\otimes(\left|B\right\rangle\otimes\left|C\right\rangle)=\left|A\right\rangle\otimes\left|BC\right\rangle=\left|ABC\right\rangle">

</div>

<br />

[comment]: <> (0 ket)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left|0\right\rangle=\begin{pmatrix}1\\%0A0\end{pmatrix}">

</div>

<br />

[comment]: <> (1 ket)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left|1\right\rangle=\begin{pmatrix}0\\%0A1\end{pmatrix}">

</div>

<br />

[comment]: <> (00 ket)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left|00\right\rangle=\left|0\right\rangle\otimes\left|0\right\rangle=\begin{pmatrix}1\\%0A0\end{pmatrix}\otimes\begin{pmatrix}1\\%0A0\end{pmatrix}=\begin{pmatrix}1\\%0A0\\%0A0\\%0A0\end{pmatrix}">

</div>

<br />

[comment]: <> (01 ket)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left|01\right\rangle=\left|0\right\rangle\otimes\left|1\right\rangle=\begin{pmatrix}1\\%0A0\end{pmatrix}\otimes\begin{pmatrix}0\\%0A1\end{pmatrix}=\begin{pmatrix}0\\%0A1\\%0A0\\%0A0\end{pmatrix}">

</div>

<br />

[comment]: <> (10 ket)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left|10\right\rangle=\left|1\right\rangle\otimes\left|0\right\rangle=\begin{pmatrix}0\\%0A1\end{pmatrix}\otimes\begin{pmatrix}1\\%0A0\end{pmatrix}=\begin{pmatrix}0\\%0A0\\%0A1\\%0A0\end{pmatrix}">

</div>

<br />

[comment]: <> (11 ket)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left|11\right\rangle=\left|1\right\rangle\otimes\left|1\right\rangle=\begin{pmatrix}0\\%0A1\end{pmatrix}\otimes\begin{pmatrix}0\\%0A1\end{pmatrix}=\begin{pmatrix}0\\%0A0\\%0A0\\%0A1\end{pmatrix}">

</div>

<br />

[comment]: <> (000 ket)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left|000\right\rangle=\left|0\right\rangle\otimes\left|0\right\rangle\otimes\left|0\right\rangle=\left|00\right\rangle\otimes\left|0\right\rangle=\begin{pmatrix}1\\%0A0\\%0A0\\%0A0\end{pmatrix}\otimes\begin{pmatrix}1\\%0A0\end{pmatrix}=\begin{pmatrix}1\\%0A0\\%0A0\\%0A0\\%0A0\\%0A0\\%0A0\\%0A0\end{pmatrix}">

</div>

<br />

[comment]: <> (001 ket)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left|001\right\rangle=\left|0\right\rangle\otimes\left|0\right\rangle\otimes\left|1\right\rangle=\left|00\right\rangle\otimes\left|1\right\rangle=\begin{pmatrix}1\\%0A0\\%0A0\\%0A0\end{pmatrix}\otimes\begin{pmatrix}0\\%0A1\end{pmatrix}=\begin{pmatrix}0\\%0A1\\%0A0\\%0A0\\%0A0\\%0A0\\%0A0\\%0A0\end{pmatrix}">

</div>

<br />

[comment]: <> (010 ket)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left|010\right\rangle=\left|0\right\rangle\otimes\left|1\right\rangle\otimes\left|0\right\rangle=\left|01\right\rangle\otimes\left|0\right\rangle=\begin{pmatrix}0\\%0A1\\%0A0\\%0A0\end{pmatrix}\otimes\begin{pmatrix}1\\%0A0\end{pmatrix}=\begin{pmatrix}0\\%0A0\\%0A1\\%0A0\\%0A0\\%0A0\\%0A0\\%0A0\end{pmatrix}">

</div>

<br />

[comment]: <> (011 ket)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left|011\right\rangle=\left|0\right\rangle\otimes\left|1\right\rangle\otimes\left|1\right\rangle=\left|01\right\rangle\otimes\left|1\right\rangle=\begin{pmatrix}0\\%0A1\\%0A0\\%0A0\end{pmatrix}\otimes\begin{pmatrix}0\\%0A1\end{pmatrix}=\begin{pmatrix}0\\%0A0\\%0A0\\%0A1\\%0A0\\%0A0\\%0A0\\%0A0\end{pmatrix}">

</div>

<br />

[comment]: <> (100 ket)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left|100\right\rangle=\left|1\right\rangle\otimes\left|0\right\rangle\otimes\left|0\right\rangle=\left|10\right\rangle\otimes\left|0\right\rangle=\begin{pmatrix}0\\%0A0\\%0A1\\%0A0\end{pmatrix}\otimes\begin{pmatrix}1\\%0A0\end{pmatrix}=\begin{pmatrix}0\\%0A0\\%0A0\\%0A0\\%0A1\\%0A0\\%0A0\\%0A0\end{pmatrix}">

</div>

<br />

[comment]: <> (101 ket)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left|101\right\rangle=\left|1\right\rangle\otimes\left|0\right\rangle\otimes\left|1\right\rangle=\left|10\right\rangle\otimes\left|1\right\rangle=\begin{pmatrix}0\\%0A0\\%0A1\\%0A0\end{pmatrix}\otimes\begin{pmatrix}0\\%0A1\end{pmatrix}=\begin{pmatrix}0\\%0A0\\%0A0\\%0A0\\%0A0\\%0A1\\%0A0\\%0A0\end{pmatrix}">

</div>

<br />

[comment]: <> (110 ket)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left|110\right\rangle=\left|1\right\rangle\otimes\left|1\right\rangle\otimes\left|0\right\rangle=\left|11\right\rangle\otimes\left|0\right\rangle=\begin{pmatrix}0\\%0A0\\%0A0\\%0A1\end{pmatrix}\otimes\begin{pmatrix}1\\%0A0\end{pmatrix}=\begin{pmatrix}0\\%0A0\\%0A0\\%0A0\\%0A0\\%0A0\\%0A1\\%0A0\end{pmatrix}">

</div>


[comment]: <> (111 ket)
<div style="background-color:rgb(0, 0, 0); text-align:center; vertical-align: middle; padding:10px">

<img src="https://render.githubusercontent.com/render/math?math=\color{white}\left|111\right\rangle=\left|1\right\rangle\otimes\left|1\right\rangle\otimes\left|1\right\rangle=\left|11\right\rangle\otimes\left|1\right\rangle=\begin{pmatrix}0\\%0A0\\%0A0\\%0A1\end{pmatrix}\otimes\begin{pmatrix}0\\%0A1\end{pmatrix}=\begin{pmatrix}0\\%0A0\\%0A0\\%0A0\\%0A0\\%0A0\\%0A0\\%0A1\end{pmatrix}">

</div>


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