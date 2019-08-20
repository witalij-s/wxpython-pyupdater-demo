#!/usr/bin/env bash
VERSION=$1

if [ -z "$VERSION" ]
then
    echo "No version paramter set."
    exit 1
fi

pyupdater build --app-version=$VERSION main.spec && \
    pyupdater pkg --process --sign
