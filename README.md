# mac-oui-lookup

[![scrape IEEE OUI data](https://github.com/ttafsir/mac-oui-lookup/actions/workflows/scrape.yml/badge.svg)](https://github.com/ttafsir/mac-oui-lookup/actions/workflows/scrape.yml)

This repository contains a Python script to download and parse Organizationally Unique Identifier (OUI) data from the IEEE website.

The OUIs are 24-bit numbers that are unique to each manufacturer of networking interfaces. They are used in the first half of a MAC address to identify the manufacturer of the device.

## Workflow

The script uses GitHub Actions to run once per day, download the latest OUI data from the IEEE, and parse it into a JSON file, mapping each OUI to the name of the manufacturer.

If the data has changed, the updated JSON file is committed and pushed back to the repository.

## Usage

To use the script on its own:

1. Ensure that Python 3.9 or higher is installed.
2. Clone the repository.
3. Run `python download_and_parse.py`.
4. The resulting `latest_oui_lookup.json` file will contain the latest OUI data in JSON format.

## Contributing

Contributions are welcome! Please open an issue if you encounter any problems, or a pull request if you make an improvement.

## License

This project is licensed under the MIT License.
