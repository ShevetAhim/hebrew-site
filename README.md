# Shevet Ahim's hebrew website

# Development

```
pip-sync
make regenerate &
make serve &
```

# Deployment

The [https://www.shevet-ahim.co.il](www.shevet-ahim.co.il) domain is managed by LightHost.
It points to [CloudFlare](https://dash.cloudflare.com/1a71ca20d51f32031042d31177c144fe/shevet-ahim.co.il) for SSL, which in turn point to GitHub Pages, where the site is deployed.

To deploy run

```
make github
```
