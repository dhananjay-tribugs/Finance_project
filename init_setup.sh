#!/bin/bash

# Name of the conda environment
conda_env_name="Finance_project"

# Create a new conda environment with Python 3.7
conda create -y -p "${conda_env_name}" python=3.7

# Activate the conda environment
conda activate "${conda_env_name}"

# Install packages from the requirements.txt file
conda install requirements.txt
