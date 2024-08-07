#!/bin/bash

# Directory containing the SVG files (change this to your directory)
DIRECTORY="./"

# Iterate over all .svg files in the directory
for svg_file in "$DIRECTORY"/*.svg
do
  # Extract the base name of the file (without the extension)
  base_name=$(basename "$svg_file" .svg)
  
  # Define the output PDF file name
  pdf_file="$DIRECTORY/$base_name.pdf"
  
  # Convert the SVG file to a PDF file
  rsvg-convert -f pdf -o "$pdf_file" "$svg_file"
  
  echo "Converted $svg_file to $pdf_file"
done
