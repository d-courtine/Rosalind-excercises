#!/bin/bash

docker run -v $(pwd):/home/meme --user $(id -u):$(id -g) memesuite/memesuite meme -nmotifs 1 -dna test.fa