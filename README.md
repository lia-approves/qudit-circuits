# BitOQSim

## Contents

- [Acknowledgements](#Acknowledgements)
- [BitOQSim Source](#BitOQSim-Source)

## Acknowledgements:
Thank you, Professor Phillip Conrad and Professor Richert Wang for advising and
encouraging me as well as for connecting me with experts in quantum computing
as well as experts in numerous other fields.
<br />
Thank you, Professor Yufei Ding and Professor Tim Sherwood for guiding me in
beginning to create BitOQSim.
<br />
Thank you, Professor Win van Dam for advising me through creating BitOQSim as
well as for giving me concrete goals for BitOQSim in Shor's factoring algorithm
and computing discrete logarithms.
<br />
Thank you, Lia Yeh for giving me feedback on BitOQSim as well as giving me the
opportunity to work on the qutrit research paper.

## BitOQSim Source

* [Quantum circuit matrices](QuantumCircuitMatrix.py)

* [Miscellaneous functions](MiscFunctions.py)

## Completed Examples

* [Grover's search algorithm in BitOQSim](GroverSearchAlgorithm.py)

* [Shor's factoring algorithm in BitOQSim](ShorFactoringAlgorithm.py)

* [Shor's factoring algorithm in Qiskit](QiskitShorFactoringAlgorithm.py)

## WIP Examples

* [Testing file](TestFile.py)

* [Discrete logarithm problem in BitOQSim](ComputingDiscreteLogarithms.py)

## License and Notice

* [License](LICENSE)

* [Notice](NOTICE)

## Requirements

* [BitOQSim](https://github.com/ccs-1l-f21/BitOQSim.git) was developed in
[Python 3.9.7](https://www.python.org/downloads/release/python-397/), and 
[Python 3.9.x](https://www.python.org/dev/peps/pep-0596/) is recommended,
although not required.

* [Required Python packages](requirement.txt)

## Abstract

[BitOQSim](https://github.com/ccs-1l-f21/BitOQSim.git) is designed as a way to
simulate quantum computers and quantum algorithms using classical computers.

In order for the language to be more transparent and educationally useful,
[BitOQSim](https://github.com/ccs-1l-f21/BitOQSim.git) uses matrices in order
to simulate qubits and quantum gates in a way that is less esoteric than other
high-level quantum simulators.  In testing,
[BitOQSim](https://github.com/ccs-1l-f21/BitOQSim.git) has proven to be
particularly useful in explaining how quantum gates function and how to build
quantum circuits when compared with high-level gate and circuit
implementations.

## Documentation

[BitOQSim](https://github.com/ccs-1l-f21/BitOQSim.git) is documented using
[Sphinx](https://www.sphinx-doc.org/en/master/) with
[reStructuredText](https://docutils.sourceforge.io/rst.html)
as its markup language.

## Disclaimer

[BitOQSim](https://github.com/ccs-1l-f21/BitOQSim.git) is not an
[IBM](https://www.ibm.com/us-en/) product, and code that uses
[Qiskit](https://qiskit.org/) is explicitly labeled as such.  Equivalent
[Qiskit](https://qiskit.org/) implementations are included in order to be used
as points of comparison.

## Background Information

Qubits may be represented as square matrices, column vectors, row vectors,
or a linear combination thereof.

* [Quantum computing basic background information](BACKGROUND.md)

## Further Reading

Useful additional resources used are included as links when relevant.