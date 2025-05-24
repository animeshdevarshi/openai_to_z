# Submissions Folder

This folder contains all competition submission files for the OpenAI to Z Challenge.

## Current Structure

```
submissions/
├── latest/                 # Latest/active submissions
├── archive/               # Historical submissions
└── README.md             # This file
```

## Submission Types

### Checkpoint 2 Submissions
- **checkpoint2_submission_*.json** - Competition submission files (JSON format)
- **checkpoint2_summary_*.md** - Human-readable summary reports (Markdown format)

## File Naming Convention
- Format: `checkpoint2_submission_YYYYMMDD_HHMMSS.json`
- Example: `checkpoint2_submission_20250524_195959.json`

## Latest Submission
The most recent and highest quality submission should be in the `latest/` folder.

## Validation Status
All submissions in this folder should be:
- ✅ Checkpoint 2 compliant
- ✅ Contains 5+ anomaly footprints
- ✅ Two independent data sources verified
- ✅ OpenAI prompts logged
- ✅ Reproducibility verified within ±50m

## Usage
The system automatically saves submissions here. The latest submission can be found by checking timestamps or in the `latest/` folder. 