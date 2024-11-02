#!/bin/bash

# Create the main directories
mkdir -p bin lib conf src data var srv apps modules deps env

# Create subdirectories under 'src'
mkdir -p src/includes src/tests src/app

# Create subdirectories under 'data'
mkdir -p data/database data/docs data/languages data/media

# Create subdirectories under 'var'
mkdir -p var/build var/cache var/logs var/temp var/uploads var/proc

# Create subdirectories under 'env'
mkdir -p env/users env/sys

# Create a directory for your specific system or app (replace 'your_app_name' with your desired name)
mkdir -p env/your_app_name

echo "Directory structure created successfully!"