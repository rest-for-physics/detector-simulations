#!/bin/bash

script_dir=$(dirname "$0")

export REST_N_EVENTS=1E4

export scintillator_type=between
export primary_distribution=test

export run_number=1
export RANDOM_RESTG4_SEED=1238415398

export scintillatorSheetMiddleMaterial=Cadmium
export scintillatorSheetMiddleThickness=2

export vetoInsertDepth=5

restG4 $script_dir/../CosmicNeutrons.rml

