# DMT Core Package

DeviceModelingToolkit (DMT) is a Python tool targeted at helping modeling engineers extract model parameters, run circuit and TCAD simulations and automate their infrastructure.

The project is still in its infancy, 
though many things already work. 
Here is an incomplete list of already working stuff:

- scalable HiCUM/L2 model parameter extraction
- HiCUM/L0 model parameter extraction
- NGSpice and ADS circuit simulator interfaces
- DEVICE and Hdev TCAD simulator interface
- Data management with pandas
- Typical electrical engineering relevant data transformations such as S-to-Z parameter conversions and so on are mostly implemented
- Many examples
- Many test cases
- Interface to Verilog-A using the Verilog-AE compiler

Currently ongoing projects:

- VSource model availability
- Improve documentation
- Test coverage of > 80 %
- Simplify DMT installation and usage
