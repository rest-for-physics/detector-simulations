#!/bin/bash

script_dir=$(dirname "$0")

export REST_N_EVENTS=1E3
export OUTPUT_DIRECTORY=/home/$USER/data/test/

mkdir -p $OUTPUT_DIRECTORY

export scintillator_type=between
export primary_distribution=test

export run_number=1
export RANDOM_RESTG4_SEED=1238415398

export scintillatorSheetMiddleMaterial=Cadmium
export scintillatorSheetMiddleThickness=2

export vetoInsertDepth=5

restG4 $script_dir/../CosmicNeutrons.rml

ls -lht $OUTPUT_DIRECTORY/babyIAXO_Between_${scintillatorSheetMiddleMaterial}${scintillatorSheetMiddleThickness}mm_Depth${vetoInsertDepth}mm_neutron_N${REST_N_EVENTS}_run${run_number}.root
