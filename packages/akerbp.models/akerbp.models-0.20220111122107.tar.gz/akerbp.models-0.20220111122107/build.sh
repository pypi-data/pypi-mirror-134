#!/usr/bin/env bash
#
# Package version number relies on git tags
# Building logic enables building in dev and then using the same version in test
# Setup.py reads tags to create the version label
if [ "$BITBUCKET_REPO_FULL_NAME" = "akerbp/models" ] || [ "$ENV" = "dev" ]
echo "Build script for akerbp.models package"
then
    if [ "$ENV" != "dev" ]
    then
        echo "Install build dependencies"
        pip install twine==3.3.0
    fi

    # Tag if untagged
    tag=$(git describe --tags --exact-match);
    if [ -z "$tag" ]
    then
        new_tag=True
        echo "Tag release"
        tag=$(date '+%Y%m%d%H%M%S');
        commit=$(git rev-parse --short HEAD);
        git tag $tag $commit
        git push origin --tags
    else
        echo "Use existing tag: $tag"
    fi

    # Build and upload if new tag was applied (or prod)
    if [ "$new_tag" ] || [ "$ENV" = "prod" ]
    then
        echo "Build package"
        python setup.py sdist bdist_wheel
        echo "Upload package"
        python -m twine upload \
            --disable-progress-bar \
            --non-interactive \
            --repository akerbp.models \
            dist/*
    else
        echo "Won't build and upload!"
    fi

    if [ "$ENV" = "dev" ]
    then
        echo "Clean up!"
        rm -fR build/ dist/ src/akerbp.models.egg-info/
    fi

fi
