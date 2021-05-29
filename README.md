# Sarcophagus Website

Public facing site built with bootstrap 4 and jekyll hosted on github pages.

## Build for Arweave

The script `arweave_build.py` creates a build for deploying the Jekyll website on the permaweb.

Requirements for running the script are:

- Python v3+
- Jekyll
- [arweave-deploy](https://www.npmjs.com/package/arweave-deploy) (npm package)

For the actual deploy you also need an `arweave keyfile`.

Depending on your environment settings for your Python alias you can run the script with:

```
python ./arweave_build.py
```

or with:

```
python3 ./arweave_build.py
```


