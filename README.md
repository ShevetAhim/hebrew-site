# Shevet Ahim's hebrew website

# Development

```
pipenv sync
pipenv run make regenerate &
pipenv run make serve &
```

# Deployment

The [https://www.shevet-ahim.co.il](www.shevet-ahim.co.il) domain is managed by LightHost.
It points to [CloudFlare](https://dash.cloudflare.com/1a71ca20d51f32031042d31177c144fe/shevet-ahim.co.il) for SSL, which in turn point to GitHub Pages, where the site is deployed.

Deployment is done automatically with every push to GitHub by [CodeShip](https://app.codeship.com/projects/304815).
Custom deploy script:

```
git fetch origin gh-pages:gh-pages
pip install pipenv
pipenv sync --python 3.6
pipenv run make github
```

Don't forget to add CodeShip's public ssh key to the repo's deploy keys, to make pushing works.
