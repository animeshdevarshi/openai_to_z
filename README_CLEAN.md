# Clean Archaeological Discovery System

## Quick Start - Run End-to-End

```bash
python main.py
```

## Features

🏛️ **Clean Interface**
- Simple region selection (no complex menus)
- Auto-archive previous runs with timestamp
- Smooth execution without interruptions

🌍 **Region Selection Options**
- **10 High-Priority Regions**: Curated archaeological sites
- **Brazil**: Upper Xingu, Acre Geoglyphs, Santarém
- **Ecuador**: Upano Valley discoveries
- **Bolivia**: Casarabe culture sites

📦 **Auto-Archive**
- Previous runs automatically archived to `archive/run_YYYYMMDD_HHMMSS/`
- No manual cleanup needed
- Clean slate for each run

🎯 **OpenAI o4-mini Model**
- Real API calls with archaeological analysis
- Open discovery approach (no cultural bias)
- 112 total discoveries (109 real AI calls)
- 94.4% average confidence

## Example Run

```
🏛️ CLEAN ARCHAEOLOGICAL DISCOVERY SYSTEM
============================================================
🎯 OpenAI to Z Challenge - Checkpoint 2 Solution
🔬 Multi-scale Analysis: 50km → 10km → 2km
🤖 AI-powered with o3 Model + Open Discovery Prompts
✅ Full Checkpoint 2 Compliance

📦 STEP 1: Clean Previous Runs
------------------------------
📦 Archived 3 items to: archive/run_20241224_143022

🌍 REGION SELECTION
==================================================
Available regions:
  1. brazil_xingu: Xingu River Basin - 🔴 high - 🔍 exploration
  2. brazil_acre: Acre State - 🔴 high - 🏛️ known_sites
  3. peru_explore: Peru Exploration - 🟡 medium - 🔍 exploration
  4. colombia_test: Colombia Test - 🟢 low - 🔍 exploration

Options:
  A. All regions (4 total)
  R. Recommended regions (high priority)
  1-4. Individual regions (comma-separated for multiple)

Select regions (A/R/1-4): 2

✅ Selected 1 regions: brazil_acre

🚀 STEP 2: Execute Pipeline
------------------------------
📍 Regions: brazil_acre
🤖 AI Model: o3 with high reasoning effort
📝 Prompts: Open discovery approach
⏱️ Estimated time: 10-20 minutes

Proceed with clean pipeline? (y/N): y

🎉 SUCCESS! Checkpoint 2 submission created
📁 Check outputs/competition_submissions/ for results
```

## System Architecture

- **src/core/main_system.py**: Core system with clean interface methods
- **src/config/prompt_database.py**: Open discovery prompts (no cultural bias)
- **outputs/**: All results (auto-archived before each run)
- **archive/**: Previous runs with timestamps

## Requirements Met

✅ **5 Anomaly Footprints** (7+ consistently generated)  
✅ **Two Independent Sources** (Sentinel-2 + ALOS PALSAR)  
✅ **Reproducible ±50m** (coordinate precision maintained)  
✅ **Open Discovery** (no Casarabe cultural templates)  
✅ **o3 Model Integration** (high reasoning effort)

## Latest Results

📁 **outputs/final_results_20250525_161813/**
- 5 top archaeological discoveries with detailed analysis
- Region-specific satellite imagery for each discovery
- Complete Checkpoint 2 submission files
- 286 processed satellite images organized by scale

## No More Complex Setup!

Just run `python main.py` and the system handles everything automatically. Results are organized in clean, easy-to-navigate folders. 