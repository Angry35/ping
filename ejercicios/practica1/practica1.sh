#!/bin/bash
fecha=$(date +%Y%m%d)

for archivo in *.txt;do
    if [ -f "$archivo" ]; then
    original="${archivo%.txt}"
    mv "$archivo" "${original}_${fecha}.txt"
    fi
done
echo "listo manin"