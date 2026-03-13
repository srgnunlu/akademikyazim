#!/usr/bin/env bash
# TezAtlas — Startup Banner
# Requires: figlet, lolcat

clear

# 1. Dependency Check
if ! command -v figlet &>/dev/null || ! command -v lolcat &>/dev/null; then
    echo -e "\033[1mTezAtlas — Agentic Academic Workflow Framework\033[0m"
    echo "To see the beautiful colorized 3D banner, please install dependencies:"
    echo "Ubuntu/Debian: sudo apt install figlet lolcat"
    echo "macOS: brew install figlet lolcat"
    echo ""
    echo -e "Type \033[1m/tezatlas\033[0m to begin or resume"
    exit 0
fi

# 2. Setup 3D Font
FONT_DIR="${HOME}/.local/share/fonts"
FONT_FILE="${FONT_DIR}/3d.flf"

if [ ! -f "$FONT_FILE" ]; then
    mkdir -p "$FONT_DIR"
    # Silently download the 3D font if missing
    curl -sL https://raw.githubusercontent.com/xero/figlet-fonts/master/3d.flf -o "$FONT_FILE"
fi

# 3. Print 3D Banner Title with Lolcat
if [ -f "$FONT_FILE" ]; then
    figlet -f "$FONT_FILE" "TezAtlas" | lolcat
else
    figlet -f standard "TezAtlas" | lolcat
fi

# 4. Project Subtitle & Author
echo "" | lolcat
printf "  \033[1m%-40s\033[0m\n" "Agentic Academic Workflow Framework" | lolcat
printf "  %-40s\n" "tezatlas.com" | lolcat
echo "" | lolcat

# Separator
printf '%0.s─' {1..60} | lolcat
echo "" | lolcat

# 5. Core Features & Capabilities
printf "  %-4s %-30s %s\n" "📄" "Doctoral / Master's Thesis" "8 phases" | lolcat
printf "  %-4s %-30s %s\n" "📝" "Journal Article" "7 phases" | lolcat
printf "  %-4s %-30s %s\n" "🎤" "Conference Paper" "6 phases" | lolcat
printf "  %-4s %-30s %s\n" "📊" "Technical / Research Report" "2-5 phases" | lolcat

echo "" | lolcat

printf "  %-20s %s\n" "🧠 AI Engine:" "Oracle, Guardian, FIRE, Provenance" | lolcat
printf "  %-20s %s\n" "🔒 Iron Rules:" "9 immutable source/citation constraints" | lolcat

echo "" | lolcat
printf '%0.s─' {1..60} | lolcat
echo "" | lolcat

# 6. Author Signature & Start Command
printf "  Built by Tarık İsmet ALKAN\n" | lolcat
echo "" | lolcat
printf "  Type \033[1m/tezatlas\033[0m to begin or resume\n"
echo ""
