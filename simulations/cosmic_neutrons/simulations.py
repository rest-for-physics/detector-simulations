#!/usr/bin/env python3

import os
import sys
import time
import subprocess
import random

import numpy as np

from datetime import datetime
from datetime import timedelta

# https://stackoverflow.com/questions/11269575/how-to-hide-output-of-subprocess-in-python-2-7
from subprocess import Popen, PIPE, STDOUT
try:
    from subprocess import DEVNULL
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')

print("*"*200)
# root paths
dir_path = os.path.realpath(__file__)
dir_path = "/".join(dir_path.split("/")[:-1])
assert os.path.isdir(dir_path)
print(f"Main directory: {dir_path}")

# slurm logs
logs_dir = os.path.join(dir_path, "logs")
os.makedirs(logs_dir, exist_ok=True)
assert os.path.isdir(logs_dir)
for file in os.listdir(logs_dir):
    # only delete .sh files
    if file.split(".")[-1] == "sh":
        os.remove(os.path.join(logs_dir, file))

print(f"Slurm logs directory: {logs_dir}")
# jobs dir (scripts to launch simulations)
jobs_dir = os.path.join(dir_path, "jobs")
os.makedirs(jobs_dir, exist_ok=True)
assert os.path.isdir(jobs_dir)
for file in os.listdir(jobs_dir):
    # only delete .o files
    if file.split(".")[-1] == "o":
        os.remove(os.path.join(jobs_dir, file))

print(f"Jobs directory (bash scripts to launch simulations): {jobs_dir}")

# simulation RML file
rml_file = os.path.join(dir_path, "CosmicNeutrons.rml")
assert os.path.isfile(rml_file)
print(f"restG4 RML file: {rml_file}")
print("*"*200)

# print REST info
rest_path = os.path.abspath(os.environ.get("REST_PATH"))
restG4_path = os.path.join(rest_path, "bin/restG4")
print(f"Found RestG4 at {restG4_path}")
print("*"*200)


