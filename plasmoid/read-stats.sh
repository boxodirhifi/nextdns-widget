#!/bin/sh

DATA_DIR="${XDG_DATA_HOME:-$HOME/.local/share}"
cat "$DATA_DIR/nextdns-widget/stats.json"

