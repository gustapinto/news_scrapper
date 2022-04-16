#!/bin/sh

# Starts the daemon to run dagster schedules and scanners
nohup dagster-daemon run &
dagit -h 0.0.0.0 -p 3000
