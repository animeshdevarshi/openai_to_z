# 🏛️ Amazon Archaeological Discovery System

**OpenAI to Z Challenge - Checkpoint 2 Solution**

Multi-scale AI-powered archaeological site detection in the Amazon rainforest using satellite imagery and cultural knowledge.

## 🎯 **What This System Does**

Discovers pre-Columbian archaeological sites across the Amazon using:
- **Multi-scale analysis**: 50km → 10km → 2km progressive zoom for network detection
- **Dual-source satellite data**: Optical (Sentinel-2) + Radar (PALSAR) for comprehensive coverage
- **AI interpretation** with archaeological domain knowledge (Casarabe culture, earthwork patterns)
- **Enhanced geographic context**: Country, region, cultural attribution for each discovery

## ⚡ **Quick Evaluation**

```bash
# Run the complete system
python main.py

# Check results
ls submissions/latest/
# → checkpoint2_submission_*.json (competition file)
# → checkpoint2_summary_*.md (human-readable report)
```

**Expected runtime**: ~15-30 minutes  
**Expected output**: 5+ archaeological discoveries with detailed context

## 🏛️ **Sample Discovery Output**

```json
{
  "anomaly_id": "AMAZON_BR_Primary_001",
  "geographic_context": {
    "country": "Brazil",
    "region_name": "Upper Xingu Basin, Brazil",
    "river_basin": "Xingu River Basin",
    "nearest_major_city": "Canarana"
  },
  "cultural_context": {
    "primary_culture": "Upper Xingu cultural complex",
    "time_period": "800-1500 CE (Late Period)",
    "cultural_affiliation": "Upper Xingu cultural complex"
  },
  "site_classification": {
    "tier": "Primary",
    "function": "Upper Xingu plaza village complex",
    "complexity_level": "High complexity"
  },
  "coordinates": {
    "center_lat": -13.2456,
    "center_lng": -53.1789,
    "confidence": 0.85
  }
}
```

## 🏆 **Checkpoint 2 Compliance**

- ✅ **Enhanced geographic context** (Country, region, river basin details)
- ✅ **Cultural attribution** (Archaeological cultures, time periods)  
- ✅ **Five anomaly footprints** (Archaeological sites with precise coordinates)
- ✅ **Dataset IDs logged** (Sentinel-2, PALSAR data sources)
- ✅ **OpenAI prompts logged** (Scale-specific archaeological analysis)
- ✅ **Reproducibility verified** (±50m tolerance)
- ✅ **Discovery leverage** (Pattern-based re-prompting)

## 📁 **Output Structure**

```
submissions/latest/          # Competition-ready files
├── checkpoint2_submission_*.json   # Main submission
├── checkpoint2_summary_*.md        # Human-readable report
├── latest_submission.json → [symlink]
└── latest_summary.md → [symlink]

outputs/archaeological_analysis/    # Detailed analysis
├── ai_responses/           # AI interpretation results
├── discoveries/            # Enhanced discovery data
└── prompts_database/       # Prompt tracking for compliance
```

## 🔧 **Prerequisites**

1. **Python 3.8+**
2. **Google Earth Engine account** (approved access required)
3. **Dependencies**: `pip install -r requirements.txt`

Optional:
- **OpenAI API key** (system uses mock responses for testing)

## 📚 **Scientific Foundation**

Based on recent archaeological research:
- **Prümers et al. 2022** - Casarabe culture settlement networks
- **Multi-scale remote sensing archaeology**
- **Amazon pre-Columbian urban planning patterns**

## 🎉 **Success Indicators**

You know it worked when you see:
```
🎉 CHECKPOINT 2 COMPLIANCE: ✅ PASS
✅ Submission package ready!

Enhanced discoveries include:
✅ Geographic context (Brazil/Peru/Colombia regions)
✅ Cultural context (Archaeological cultures & time periods)
✅ Site classification (Function, complexity, preservation)
✅ Research potential (Excavation priority, conservation urgency)
```

---

**Ready to evaluate?** Run `python main.py` and check `submissions/latest/` for results.

For detailed setup instructions, see [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md). 