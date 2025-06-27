#!/bin/bash

fecha=$(date +%Y%m%d)
echo "inicio:$(date '+%F %T')" > main.log
for archivo in *.txt;do
    if [ -f "$archivo" ]; then
    original="${archivo%.txt}"
    mv "$archivo" "${original}_${fecha}.txt" 2>> main.log
    fi
done

echo "fin: $(date '+%F %T')" >> main.log
echo "listo manin"
echo "el use de base la practica 1"