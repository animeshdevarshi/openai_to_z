# Clean Archaeological Discovery System

## 🏛️ OpenAI to Z Challenge - Checkpoint 2 Solution

A streamlined archaeological discovery system using AI-powered satellite analysis to identify Amazon archaeological sites.

## 🚀 Quick Start

```bash
# 1. Activate environment
source /Users/animeshdevarshi/pythonenvs/venv/bin/activate

# 2. Run the complete analysis
python3 main.py
```

## 📁 **Latest Results: outputs/final_results_20250525_115612/**

### 🎯 **Browse Your Results:**
- **📖 Start Here**: `outputs/final_results_20250525_115612/README.md`
- **🔍 Discoveries**: `outputs/final_results_20250525_115612/2_discoveries/`
- **🏛️ Submission**: `outputs/final_results_20250525_115612/1_submission/`
- **📸 Images**: `outputs/final_results_20250525_115612/3_processed_images/`

## ✅ **Features**

🌍 **Clean Interface**
- Simple region selection (1-4 regions available)
- Auto-archive previous runs
- Smooth execution without interruptions

🤖 **AI-Powered Analysis** 
- OpenAI o3 model with high reasoning effort
- Open discovery approach (no cultural bias)
- Multi-scale analysis: 50km → 10km → 2km

📦 **Organized Results**
- Clean 4-folder structure
- Individual discovery details with images
- Easy navigation and sharing
- **No messy temporary folders created**

## 🎯 **Results Summary**

✅ **Checkpoint 2 Compliant**
- 5+ archaeological discoveries identified
- Two independent data sources (Sentinel-2 + Sentinel-1/ALOS)
- All prompts logged and documented
- Reproducibility verified (±50m tolerance)

## 📂 **Clean Output Structure**

```
outputs/
└── final_results_YYYYMMDD_HHMMSS/
    ├── 1_submission/          # Competition files (JSON + MD)
    ├── 2_discoveries/         # Top discoveries with images
    │   ├── discovery_01/      # Individual discovery details
    │   ├── discovery_02/      # Coordinates, images, analysis
    │   └── ...
    ├── 3_processed_images/    # All satellite imagery
    │   ├── regional/          # 50km archaeological heatmaps
    │   ├── zone/              # 10km landscape analysis  
    │   └── site/              # 2km high-resolution sites
    └── 4_metadata/            # Technical analysis data
```

## 🛠️ **Additional Tools**

- `organize_existing_results.py` - Organize existing messy results  
- `cleanup_workspace.py` - Clean old folders (optional)

## 🧹 **Clean Processing**

✨ **No Messy Folders**: The system now uses temporary directories during processing and only creates the clean organized structure in `outputs/final_results_*`

🗑️ **Auto-Cleanup**: All temporary processing folders are automatically removed after completion

## 🔧 **System Requirements**

- Python 3.8+
- Google Earth Engine access
- OpenAI API key
- Virtual environment

## 📖 **Documentation**

- Individual discovery details in `2_discoveries/`
- Technical metadata in `4_metadata/`
- Complete submission files in `1_submission/`

---

**🎉 Single command to discover archaeological sites in the Amazon!**

```bash
python3 main.py
``` 