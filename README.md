# BitOQSim

## Contents

- [Acknowledgements](#Acknowledgements)
- [Abstract](#Abstract)
- [Background Information](#Background-Information)
- [BitOQSim Source](#BitOQSim-Source)
- [Completed Examples](#Completed-Examples)
- [WIP Examples](#WIP-Examples)
- [License and Notice](#License-and-Notice)
- [Requirements](#Requirements)
- [Documentation](#Documentation)
- [Disclaimer](#Disclaimer)
- [Further Reading](#Further-Reading)
- [Contribute](#Contribute)
- [Credits](#Credits)

***

## Acknowledgements
Thank you, Professor Phillip Conrad and Professor Richert Wang for advising and
encouraging me as well as for connecting me with experts in quantum computing
as well as experts in numerous other fields.
<br />
Thank you, Professor Yufei Ding and Professor Tim Sherwood for guiding me in
beginning to create BitOQSim.
<br />
Thank you, Professor Wim van Dam for advising me through creating BitOQSim as
well as for giving me concrete goals for BitOQSim in Shor's factoring algorithm
and computing discrete logarithms.
<br />
Thank you, Lia Yeh for giving me feedback on BitOQSim as well as giving me the
opportunity to work on the qutrit research paper.

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

## Background Information

Qubits may be represented as square matrices, column vectors, row vectors,
or a linear combination thereof.

* [Quantum computing basic background information](BACKGROUND.md)

* [CWI Thesis On Quantum Computation Theory](https://www.illc.uva.nl/Research/Publications/Dissertations/DS-2002-04.text.pdf)

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

## Further Reading

Useful additional resources used are included as links when relevant.

## Contribute

Feel free to [open an issue](https://github.com/ccs-1l-f21/BitOQSim/issues/new)
if you'd like to give me feedback or ask for features.

If you'd like to contribute, feel free to fork this repository and open a pull
request.

## Credits

Alex Lim

[![GitHub Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AlexLim-Pro)
[![Gmail Badge](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:alex@virtueware.com)