#!/bin/bash

docker run -v $(pwd):/home/meme --user $(id -u):$(id -g) memesuite/memesuite meme ${1} -protein -oc . -nostatus -time 14400 -mod zoops -nmotifs 3 -objfun classic -markov_order 0 -oc meme_res
