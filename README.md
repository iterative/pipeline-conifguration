# Pipeline configuration examples 
Ideas, examples and best practices for pipeline configurations
# Patterns

|Pattern Name | Directory | Short description| 
| --- | --- | --- |
| Single `params.yaml` file  | `single-params-yaml/` | Organize configurations by stages and environments |
| Multiple `params` files  |  `multi-params-files/` | Split configurations into separate config files |
| Multiple validation datasets  |  `multi-validation-datasets/` | Use `foreach` clause to configure `evaluation` stage run |


## Install

```bash
python3 -m venv venv
echo 'export PYTHONPATH=.' >> venv/bin/activate
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```
