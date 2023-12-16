<h1 align="center">
  <img src="./png/rtab_logo.png" alt="rtab" width="60px">
  <br />
  rtab - Rich Tabulator
</h1>

<p align="center">A simple formatting cli that converts json, yaml or csv into tables using the <a href="https://github.com/Textualize/rich">rich</a> library.</p>


# Installation &nbsp;&nbsp;&nbsp;&nbsp; [![rich-tab](https://snapcraft.io/rich-tab/badge.svg)](https://snapcraft.io/rich-tab)

```bash
sudo snap install rich-tab --edge
```

# Usage
```bash
something --format json | rtab -j
something --format yaml | rtab -y
something --format csv | rtab -c
```

### You can get creative with this and use it to pretty print various existing tools

> [!NOTE]
> This is meant to be an additive to existing awesome tools like `jq`, `yq`, etc...

- Using with openstack cli
```bash
openstack server list -fjson | rtab -j
openstack server list -fcsv | rtab -c
```

For example:
- without rtab
![without_rtab](/png/without_rtab.png)

- with rtab
![with_rtab](/png/with_rtab.png)


# Building and Dev
```bash
# to build the snap
make build

# to install a local version of the snap
sudo snap install rtab.snap --dangerous

# unittests, linting etc...
make lint
make unittests
```

<br>

<h1 align="center">
<a href="https://snapcraft.io/rich-tab">
  <img alt="Get it from the Snap Store" src="https://snapcraft.io/static/images/badges/en/snap-store-black.svg" />
</a>
</h1>
