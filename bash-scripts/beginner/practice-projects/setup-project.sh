#!/bin/bash
# setup-project: Create a project directory with proper permissions and logging

set -euo pipefail

PROGNAME="$(basename "$0")"

usage() {
    echo "Usage: $PROGNAME PROJECT_NAME" >&2
    echo "Create a project directory structure with proper permissions" >&2
    exit 1
}

# Check arguments
if [ $# -eq 0 ]; then
    usage
fi

PROJECT_NAME="$1"
PROJECT_DIR="$HOME/projects/$PROJECT_NAME"
LOG_FILE="$PROJECT_DIR/setup.log"

# Function to log messages to both screen and file
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log_error() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: $1" | tee -a "$LOG_FILE" >&2
}

# Check if project already exists
if [ -d "$PROJECT_DIR" ]; then
    log_error "Project '$PROJECT_NAME' already exists at $PROJECT_DIR"
    exit 1
fi

# Create directory structure
log "Creating project: $PROJECT_NAME"
mkdir -p "$PROJECT_DIR"/{src,data,logs,scripts,output}

# Create initial files
log "Creating initial files..."
touch "$PROJECT_DIR/README.md"
touch "$PROJECT_DIR/src/main.py"
touch "$PROJECT_DIR/scripts/run.sh"
touch "$PROJECT_DIR/.gitignore"

# Set permissions
log "Setting permissions..."

# Make scripts directory executable
chmod 755 "$PROJECT_DIR/scripts"
chmod +x "$PROJECT_DIR/scripts/run.sh"

# Make data directory read/write for user only
chmod 700 "$PROJECT_DIR/data"

# Make logs directory writable
chmod 755 "$PROJECT_DIR/logs"

# Create a report of what was created
REPORT_FILE="$PROJECT_DIR/structure_report.txt"

{
    echo "Project Structure Report"
    echo "========================"
    echo "Project: $PROJECT_NAME"
    echo "Location: $PROJECT_DIR"
    echo "Created: $(date)"
    echo ""
    echo "Directory Structure:"
    echo "-------------------"
    ls -lR "$PROJECT_DIR"
    echo ""
    echo "Permissions Summary:"
    echo "-------------------"
    find "$PROJECT_DIR" -type d -exec ls -ld {} \;
    echo ""
    echo "Files Created:"
    echo "-------------"
    find "$PROJECT_DIR" -type f
} > "$REPORT_FILE"

log "Project created successfully!"
log "Location: $PROJECT_DIR"
log "Report saved to: $REPORT_FILE"

# Display summary
echo ""
echo "Summary:"
cat "$REPORT_FILE"
