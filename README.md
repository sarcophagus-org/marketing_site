# Sarcophagus Website

Public facing site built with bootstrap 4 and jekyll hosted on github pages

# Deploying to Arweave

Be sure to set up the arweave CLI with your keyfile beforehand ([see here](https://github.com/ArweaveTeam/arweave-deploy)).

```
docker run --rm -it --volume="$PWD:/srv/jekyll" \
  --volume="$PWD/vendor/bundle:/usr/local/bundle" \
  --env JEKYLL_ENV=production jekyll/jekyll:3.8 jekyll build

arweave deploy-dir _site
```
