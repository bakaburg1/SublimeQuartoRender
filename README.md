# SublimeQuartoRender

SublimeQuartoRender is a Sublime Text package that provides easy rendering of Quarto documents directly from within the editor.

## Features

- Render Quarto documents (.qmd files) with a single command
- Accessible via Command Palette or custom key binding
- Displays rendering status and error messages

## Installation

<!-- ### Via Package Control (Recommended)

1. Open Sublime Text
2. Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux) to open the Command Palette
3. Type `Package Control: Install Package` and press Enter
4. Search for "SublimeQuartoRender" and press Enter to install 

### Manual Installation-->

1. Navigate to your Sublime Text Packages directory:
   - Windows: `%APPDATA%\Sublime Text\Packages/User`
   - macOS: `~/Library/Application Support/Sublime Text/Packages/User`
   - Linux: `~/.config/sublime-text/Packages/User`
2. Download the following file in the folder: `quarto_render.py`, `Quarto.sublime-commands`

## Usage

1. Open a Quarto document (.qmd file) in Sublime Text
2. Use one of the following methods to render the document:
   - Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux), type "Quarto: Render Document", and press Enter

## Requirements

- Sublime Text 3 or 4
- Quarto CLI installed and accessible in your system PATH

## Key Binding

1. Go to `Preferences > Key Bindings`
2. Add the following to your User key bindings, replacing `<your_preferred_key_binding>` e.g. `ctrl/cmd + alt + Q`, with your desired key combination:

```json
{ "keys": ["<your_preferred_key_binding>"], "command": "quarto_render" }
```

## Troubleshooting

If you encounter issues:

1. Ensure Quarto is properly installed and accessible from the command line
2. Check the Sublime Text console (`` Ctrl+` ``) for any error messages
3. Make sure your .qmd file is saved before attempting to render

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any problems or have any suggestions, please [open an issue](https://github.com/bakaburg1/SublimeQuartoRender/issues) on GitHub.

## Acknowledgements

- This package was inspired by the need for better Quarto integration in Sublime Text
- Thanks to the Quarto team for their excellent documentation