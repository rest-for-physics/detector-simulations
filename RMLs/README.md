This directory hosts `restG4` RML definitions that will be used as a template to launch simulations.

Usually, RMLs define few variables that need to be modified at `<globals>` in order to control the behaviour of the simulation. Those variables will take a dummy value by default so that the simulation executes properly. However, those values will be modified by a external script at the `studies` directory.

- **isotope_point.rml:** A simulation where we consider radioactive decays from a point-like source.

- **isotope_volume.rml:** A simulation where we consider radioactive decays from a given GDML volume.

- **xrays.rml:** 

- **cosmic_neutrons.rml:** 

- **g4_analysis.rml:** A basic geant4 analysis processing definition to add few observables to the analysis tree. TODO. This should be probably placed at the `detector-response` repository. Although it would be good to find a way for `restG4` to generate the analysis tree observables directly on the first generated output file. See [forum post](http://rest-forum.unizar.es/t/best-way-to-connect-restg4-directy-with-the-data-processing-chain/486). 

