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

### **Step 5: Organized System Structure**

**Core System Files (src/ directory):**
- `main.py` - Main orchestrator
- `src/config/region_config.py` - Region configurations  
- `src/data/gee_data_loader.py` - Satellite data acquisition
- `src/data/image_processor.py` - Image processing & analysis
- `src/analysis/ai_archaeological_analyzer.py` - AI interpretation
- `src/analysis/results_manager.py` - Checkpoint 2 compliance
- `src/config/output_paths.py` - Output organization

**Configuration Files:**
- `regions.json` - Available research regions
- `requirements.txt` - Python dependencies
- `README.md` - This setup guide

**Organized Structure:**
```
src/
├── config/          # Configuration modules
├── data/           # Data acquisition & processing
└── analysis/       # AI analysis & results management

outputs/            # Generated outputs (organized)
├── archaeological_analysis/
│   ├── ai_responses/      # AI analysis results
│   ├── discoveries/       # Archaeological discoveries
│   └── prompts_database/ # Prompt tracking
├── competition_submissions/
└── satellite_imagery/

submissions/        # Competition submissions
├── latest/        # Current active submission
└── archive/       # Historical submissions
```

### **Step 6: Create Directory Structure**

```bash
# The system will auto-create these, but you can pre-create:
mkdir -p outputs/archaeological_analysis/{ai_responses,discoveries,prompts_database}
mkdir -p outputs/satellite_imagery/{regional,zones,sites}
mkdir -p outputs/competition_submissions
mkdir -p submissions/{latest,archive}
```

### **Step 7: Test Installation**

```bash
# Quick test - should show system status
python main.py

# You should see:
# 🏛️ Enhanced Amazon Archaeological Discovery System
# 🎯 OpenAI to Z Challenge - Checkpoint 2 Solution
# ✅ All components initialized successfully!
```

## 🎮 **HOW TO RUN**

### **Complete Automatic Pipeline (Recommended)**

```bash
python main.py

# The system will automatically:
# 1. Load multiple Amazon regions
# 2. Process satellite imagery at multiple scales
# 3. Run AI archaeological analysis
# 4. Generate Checkpoint 2 submission
# 
# ⏱️ Takes 15-30 minutes
# ✅ Produces complete submission with enhanced discoveries
```

## 📊 **EXPECTED OUTPUTS**

After successful run, you'll have:

```
outputs/
├── archaeological_analysis/
│   ├── ai_responses/
│   │   └── enhanced_ai_analysis_*.json    # AI interpretation
│   ├── discoveries/
│   │   ├── processed_data.json           # Raw site data
│   │   └── archaeological_discoveries_*.json # Enhanced discoveries
│   └── prompts_database/
│       └── ai_prompts_used_*.json        # Prompt tracking
├── competition_submissions/
│   └── checkpoint2_final/                # Competition files
└── satellite_imagery/                    # Multi-scale imagery

submissions/
├── latest/
│   ├── checkpoint2_submission_*.json     # Latest submission
│   ├── checkpoint2_summary_*.md          # Human readable report
│   ├── latest_submission.json → [symlink] # Quick access
│   └── latest_summary.md → [symlink]     # Quick access
└── archive/                              # Previous versions
```

## 🏛️ **Enhanced Archaeological Discoveries**

Each discovery includes comprehensive context:

```json
{
  "anomaly_id": "AMAZON_BR_Primary_001",
  "geographic_context": {
    "country": "Brazil",
    "region_name": "Upper Xingu Basin, Brazil", 
    "river_basin": "Xingu River Basin",
    "nearest_major_city": "Canarana",
    "administrative_level_1": "Mato Grosso",
    "coordinates": "WGS84 ±10m precision"
  },
  "cultural_context": {
    "primary_culture": "Upper Xingu cultural complex",
    "time_period": "800-1500 CE (Late Period)",
    "cultural_affiliation": "Upper Xingu cultural complex",
    "regional_network_role": "Major ceremonial hub"
  },
  "site_classification": {
    "tier": "Primary",
    "function": "Upper Xingu plaza village complex", 
    "complexity_level": "High complexity",
    "preservation_status": "Well-preserved"
  },
  "research_potential": {
    "excavation_priority": "High priority",
    "scientific_significance": "Major contribution to Upper Xingu archaeology",
    "conservation_urgency": "Standard monitoring needed"
  }
}
```

## 🎯 **QUICK START FOR ABSOLUTE BEGINNERS**

**If you're completely new to this:**

1. **Install Python 3.8+** from python.org
2. **Download all the system files** to one folder
3. **Open terminal/command prompt** in that folder  
4. **Run**: `pip install -r requirements.txt`
5. **Sign up for Google Earth Engine** (link above)
6. **Wait for approval** (1-2 days)
7. **Run**: `python main.py`
8. **Wait 15-30 minutes** for results
9. **Check**: `submissions/latest/` for your competition submission

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

**4. Import errors**
```bash
# Solution: Ensure you're in the project root directory
cd /path/to/solution2
python main.py
```

## 🏆 **CHECKPOINT 2 COMPLIANCE**

This system automatically ensures:

- ✅ **Enhanced geographic context** (Country, region, river basin details)
- ✅ **Cultural attribution** (Archaeological cultures, time periods)
- ✅ **Five anomaly footprints** (Archaeological sites)
- ✅ **Dataset IDs logged** (Automatic tracking)
- ✅ **OpenAI prompts logged** (Scale-specific prompts)
- ✅ **Reproducibility verified** (±50m tolerance)
- ✅ **Discovery leverage** (Pattern-based re-prompting)

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
3. Check project structure: files should be in `src/` directory
4. Verify you're running from project root: `python main.py`

## 🎉 **SUCCESS CRITERIA**

**You know it worked when you see:**

```
🎉 CHECKPOINT 2 COMPLIANCE: ✅ PASS
✅ Submission package ready!
📄 Files created in submissions/latest/:
   • checkpoint2_submission_*.json
   • checkpoint2_summary_*.md
   
Enhanced discoveries include:
✅ Geographic context (Country: Brazil/Peru/Colombia)
✅ Cultural context (Archaeological cultures & time periods)
✅ Site classification (Function, complexity, preservation)
✅ Research potential (Excavation priority, conservation urgency)
```

**This means you have a complete, competition-ready archaeological discovery submission with detailed cultural context!**

---

*Ready to discover lost civilizations in the Amazon? Let's go! 🏛️* 