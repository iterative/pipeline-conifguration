#!/usr/bin/env bash
PARAMS=$(sed 's/file: //' params.yaml)
echo "using params file $PARAMS"
echo "contents: $(cat $PARAMS)"
