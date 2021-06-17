#!/bin/bash

script_dir=$(dirname "$0")

export REST_N_EVENTS=1E4
export OUTPUT_DIRECTORY=/tmp/test_simulations

mkdir -p $OUTPUT_DIRECTORY

export scintillator_type=between
export primary_distribution=test

export run_number=1
export RANDOM_RESTG4_SEED=137

export scintillatorSheetMiddleMaterial=Cadmium
export scintillatorSheetMiddleThickness=2

export vetoInsertDepth=5

restG4 $script_dir/../CosmicNeutrons.rml

OUTPUT_FILE=$OUTPUT_DIRECTORY/babyIAXO_Between_${scintillatorSheetMiddleMaterial}${scintillatorSheetMiddleThickness}mm_Depth${vetoInsertDepth}mm_neutron_N${REST_N_EVENTS}_run${run_number}.root

echo $OUTPUT_FILE
ls -lht $OUTPUT_FILE
