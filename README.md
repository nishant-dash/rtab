# rt
A simple formatting cli that converts json, yaml and csv into tables using the [rich](https://github.com/Textualize/rich) library

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
```