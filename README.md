# ![rt_logo](/png/rt_logo.png)
A simple formatting cli that converts json, yaml or csv into tables using the [rich](https://github.com/Textualize/rich) library

rt stands for Rich Tabulator

# Installation
```bash
sudo snap install rt
```

# Usage
```bash
something --format json | rt -j
something --format yaml | rt -y
something --format csv | rt -c
```

## You can get creative with this and use it to pretty print various existing tools
### NOTE: This is meant to be an additive to existing awesome tools like `jq`, `yq`, etc...

- Using with openstack cli
```bash
openstack server list -fjson | rt -j
openstack server list -fcsv | rt -c
```

For example:
- without rt
![without_rt](/png/without_rt.png)

- with rt
![with_rt](/png/with_rt.png)