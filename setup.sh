#!/bin/bash

echo "Installing Xcomments..."

mkdir -p "$HOME/.local/bin"

detect_shell_config() {
    local shell_name
    shell_name=$(basename "$SHELL")
    if [ "$shell_name" = "zsh" ]; then
        echo "$HOME/.zshrc"
    elif [ "$shell_name" = "bash" ]; then
        echo "$HOME/.bashrc"
    else
        echo "$HOME/.bashrc"
    fi
}

CONFIG_FILE=$(detect_shell_config)

if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$CONFIG_FILE" 2>/dev/null; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$CONFIG_FILE"
    echo "Added ~/.local/bin to PATH in $CONFIG_FILE"
else
    echo "~/.local/bin already in PATH in $CONFIG_FILE"
fi

export PATH="$HOME/.local/bin:$PATH"

if ! python3 -c "import pyfiglet" &> /dev/null; then
    echo "Installing pyfiglet..."
    if command -v pip3 &>/dev/null; then
        pip3 install --user pyfiglet
    elif command -v pip &>/dev/null; then
        pip install --user pyfiglet
    else
        echo "Error: pip or pip3 not found. Please install Python package manager."
        exit 1
    fi
fi

if [ ! -f xcomments.py ]; then
    echo "Error: xcomments.py not found in current directory."
    exit 1
fi

chmod +x xcomments.py
cp xcomments.py "$HOME/.local/bin/Xcomments"

echo "Installed successfully!"
echo "Restart your terminal or run:"
echo "  source $CONFIG_FILE"
echo ""
echo "Usage example:"
echo "  Xcomments -fp <file-path> -ft <file-type> [--backup]"
echo ""
echo "Supported file types (-ft):"
echo "  html     — Remove HTML comments <!-- ... -->"
echo "  css      — Remove CSS comments /* ... */"
echo "  js       — Remove JavaScript comments // ... and /* ... */"
echo "  hybrid   — For files containing HTML, CSS, and JS mixed"
echo "  python   — Remove Python comments # ..."
echo "  bash     — Remove Bash/Shell comments # ..."
echo "  c        — Remove C/C++ comments // ... and /* ... */"
echo "  java     — Remove Java comments // ... and /* ... */"
echo "  php      — Remove PHP comments // ... /* ... */ and # ..."
echo "  ruby     — Remove Ruby comments # ..."
echo "  perl     — Remove Perl comments # ..."
echo "  sql      — Remove SQL comments -- ... and /* ... */"
echo "  xml      — Remove XML comments <!-- ... -->"
echo "  json     — Remove JSON style comments (non-standard) // ... and /* ... */"
echo ""
echo "Use -h or --help to show this message anytime."
echo ""
Xcomments -h
