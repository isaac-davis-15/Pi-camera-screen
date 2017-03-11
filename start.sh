#!/bin/bash

sudo bash -c "python gpio_check.py"  & PIDCHECK=$!
sudo bash -c "python slide.py"
wait $PIDCHECK