configurations = dict()
configurations["between"] = [
    {
    "scintillatorSheetMiddleMaterial": "Cadmium",
    "scintillatorSheetMiddleThickness": 2,
    "vetoInsertDepth": 5,
    },  
    {
    "scintillatorSheetMiddleMaterial": "Cadmium",
    "scintillatorSheetMiddleThickness": 2,
    "vetoInsertDepth": 50,
    },   
    {
    "scintillatorSheetMiddleMaterial": "Cadmium",
    "scintillatorSheetMiddleThickness": 2,
    "vetoInsertDepth": 110,
    },    
    {
    "scintillatorSheetMiddleMaterial": "Cadmium",
    "scintillatorSheetMiddleThickness": 2,
    "vetoInsertDepth": 150,
    },    
    {
    "scintillatorSheetMiddleMaterial": "Cadmium",
    "scintillatorSheetMiddleThickness": 2,
    "vetoInsertDepth": 190,
    },
]
configurations["single"] = [
    {
    "scintillatorSheetLastMaterial": "Vacuum",
    "scintillatorSheetLastThickness": 5,
    },
    {
    "scintillatorSheetLastMaterial": "Lead",
    "scintillatorSheetLastThickness": 20,
    },
    {
    "scintillatorSheetLastMaterial": "Lead",
    "scintillatorSheetLastThickness": 50,
    },
    {
    "scintillatorSheetLastMaterial": "Lead",
    "scintillatorSheetLastThickness": 100,
    },
    {
    "scintillatorSheetLastMaterial": "Lead",
    "scintillatorSheetLastThickness": 200,
    },
]
configurations["double"] = [
    {
    "scintillatorSheetMiddleMaterial": "Cadmium",
    "scintillatorSheetMiddleThickness": 2,
    "scintillatorSheetLastMaterial": "Vacuum",
    "scintillatorSheetLastThickness": 50,
    },
    {
    "scintillatorSheetMiddleMaterial": "Cadmium",
    "scintillatorSheetMiddleThickness": 5,
    "scintillatorSheetLastMaterial": "Vacuum",
    "scintillatorSheetLastThickness": 50,
    },    
    {
    "scintillatorSheetMiddleMaterial": "StainlessSteel",
    "scintillatorSheetMiddleThickness": 5,
    "scintillatorSheetLastMaterial": "Vacuum",
    "scintillatorSheetLastThickness": 50,
    },    
    {
    "scintillatorSheetMiddleMaterial": "Cadmium",
    "scintillatorSheetMiddleThickness": 2,
    "scintillatorSheetLastMaterial": "Lead",
    "scintillatorSheetLastThickness": 50,
    }, 
    {
    "scintillatorSheetMiddleMaterial": "Cadmium",
    "scintillatorSheetMiddleThickness": 5,
    "scintillatorSheetLastMaterial": "Lead",
    "scintillatorSheetLastThickness": 50,
    }, 
    {
    "scintillatorSheetMiddleMaterial": "StainlessSteel",
    "scintillatorSheetMiddleThickness": 5,
    "scintillatorSheetLastMaterial": "Lead",
    "scintillatorSheetLastThickness": 50,
    }, 
    {
    "scintillatorSheetMiddleMaterial": "Cadmium",
    "scintillatorSheetMiddleThickness": 2,
    "scintillatorSheetLastMaterial": "Lead",
    "scintillatorSheetLastThickness": 100,
    }, 
    {
    "scintillatorSheetMiddleMaterial": "StainlessSteel",
    "scintillatorSheetMiddleThickness": 5,
    "scintillatorSheetLastMaterial": "Lead",
    "scintillatorSheetLastThickness": 100,
    }, 
    {
    "scintillatorSheetMiddleMaterial": "Cadmium",
    "scintillatorSheetMiddleThickness": 5,
    "scintillatorSheetLastMaterial": "Lead",
    "scintillatorSheetLastThickness": 100,
    }, 
    {
    "scintillatorSheetMiddleMaterial": "Cadmium",
    "scintillatorSheetMiddleThickness": 2,
    "scintillatorSheetLastMaterial": "Lead",
    "scintillatorSheetLastThickness": 200,
    }, 
    {
    "scintillatorSheetMiddleMaterial": "StainlessSteel",
    "scintillatorSheetMiddleThickness": 5,
    "scintillatorSheetLastMaterial": "Lead",
    "scintillatorSheetLastThickness": 200,
    }, 
    {
    "scintillatorSheetMiddleMaterial": "Cadmium",
    "scintillatorSheetMiddleThickness": 5,
    "scintillatorSheetLastMaterial": "Lead",
    "scintillatorSheetLastThickness": 200,
    }, 
]
configurations["triple"] = configurations["double"]
configurations["quad"] = configurations["double"]

global_configuration = {
    "primary_distribution": "test",
}

n_events_per_job = "1E3"
n_jobs = 10

i = 0
processes = []
#for scintillator_type in ["single", "double", "triple", "quad"]:
for scintillator_type in ["between"]:

    for environment in configurations[scintillator_type]:
        date_time = datetime.now()
        date_time += timedelta(seconds=60)

        for k in range(n_jobs):

            i += 1
            simulation_type=f"biaxo_{scintillator_type}_{n_events_per_job}"
            log_file = os.path.join(logs_dir, f"{simulation_type}_{i}.o")
            bash_script = f"""#!/bin/bash
                #SBATCH -J {simulation_type}
                #SBATCH -o {log_file}
                #SBATCH -p bifi
                #SBATCH --mem-per-cpu=2G
                #SBATCH --time=1-12:00:00
                #SBATCH --ntasks=1
                #SBATCH --begin={date_time.strftime("%H:%M-%m/%d/%y")}
                """
            bash_script += f"export REST_N_EVENTS={n_events_per_job}\n"
            bash_script += f"export scintillator_type={scintillator_type}\n"

            bash_script += f"export run_number={k+1}\n"
            bash_script += f"export RANDOM_RESTG4_SEED={random.randint(1, 2147483647)}\n"

            for key, value in environment.items():
                bash_script += f"export {key}={value}\n"

            for key, value in global_configuration.items():
                bash_script += f"export {key}={value}\n"

            bash_script += f"{restG4_path} {rml_file}\n"

            job_file = os.path.join(jobs_dir, f"{simulation_type}_{i}.sh")
            with open(job_file, "w") as f:
                for line in bash_script.split("\n"):
                    if line.strip() == "":
                        continue
                    f.write(line.lstrip(" ") + "\n")

            #subprocess.Popen(["sbatch", job_file])



