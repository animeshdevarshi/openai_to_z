# Analysis Metadata

## Contents
This directory contains technical analysis files and metadata:

- `ai_archaeological_analysis_*.json` - Complete AI analysis responses
- `processed_data.json` - Processed satellite data details
- Technical logs and analysis parameters

## AI Model Information
- **Primary Model**: o4-mini-2025-04-16
- **Reasoning Effort**: high
- **Response Format**: json_object
- **Models Used**: o4-mini-2025-04-16
- **Total AI Calls**: 436

## Analysis Pipeline
1. **Data Acquisition**: Sentinel-2 + Sentinel-1/ALOS PALSAR
2. **Multi-scale Processing**: 50km → 10km → 2km analysis
3. **AI Analysis**: o4-mini-2025-04-16 with archaeological prompts
4. **Discovery Validation**: Confidence scoring and verification
5. **Submission Generation**: Checkpoint 2 compliance validation

Generated: 2025-05-25 16:18:14
