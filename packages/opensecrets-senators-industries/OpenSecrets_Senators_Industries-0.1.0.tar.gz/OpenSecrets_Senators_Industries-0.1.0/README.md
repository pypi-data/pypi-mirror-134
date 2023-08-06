# OpenSecrets_Senators_Industries

Python package that allows users to view information about their senators and the industries that fund them.

## Installation

```bash
$ pip install OpenSecrets_Senators_Industries
```

## Usage

```
from OpenSecrets_Senators_Industries import OpenSecrets_Senators_Industries

ProPublica = ProPublicaAPIKey('insert ProPublica API Key here')
OpenSecrets = OpenSecretsAPIKey('insert OpenSecrets API Key here')

top_20_industries_ids(year)
ProPublica.senate_members(congress_sitting)
OpenSecrets.top_senators_each_industry(propublica_api_key, industry_id, congress_sitting)

```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`OpenSecrets_Senators_Industries` was created by Jade Qiu. It is licensed under the terms of the MIT license.

## Credits

`OpenSecrets_Senators_Industries` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
