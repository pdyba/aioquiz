#!/usr/bin/env bash
python -m pytest --cov=. --cov-config .coveragerc --cov-report term --cov-report html:cov_html tests