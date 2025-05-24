# 🏛️ Enhanced Amazon Archaeological Discovery System

**OpenAI to Z Challenge - Checkpoint 2 Complete Solution**

Multi-scale archaeological network detection in the Amazon using dual-source satellite analysis and AI interpretation.

## 🎯 **What This System Does**

- **Discovers pre-Columbian archaeological sites** in the Amazon rainforest
- **Multi-scale analysis**: 50km → 10km → 2km progressive zoom
- **Dual-source data**: Optical (Sentinel-2) + Radar (Sentinel-1/PALSAR)
- **AI-powered interpretation** with archaeological domain knowledge
- **Full Checkpoint 2 compliance** for OpenAI competition
- **Reproducible methodology** with ±50m tolerance

## 🚀 **COMPLETE SETUP FROM SCRATCH**

### **Step 1: System Requirements**

```bash
# Python 3.8+ required
python --version  # Should be 3.8 or higher

# Operating Systems supported:
# - macOS (recommended)
# - Linux Ubuntu/Debian
# - Windows 10/11 with WSL
```

### **Step 2: Install Dependencies**

```bash
# Create virtual environment (recommended)
python -m venv archaeological_env
source archaeological_env/bin/activate  # On Windows: archaeological_env\Scripts\activate

# Install all dependencies
pip install -r requirements.txt
```

### **Step 3: Google Earth Engine Setup**

This is **CRITICAL** - without this, the system won't work:

```bash
# 1. Go to: https://earthengine.google.com/
# 2. Sign up with your Google account
# 3. Wait for approval (usually 1-2 days)
# 4. Once approved, authenticate:

import ee
ee.Authenticate()  # This will open browser for authentication
ee.Initialize()    # This confirms it works
```

**⚠️ IMPORTANT**: You MUST complete Google Earth Engine signup and get approved before proceeding.

### **Step 4: OpenAI API Setup (Optional)**

For real AI analysis (current version uses mock responses for testing):

```bash
# Get OpenAI API key from: https://platform.openai.com/api-keys
# Add to your environment:

# Option 1: Environment variable
export OPENAI_API_KEY="your-api-key-here"

# Option 2: Keyring (more secure)
python -c "import keyring; keyring.set_password('openai', 'api_key', 'your-api-key-here')"

# Option 3: .env file
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

### **Step 5: Download the Complete System**

All required files:

**Core System Files:**
- `enhanced_main_system.py` - Main orchestrator
- `simple_region_config.py` - Region configurations  
- `enhanced_data_acquisition.py` - Satellite data loading
- `enhanced_data_processor.py` - Image processing & analysis
- `enhanced_ai_analyzer.py` - AI interpretation
- `enhanced_results_manager.py` - Checkpoint 2 compliance
- `output_config.py` - Output organization

**Configuration Files:**
- `simple_regions.json` - Available research regions
- `requirements.txt` - Python dependencies
- `README.md` - This setup guide

### **Step 6: Create Directory Structure**

```bash
# The system will auto-create these, but you can pre-create:
mkdir -p outputs/images/regional
mkdir -p outputs/images/zones  
mkdir -p outputs/images/sites
mkdir -p outputs/analysis_results
mkdir -p outputs/submissions
```

### **Step 7: Test Installation**

```bash
# Quick test - should show system status
python enhanced_main_system.py

# You should see:
# 🏛️ Enhanced Amazon Archaeological Discovery System
# 🎯 OpenAI to Z Challenge - Checkpoint 2 Solution
# ✅ All components initialized successfully!
```

## 🎮 **HOW TO RUN**

### **Option 1: Complete Automatic Pipeline (Recommended)**

```bash
python enhanced_main_system.py

# Select: "1. Run complete pipeline automatically"
# Choose: 3 regions (recommended for first run)
# Confirm: "y" to proceed
# 
# ⏱️ Takes 15-30 minutes
# ✅ Produces complete Checkpoint 2 submission
```

### **Option 2: Step-by-Step Mode (For Learning)**

```bash
python enhanced_main_system.py

# Select: "2. Step-by-step interactive mode"
# Then run each step individually:
# 1. Authentication
# 2. Load Data  
# 3. Processing
# 4. AI Analysis
# 5. Create Submission
```

## 📊 **EXPECTED OUTPUTS**

After successful run, you'll have:

```
outputs/
├── images/
│   ├── regional/        # 50km scale network maps
│   ├── zones/          # 10km scale site detection  
│   └── sites/          # 2km scale detailed sites
├── analysis_results/
│   ├── processed_data.json
│   ├── enhanced_ai_analysis_*.json
│   └── ai_analyses.json
└── submissions/
    ├── checkpoint2_submission_*.json  # Competition submission
    └── checkpoint2_summary_*.md       # Human readable report
```

## 🎯 **QUICK START FOR ABSOLUTE BEGINNERS**

**If you're completely new to this:**

1. **Install Python 3.8+** from python.org
2. **Download all the system files** to one folder
3. **Open terminal/command prompt** in that folder  
4. **Run**: `pip install -r requirements.txt`
5. **Sign up for Google Earth Engine** (link above)
6. **Wait for approval** (1-2 days)
7. **Run**: `python enhanced_main_system.py`
8. **Select option 1** (complete pipeline)
9. **Wait 15-30 minutes** for results

## 🛠️ **TROUBLESHOOTING**

### **Common Issues:**

**1. "Google Earth Engine not authenticated"**
```bash
# Solution: Complete GEE signup and run:
import ee; ee.Authenticate(); ee.Initialize()
```

**2. "No module named 'geemap'"**
```bash
# Solution: Install dependencies:
pip install -r requirements.txt
```

**3. "Bolivia region failed"**
```bash
# Normal - Bolivia removed due to data issues
# System will automatically use other regions
```

**4. "AI analysis returned 0 discoveries"**
```bash
# Normal - system uses mock AI responses for testing
# Real OpenAI integration available with API key
```

## 🏆 **CHECKPOINT 2 COMPLIANCE**

This system automatically ensures:

- ✅ **Two independent data sources** (Sentinel-2 + Sentinel-1)
- ✅ **Five anomaly footprints** (archaeological sites)
- ✅ **Dataset IDs logged** (automatic tracking)
- ✅ **OpenAI prompts logged** (scale-specific prompts)
- ✅ **Reproducibility verified** (±50m tolerance)
- ✅ **Discovery leverage** (pattern-based re-prompting)

## 📚 **SCIENTIFIC BACKGROUND**

**Based on:**
- Prümers et al. 2022 - Casarabe culture settlement networks
- Multi-scale remote sensing archaeology
- Amazon pre-Columbian urban planning
- Defensive earthwork analysis

**Method:**
- Progressive scale analysis (50km → 10km → 2km)
- Archaeological probability mapping
- Geometric pattern recognition
- AI-assisted site classification

## 🤝 **SUPPORT**

**If you get stuck:**

1. Check Google Earth Engine is properly authenticated
2. Verify all dependencies installed: `pip list`
3. Run in step-by-step mode for detailed debugging
4. Check system status: option 4 in main menu

## 🎉 **SUCCESS CRITERIA**

**You know it worked when you see:**

```
🎉 CHECKPOINT 2 COMPLIANCE: ✅ PASS
✅ Submission package ready!
📄 Files created:
   • checkpoint2_submission_*.json
   • checkpoint2_summary_*.md
```

**This means you have a complete, competition-ready archaeological discovery submission!**

---

*Ready to discover lost civilizations in the Amazon? Let's go! 🏛️* 