#!/usr/bin/env bash

export THEANO_FLAGS='mode=FAST_RUN,device=gpu,floatX=float32'
export OMP_NUM_THREADS=`nproc`
export PYTHONPATH="$PYTHONPATH:."