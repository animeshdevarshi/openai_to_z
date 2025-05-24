# Archaeological Discovery System - Project Structure

**Clean organized structure for Amazon archaeological site detection**

## Overview
Multi-scale archaeological network detection system with Google Earth Engine integration, AI analysis, and full Checkpoint 2 compliance.

## Project Structure

```
solution2/
├── src/                                    # Source code (organized)
│   ├── core/
│   │   └── main_system.py                 # Main system orchestration
│   ├── data/
│   │   ├── satellite_acquisition.py       # Dual-source data loading
│   │   └── image_processor.py            # Multi-scale processing
│   ├── analysis/
│   │   ├── ai_archaeological_analyzer.py  # AI analysis with domain knowledge
│   │   └── results_manager.py            # Checkpoint 2 compliance & validation
│   └── config/
│       ├── regions.py                     # Amazon region management
│       ├── prompt_database.py            # AI prompts and knowledge base
│       └── output_paths.py               # File path organization
│
├── submissions/                           # Competition submissions (organized)
│   ├── latest/                           # Current active submission
│   │   ├── checkpoint2_submission_*.json # Latest submission
│   │   ├── checkpoint2_summary_*.md     # Latest summary
│   │   ├── latest_submission.json       # → symlink to current
│   │   ├── latest_summary.md           # → symlink to current
│   │   └── README.md                   # Latest submission info
│   ├── archive/                         # Historical submissions
│   │   ├── checkpoint2_submission_*.json # Older versions
│   │   ├── checkpoint2_summary_*.md     # Older summaries
│   │   └── README.md                   # Archive documentation
│   └── README.md                       # Submissions folder guide
│
├── outputs/                              # Generated outputs
│   ├── images/                          # Multi-scale visualization
│   │   ├── regional/                   # 50km scale images
│   │   ├── zone/                       # 10km scale images
│   │   └── site/                       # 2km scale images
│   └── analysis_results/               # Processing results
│       ├── processed_data.json         # Multi-scale processed data
│       ├── enhanced_ai_analysis_*.json # AI discovery results
│       └── pipeline_progress.json     # Resume capability
│
├── archive/                             # Archived old versions
│   ├── old_versions/                   # Old "enhanced_*" files
│   │   ├── enhanced_main_system.py
│   │   ├── enhanced_data_acquisition.py
│   │   └── ...
│   └── README.md                       # Archive documentation
│
├── main.py                             # Clean entry point
├── regions.json                        # Region configuration
├── requirements.txt                    # Dependencies
├── README.md                          # Main documentation
├── implementation_guide.md            # Technical guide
└── PROJECT_STRUCTURE.md              # This file
```

## Key Features

### 🏛️ Archaeological Focus
- **Multi-scale Analysis:** 50km → 10km → 2km progressive detection
- **Domain Knowledge:** Casarabe culture settlement patterns (Prümers et al. 2022)
- **Pattern Recognition:** Defensive earthworks, site hierarchies, spatial relationships

### 📊 Checkpoint 2 Compliance
- **Two Independent Sources:** Sentinel-2 Optical + Sentinel-1 Radar
- **Five Anomaly Footprints:** Archaeological sites with coordinates
- **Dataset IDs Logged:** COPERNICUS/S2_SR_HARMONIZED, COPERNICUS/S1_GRD
- **AI Prompts Logged:** Multi-scale analysis with archaeological context
- **Reproducibility:** ±50m tolerance verified
- **Discovery Leverage:** Pattern-based re-analysis implementation

### 🔄 System Architecture
- **Resume Capability:** Interrupted sessions can be continued
- **Clean Organization:** Logical folder structure without "enhanced_" prefixes
- **Modular Design:** Independent components for data, processing, analysis
- **Quality Assurance:** Comprehensive validation and error handling

## File Organization Principles

### Source Code (`src/`)
- **core/:** System orchestration and main pipeline
- **data/:** Data acquisition and processing components
- **analysis/:** AI analysis and results management
- **config/:** Configuration files and settings

### Submissions (`submissions/`)
- **latest/:** Current active submission ready for competition
- **archive/:** Historical submissions for development tracking
- **Symlinks:** Easy access to current submission via `latest_*.json/md`

### Outputs (`outputs/`)
- **images/:** Multi-scale visualization outputs
- **analysis_results/:** Processing and AI analysis results
- **Organized by scale:** Regional → Zone → Site progression

## Usage

### Quick Start
```bash
python main.py
```

### Step-by-Step Mode
```python
from src.core.main_system import ArchaeologicalDiscoverySystem
system = ArchaeologicalDiscoverySystem()
system.run_step_by_step_mode()
```

## Competition Readiness

The latest submission in `submissions/latest/` is ready for:
- ✅ Checkpoint 2 evaluation
- ✅ Peer review process
- ✅ Reproducibility verification
- ✅ Academic publication

## Development History

This clean structure evolved from initial "enhanced_*" naming to a professional organization suitable for academic and competition use. All old versions are preserved in `archive/old_versions/` for reference. 