########################################
# Library of Baby-IAXO simulations- paths
########################################
export BabyIAXO_PATH="$HOME/GitLab/BabyIAXO" ## Change this to your GitLab source directory.
export BabyIAXO_SIMPATH="$BabyIAXO_PATH/iaxo-simulations/simulations/background"
export BabyIAXO_GEOMETRY="$BabyIAXO_PATH/iaxo-geometry/BabyIAXO/reference/Setup.gdml"

########################################
# Library of Baby-IAXO simulations- variables
########################################
#export GAS="Argon_ISO"
#export PRESSURE="4.0" #in bar
#export QUENCHER="0.02" #fraction of 1
export Nevents="1000000"

#####################################################################################
## FullChain simulations
## Isotope options Co60, K40, Cs137, Th232, U238
#####################################################################################
export REST_ISOTOPE="U238" #More options 

#####################################################################################
## Volume options: AGET, Capacitor, Resistor, Diode.


#####################################################################################
##Full Chain From Point Source
#####################################################################################
export POS_X="0"
export POS_Y="7"
export POS_Z="20"
restG4 $BabyIAXO_SIMPATH/IsotopePoint.rml


##############

###### Add other simulation definitions here

