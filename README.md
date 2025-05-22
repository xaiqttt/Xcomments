# Xcomments

**Xcomments** is a clean and powerful CLI tool that removes comments from various source code files. Built for developers who want fast, no-nonsense code cleanup across many languages — including support for hybrid files (HTML/CSS/JS in one).

---

## Features

- Remove comments from multiple languages
- Hybrid file support (e.g., HTML with inline CSS & JS)
- Backup option before cleaning
- Clean CLI interface with ASCII banner
- Works on both Termux and standard Linux terminals
- ZSH and BASH compatible

---

## Installation

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/Xcomments.git
cd Xcomments
```

### 2. Run Setup

```bash
chmod +x setup.sh
./setup.sh
```

Then follow the on-screen instructions to add it to your shell's PATH.

---

## Usage

```bash
Xcomments -fp <file-path> -ft <file-type> [--backup]
```

### Example

```bash
Xcomments -fp index.html -ft html --backup
```

---

## Supported File Types

| File Type | Description                                |
|-----------|--------------------------------------------|
| html      | `<!-- ... -->`                             |
| css       | `/* ... */`                                |
| js        | `// ...` and `/* ... */`                   |
| hybrid    | HTML + CSS + JS combined in one file       |
| python    | `# ...`                                     |
| bash      | `# ...`                                     |
| c         | `// ...` and `/* ... */`                   |
| cpp       | same as C                                   |
| java      | `// ...` and `/* ... */`                   |
| php       | `//`, `#`, and `/* ... */`                 |
| ruby      | `# ...`                                     |
| perl      | `# ...`                                     |
| sql       | `-- ...` and `/* ... */`                   |
| xml       | `<!-- ... -->`                             |
| json      | `// ...` and `/* ... */` (non-standard)    |

---

## Help Menu

```bash
Xcomments -h
```

This shows the usage instructions and supported file types.

---

## Compatibility

- Termux (Android)
- Linux distros (Ubuntu, Debian, Arch, Kali, etc.)
- Supports ZSH and BASH automatically

---

## Author

Created with purpose by **0X4P0R41**
