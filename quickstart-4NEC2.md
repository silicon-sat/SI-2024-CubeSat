# 4NEC2 Quick Start Guide 

This is a quickstart guide which takes the included dipole example and demonstrates on how to generate the radiation pattern, VSWR and matching network.

- Download and install [4NEC2](https://www.qsl.net/4nec2/) antenna modeling and simulation software.
- Start the software and load the dipole example:
  - `File-> Open 4nec2 in/out file` or click the _first_ menu button from the left and load:
  - `C:\4nec2\models\exampl2.nec`
- This example is a _copper-wire dipole_ tuned at _300 MHz_.
- The code syntax is explained in the section below:

# Syntax explaination for the Dipole example 

```bash
SY len=.34642				' Symbol: Length for WL/2
'
GW 1 9 0 -len/2 0 0 len/2 0 .0001	' Wire 1, 9 segments, halve wavelength long.
GE 0					' End of geometry
'
LD 5 1 0 0 5.8001E7			' Wire conductivity
'
EX 0 1 5 0 1 0				' Voltage source (1+j0) at wire 1 segment 5.
FR 0 1 0 0 300 0			' Set design frequency (300 Mc).
EN	
``` 

- **SY**: Defines a symbolic variable len with the value `0.34642`. This represents the length of the dipole antenna in wavelengths (WL).
- **GW**: Defines a wire structure.
  - `1`: Wire tag number.
  - `9`: Number of segments in the wire.
  - `0 -len/2 0`: Coordinates of the start of the wire (x1, y1, z1).
  - `0  len/2 0`: Coordinates of the end of the wire (x2, y2, z2).
  - `0.0001`: Radius of the wire in meters.
  - This command defines a wire (dipole) that is centered at the origin and extends len/2 units in both directions along the y-axis. The wire is segmented into 9 parts, and it has a small radius of 0.0001 meters.
- **GE**: Indicates the end of the geometry specification.  `0`: Indicates the end of the geometry input.
- **LD**: Specifies the loading (i.e., material properties) of the wire.
  - `5`: Conductivity type.
  - `1`: Wire tag number.
  - `0`: Starting segment.
  - `0`: Ending segment.
  - `5.8001E7`: Conductivity of the wire material in Siemens per meter (S/m).
- **EX**: Specifies an excitation (source) for the antenna.
  - `0`: Excitation type (voltage source).
  - `1`: Wire tag number.
  - `5`: Segment number where the source is applied.
  - `0`: Not used in this context.
  - `1`: Real part of the source voltage.
  - `0`: Imaginary part of the source voltage.
- **FR**: Specifies the frequency of the simulation.
  - `0`: Frequency type (single frequency).
  - `1`: Number of frequency steps.
  - `0`: Starting frequency.
  - `0`: Frequency step size.
  - `300`: Design frequency in MHz (300 MHz).
  - `0`: Not used in this context.
