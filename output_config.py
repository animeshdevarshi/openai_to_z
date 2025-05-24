# output_config.py
# Centralized output paths configuration for organized file structure

import os
from pathlib import Path

# Base output directory
BASE_OUTPUT_DIR = "outputs"

# Output subdirectories
SUBMISSIONS_DIR = os.path.join(BASE_OUTPUT_DIR, "submissions")
IMAGES_DIR = os.path.join(BASE_OUTPUT_DIR, "images", "enhanced_images")
ANALYSIS_RESULTS_DIR = os.path.join(BASE_OUTPUT_DIR, "analysis_results")

# Specific output paths
OUTPUT_PATHS = {
    # Submission files
    'submissions': SUBMISSIONS_DIR,
    'checkpoint2_submission': os.path.join(SUBMISSIONS_DIR, "checkpoint2_submission.json"),
    'submission_summary': os.path.join(SUBMISSIONS_DIR, "submission_summary.md"),
    
    # Image outputs
    'enhanced_images': IMAGES_DIR,
    'regional_images': os.path.join(IMAGES_DIR, "regional"),
    'zone_images': os.path.join(IMAGES_DIR, "zone"),
    'site_images': os.path.join(IMAGES_DIR, "site"),
    
    # Analysis results
    'analysis_results': ANALYSIS_RESULTS_DIR,
    'ai_analysis': os.path.join(ANALYSIS_RESULTS_DIR, "ai_analysis_complete.json"),
    'ai_responses': os.path.join(ANALYSIS_RESULTS_DIR, "ai_model_responses.json"),
    'prompts_used': os.path.join(ANALYSIS_RESULTS_DIR, "prompts_logged.json"),
    'discoveries': os.path.join(ANALYSIS_RESULTS_DIR, "discoveries.json"),
    'metadata': os.path.join(ANALYSIS_RESULTS_DIR, "metadata.json"),
    'processing_log': os.path.join(ANALYSIS_RESULTS_DIR, "processing_log.txt"),
    
    # Individual AI response files by scale
    'regional_responses': os.path.join(ANALYSIS_RESULTS_DIR, "regional_ai_responses.json"),
    'zone_responses': os.path.join(ANALYSIS_RESULTS_DIR, "zone_ai_responses.json"),
    'site_responses': os.path.join(ANALYSIS_RESULTS_DIR, "site_ai_responses.json"),
    'leverage_responses': os.path.join(ANALYSIS_RESULTS_DIR, "leverage_ai_responses.json")
}

def get_paths():
    """Get all organized output paths for the system"""
    ensure_output_dirs()  # Ensure directories exist
    return {
        'base': BASE_OUTPUT_DIR,
        'submissions': SUBMISSIONS_DIR,
        'images': IMAGES_DIR,
        'analysis_results': ANALYSIS_RESULTS_DIR,
        'regional_images': OUTPUT_PATHS['regional_images'],
        'zone_images': OUTPUT_PATHS['zone_images'],
        'site_images': OUTPUT_PATHS['site_images']
    }

def ensure_output_dirs():
    """Create all output directories if they don't exist"""
    dirs_to_create = [
        BASE_OUTPUT_DIR,
        SUBMISSIONS_DIR,
        IMAGES_DIR,
        ANALYSIS_RESULTS_DIR,
        OUTPUT_PATHS['regional_images'],
        OUTPUT_PATHS['zone_images'],
        OUTPUT_PATHS['site_images']
    ]
    
    for directory in dirs_to_create:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    print(f"✅ Output directories created/verified:")
    for directory in dirs_to_create:
        print(f"   📁 {directory}")

def get_output_path(key):
    """Get a specific output path by key"""
    return OUTPUT_PATHS.get(key, "")

def get_timestamped_filename(base_name, extension, directory_key='submissions'):
    """Generate a timestamped filename in the specified directory"""
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{base_name}_{timestamp}.{extension}"
    directory = OUTPUT_PATHS.get(directory_key, SUBMISSIONS_DIR)
    return os.path.join(directory, filename)

if __name__ == "__main__":
    # Test the configuration
    print("🗂️ OUTPUT CONFIGURATION")
    print("=" * 40)
    ensure_output_dirs()
    print(f"\n📋 Available output paths:")
    for key, path in OUTPUT_PATHS.items():
        print(f"   {key}: {path}") 
    
    print(f"\n🔧 Testing get_paths():")
    paths = get_paths()
    for key, path in paths.items():
        print(f"   {key}: {path}") 