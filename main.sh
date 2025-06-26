#!/bin/bash  
documento="dominio.txt"

while IFS= read -r dominio; do
  if ping -c 1 "$dominio" > /dev/null 2>&1; then
    echo "$dominio esta activo."
  else
    echo "$dominio no esta activo."
    fi
    done < "$documento"
    echo "Proceso completado."
    