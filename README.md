This is a reference repository to be used as a template to create REST based Geant4 simulations in IAXO. This repository will define a recommended structure when working with REST, provide generic RML definitions, and scripts to launch simulations that will be later on personalized for different dedicated projects, as for IAXO-D0, IAXO-D1, BabyIAXO, etc.

Please, update this README.md at the repository with detailed project information

### Basic project structure/contents:

- **simulations**: It will contain the RML definitions that are used to launch `restG4`. We should be able to launch/test them by just going to the corresponding directory and executing `restG4 conf.rml`. Therefore, it will define in `<globals>` few default values that will allow to run the simulations with a few events.

- **scripts**: Scripts that allow to extract information from a `TRestGeant4Event` and get few results or plots out of the box. If frequently used, these scripts could be upgraded and be hosted directly at the official REST macros for Geant4, at the [geant4lib](github.com/rest-for-physics/geant4lib) repository.

- **studies**: This directory should contain ready to launch scripts directly to the NAF-IAXO batch system. We just define few variables to adjust the number of events to be launched, the isotope, the generator volume, etc. And we launch.

### Cloning this repository

``` 
git clone git@github.com:iaxo/detector-simulations.git
```

Once the repository is cloned locally we need to link the detector geometry repository as a submodule executing the following line.

```
cd detector-simulations
git submodule update --init geometry
```

