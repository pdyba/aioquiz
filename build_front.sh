#!/usr/bin/env bash
rm -r ./static/dist/*
rm static/js/templates.js
npm run build && rm static/js/templates.js static/dist/bundle.js &&echo "Success"
