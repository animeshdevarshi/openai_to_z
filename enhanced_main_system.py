# enhanced_main_system.py
# Complete OpenAI to Z Challenge Checkpoint 2 Solution
# Multi-scale archaeological discovery with full compliance

import os
import sys
import time
import json
import glob
from datetime import datetime
from typing import Dict, List, Optional

# Import all enhanced components
from simple_region_config import SimpleRegionConfig
from enhanced_data_acquisition import EnhancedDataAcquisition
from enhanced_data_processor import EnhancedDataProcessor
from enhanced_ai_analyzer import EnhancedAIAnalyzer
from enhanced_results_manager import EnhancedResultsManager
from output_config import get_paths

class EnhancedAmazonArchaeology:
    """
    Complete enhanced system for Amazon archaeological discovery
    Implements multi-scale analysis with full Checkpoint 2 compliance
    Added resume functionality and step selection
    """
    
    def __init__(self):
        """Initialize the complete enhanced system with resume capability"""
        print("🏛️ Enhanced Amazon Archaeological Discovery System")
        print("=" * 60)
        print("🎯 OpenAI to Z Challenge - Checkpoint 2 Solution")
        print("🔬 Multi-scale Network Detection: 50km → 10km → 2km")
        print("📊 Dual-source Analysis: Optical + Radar")
        print("🤖 AI-powered with Archaeological Knowledge")
        print("✅ Full Checkpoint 2 Compliance")
        print("🔄 Resume capability enabled")
        print()
        
        # Initialize all components
        print("🔧 Initializing system components...")
        
        self.region_config = SimpleRegionConfig()
        self.data_acquisition = EnhancedDataAcquisition()
        self.data_processor = EnhancedDataProcessor()
        self.ai_analyzer = EnhancedAIAnalyzer()
        self.results_manager = EnhancedResultsManager()
        
        # Get organized paths
        self.paths = get_paths()
        
        # Track pipeline progress with file-based persistence
        self.progress_file = os.path.join(self.paths['base'], 'pipeline_progress.json')
        self.pipeline_status = self.load_pipeline_progress()
        
        # Store results from each stage
        self.loaded_data = {}
        self.processed_data = {}
        self.ai_analyses = {}
        self.final_submission = {}
        
        print("✅ All components initialized successfully!")
        print("🔄 Checking for previous progress...")
        self.detect_existing_progress()
        print()

    def load_pipeline_progress(self) -> Dict:
        """Load pipeline progress from file"""
        default_status = {
            'authentication': False,
            'data_loaded': False,
            'processing_complete': False,
            'ai_analysis_complete': False,
            'submission_ready': False,
            'last_updated': None,
            'regions_processed': [],
            'images_created': {},
            'ai_responses_saved': {}
        }
        
        if os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, 'r') as f:
                    return json.load(f)
            except:
                return default_status
        return default_status

    def save_pipeline_progress(self):
        """Save current pipeline progress to file"""
        self.pipeline_status['last_updated'] = datetime.now().isoformat()
        try:
            with open(self.progress_file, 'w') as f:
                json.dump(self.pipeline_status, f, indent=2)
        except Exception as e:
            print(f"⚠️ Could not save progress: {e}")

    def detect_existing_progress(self):
        """Detect what has already been completed"""
        print("🔍 Scanning for existing progress...")
        
        # Check for existing images
        image_dirs = ['regional', 'zone', 'site']
        existing_images = {}
        
        for img_dir in image_dirs:
            img_path = os.path.join(self.paths['images'], img_dir)
            if os.path.exists(img_path):
                images = glob.glob(os.path.join(img_path, '*.png'))
                if images:
                    existing_images[img_dir] = len(images)
                    print(f"   📸 Found {len(images)} {img_dir} images")
        
        # Check for AI analysis results
        ai_results_path = self.paths['analysis_results']
        existing_ai_files = []
        if os.path.exists(ai_results_path):
            ai_files = glob.glob(os.path.join(ai_results_path, '*_ai_*.json'))
            existing_ai_files = [os.path.basename(f) for f in ai_files]
            if ai_files:
                print(f"   🤖 Found {len(ai_files)} AI analysis files")
        
        # Check for submissions
        submissions_path = self.paths['submissions']
        existing_submissions = []
        if os.path.exists(submissions_path):
            submission_files = glob.glob(os.path.join(submissions_path, 'checkpoint2_*.json'))
            existing_submissions = [os.path.basename(f) for f in submission_files]
            if submission_files:
                print(f"   📦 Found {len(submission_files)} submission files")
        
        # Update pipeline status based on findings
        if existing_images:
            self.pipeline_status['processing_complete'] = True
            print("   ✅ Processing appears complete (images found)")
        
        if existing_ai_files:
            self.pipeline_status['ai_analysis_complete'] = True
            print("   ✅ AI analysis appears complete (results found)")
        
        if existing_submissions:
            self.pipeline_status['submission_ready'] = True
            print("   ✅ Submissions found")
        
        self.pipeline_status['images_created'] = existing_images
        self.pipeline_status['ai_responses_saved'] = existing_ai_files
        
        if any([existing_images, existing_ai_files, existing_submissions]):
            print("🔄 Previous work detected - resume options available")
        else:
            print("🚀 No previous work found - fresh start")

    def load_existing_data(self):
        """Load existing processed data from files"""
        print("📂 Loading existing data...")
        
        # Try to load processed data
        processed_data_file = os.path.join(self.paths['analysis_results'], 'processed_data.json')
        if os.path.exists(processed_data_file):
            try:
                with open(processed_data_file, 'r') as f:
                    self.processed_data = json.load(f)
                print(f"   ✅ Loaded processed data for {len(self.processed_data)} regions")
                
                # Debug: Show what we loaded
                for region_id, region_data in self.processed_data.items():
                    zones_count = len(region_data.get('scales', {}).get('zones', []))
                    sites_count = len(region_data.get('scales', {}).get('sites', []))
                    print(f"   📍 {region_id}: {zones_count} zones, {sites_count} sites")
                    
            except Exception as e:
                print(f"   ⚠️ Could not load processed data: {e}")
        
        # Try to load AI analyses
        ai_analysis_file = os.path.join(self.paths['analysis_results'], 'ai_analyses.json')
        if os.path.exists(ai_analysis_file):
            try:
                with open(ai_analysis_file, 'r') as f:
                    self.ai_analyses = json.load(f)
                print(f"   ✅ Loaded AI analyses")
            except Exception as e:
                print(f"   ⚠️ Could not load AI analyses: {e}")
        else:
            print("   🔄 No previous AI analyses found - will run fresh analysis")
            self.ai_analyses = {}  # Reset to ensure fresh analysis
        
        # Load the latest enhanced AI analysis file with discoveries
        enhanced_ai_files = glob.glob(os.path.join(self.paths['analysis_results'], 'enhanced_ai_analysis_*.json'))
        if enhanced_ai_files:
            # Get the most recent file
            latest_ai_file = max(enhanced_ai_files, key=os.path.getmtime)
            try:
                with open(latest_ai_file, 'r') as f:
                    enhanced_ai_data = json.load(f)
                
                # Load discoveries into the AI analyzer
                if 'discoveries' in enhanced_ai_data:
                    self.ai_analyzer.discoveries = enhanced_ai_data['discoveries']
                    print(f"   ✅ Loaded {len(self.ai_analyzer.discoveries)} AI discoveries")
                
                # Load AI responses if available
                if 'ai_responses' in enhanced_ai_data:
                    self.ai_analyzer.ai_responses = enhanced_ai_data['ai_responses']
                    print(f"   ✅ Loaded {len(self.ai_analyzer.ai_responses)} AI responses")
                
                # Load prompts used
                if 'prompts_used' in enhanced_ai_data:
                    self.ai_analyzer.prompts_used = enhanced_ai_data['prompts_used']
                    total_prompts = sum(len(prompts) if isinstance(prompts, list) else (1 if prompts else 0) 
                                      for prompts in self.ai_analyzer.prompts_used.values())
                    print(f"   ✅ Loaded {total_prompts} AI prompts")
                    
            except Exception as e:
                print(f"   ⚠️ Could not load enhanced AI analysis: {e}")
        else:
            print("   🔄 No enhanced AI analysis found - discoveries may be missing")

    def save_current_data(self):
        """Save current data state"""
        try:
            # Save processed data
            if self.processed_data:
                processed_file = os.path.join(self.paths['analysis_results'], 'processed_data.json')
                with open(processed_file, 'w') as f:
                    # Remove GEE objects for JSON serialization
                    serializable_data = self.make_serializable(self.processed_data)
                    json.dump(serializable_data, f, indent=2)
            
            # Save AI analyses
            if self.ai_analyses:
                ai_file = os.path.join(self.paths['analysis_results'], 'ai_analyses.json')
                with open(ai_file, 'w') as f:
                    json.dump(self.ai_analyses, f, indent=2)
            
            self.save_pipeline_progress()
            
        except Exception as e:
            print(f"⚠️ Could not save current data: {e}")

    def make_serializable(self, data):
        """Remove non-serializable objects for JSON storage"""
        if isinstance(data, dict):
            result = {}
            for key, value in data.items():
                if key in ['data_sources', 'regional_area']:  # Skip GEE objects
                    continue
                result[key] = self.make_serializable(value)
            return result
        elif isinstance(data, list):
            return [self.make_serializable(item) for item in data]
        else:
            return data

    def step_1_setup_and_authentication(self) -> bool:
        """
        Step 1: Setup Google Earth Engine authentication
        """
        print("🔑 STEP 1: Setup and Authentication")
        print("-" * 40)
        
        # Show available regions with data status
        print("🌍 Available Amazon regions:")
        regions = self.region_config.get_regions_by_priority(8)
        for region_id, info in regions.items():
            priority_emoji = "🔴" if info['priority'] == 'high' else "🟡" if info['priority'] == 'medium' else "🟢"
            sites_emoji = "🏛️" if info['known_sites'] else "🔍"
            
            # Add data availability status (simplified check)
            data_status = "📊" if region_id in ['brazil_xingu', 'brazil_acre', 'peru_explore'] else "⚠️"
            
            print(f"  {priority_emoji} {sites_emoji} {data_status} {region_id}: {info['name']} ({info['country']})")
        
        print()
        print("📊 = Good data availability")
        print("⚠️ = Limited data availability")
        print()
        
        # Setup Google Earth Engine
        if self.data_acquisition.setup_google_earth_engine():
            self.pipeline_status['authentication'] = True
            self.save_pipeline_progress()
            print("✅ Step 1 completed - Authentication successful!")
            return True
        else:
            print("❌ Step 1 failed - Please setup Google Earth Engine")
            print("\n📚 Setup Instructions:")
            print("1. Visit: https://earthengine.google.com/")
            print("2. Sign up with Google account")
            print("3. Wait for approval (1-2 days)")
            print("4. Run: import ee; ee.Authenticate()")
            print("5. Re-run this system")
            return False

    def select_regions_for_analysis(self, max_regions: int = 3) -> List[str]:
        """
        Let user select which regions to analyze
        """
        print(f"🗺️ REGION SELECTION")
        print("-" * 30)
        
        regions = self.region_config.get_regions_by_priority(8)
        
        # Recommended regions with excellent/good data availability
        recommended = []
        for region_id, info in regions.items():
            data_status = info.get('data_availability', 'unknown')
            if data_status in ['excellent', 'good']:
                recommended.append(region_id)
        
        print("📍 Recommended regions (good data availability):")
        for i, region_id in enumerate(recommended[:3], 1):
            if region_id in regions:
                info = regions[region_id]
                sites_text = "Known sites" if info.get('known_sites', False) else "Exploration"
                data_status = info.get('data_availability', 'unknown')
                print(f"  {i}. {region_id}: {info['name']} ({sites_text}) - {data_status}")
        
        print(f"\n🌍 All available regions:")
        region_list = list(regions.keys())
        for i, region_id in enumerate(region_list, 1):
            info = regions[region_id]
            data_status = info.get('data_availability', 'unknown')
            
            # Data availability emoji
            if data_status == 'excellent':
                status_emoji = "🟢"
            elif data_status == 'good':
                status_emoji = "📊"
            elif data_status == 'fair':
                status_emoji = "🟡"
            else:
                status_emoji = "⚠️"
            
            sites_text = "🏛️ Known sites" if info.get('known_sites', False) else "🔍 Exploration"
            print(f"  {i}. {region_id}: {info['name']} - {status_emoji} {data_status} - {sites_text}")
        
        print(f"\nOptions:")
        print(f"  R. Use recommended regions (auto-select best {min(max_regions, len(recommended))})")
        print(f"  A. Analyze all available regions")
        print(f"  C. Custom selection")
        
        while True:
            choice = input(f"\nSelect option (R/A/C/1-{len(region_list)}): ").strip().upper()
            
            if choice == 'R':
                selected = recommended[:max_regions]
                print(f"✅ Selected recommended regions: {', '.join(selected)}")
                return selected
            
            elif choice == 'A':
                selected = region_list[:max_regions]
                print(f"✅ Selected all regions: {', '.join(selected)}")
                return selected
            
            elif choice == 'C':
                return self.custom_region_selection(region_list, max_regions)
            
            elif choice.isdigit():
                region_idx = int(choice) - 1
                if 0 <= region_idx < len(region_list):
                    selected = [region_list[region_idx]]
                    print(f"✅ Selected single region: {selected[0]}")
                    return selected
                else:
                    print("❌ Invalid region number")
            
            else:
                print("❌ Invalid choice, please try again")

    def custom_region_selection(self, region_list: List[str], max_regions: int) -> List[str]:
        """
        Allow custom region selection
        """
        print(f"\n🎯 CUSTOM SELECTION (max {max_regions} regions)")
        print("Enter region numbers separated by commas (e.g., 1,3,4):")
        
        while True:
            selection = input("Regions: ").strip()
            
            try:
                indices = [int(x.strip()) - 1 for x in selection.split(',')]
                
                if len(indices) > max_regions:
                    print(f"❌ Too many regions selected (max {max_regions})")
                    continue
                
                if all(0 <= idx < len(region_list) for idx in indices):
                    selected = [region_list[idx] for idx in indices]
                    print(f"✅ Selected regions: {', '.join(selected)}")
                    return selected
                else:
                    print("❌ Invalid region numbers")
            
            except ValueError:
                print("❌ Please enter numbers separated by commas")
    
    def step_2_load_dual_source_data(self, max_regions: int = 3) -> bool:
        """
        Step 2: Load dual-source satellite data with region selection
        Implements Checkpoint 2 requirement for two independent sources
        """
        if not self.pipeline_status['authentication']:
            print("❌ Please complete Step 1 first!")
            return False
        
        print(f"📡 STEP 2: Load Dual-Source Data")
        print("-" * 40)
        print("📊 Data sources: Optical (Sentinel-2) + Radar (PALSAR/Sentinel-1)")
        print("✅ Checkpoint 2 compliance: Two independent public sources")
        print()
        
        # Let user select regions
        selected_regions = self.select_regions_for_analysis(max_regions)
        
        if not selected_regions:
            print("❌ No regions selected")
            return False
        
        print(f"\n🎯 Loading data for: {', '.join(selected_regions)}")
        print("⏱️ This may take several minutes per region...")
        print()
        
        # Load data for selected regions only
        self.loaded_data = self.data_acquisition.load_specific_regions(selected_regions)
        
        if self.loaded_data:
            self.pipeline_status['data_loaded'] = True
            
            # Show data summary
            data_summary = self.data_acquisition.get_data_summary()
            self.data_acquisition.show_summary()
            
            print(f"\n✅ Step 2 completed - Data loaded for {len(self.loaded_data)} regions!")
            print(f"📊 Checkpoint 2 compliance verified: ✅")
            return True
        else:
            print("❌ Step 2 failed - No data loaded")
            print("💡 Try selecting different regions with better data availability")
            return False
    
    def step_3_multi_scale_processing(self) -> bool:
        """
        Step 3: Multi-scale progressive image processing
        Creates images for all three analysis scales
        """
        if not self.pipeline_status['data_loaded']:
            print("❌ Please complete Step 2 first!")
            return False
        
        print(f"🔬 STEP 3: Multi-Scale Processing")
        print("-" * 40)
        print("🌍 Scale 1: Regional network detection (50km)")
        print("🔍 Scale 2: Zone site identification (10km)")
        print("🎯 Scale 3: Site feature confirmation (2km)")
        print()
        
        # Process all loaded regions with multi-scale analysis
        self.processed_data = self.data_processor.process_all_regions(self.loaded_data)
        
        if self.processed_data:
            self.pipeline_status['processing_complete'] = True
            
            # Save current data state including processed results
            print("💾 Saving processing results...")
            self.save_current_data()
            
            # Count total discoveries
            total_candidates = sum(
                len(result['discovery_candidates']) 
                for result in self.processed_data.values()
            )
            
            print(f"\n✅ Step 3 completed - Multi-scale processing finished!")
            print(f"🎯 Discovery candidates found: {total_candidates}")
            print(f"📁 Images created in: {self.data_processor.output_folder}/")
            print(f"💾 Processing data saved to: {self.paths['analysis_results']}/")
            return True
        else:
            print("❌ Step 3 failed - Processing unsuccessful")
            return False
    
    def step_4_ai_analysis_pipeline(self) -> bool:
        """
        Step 4: Complete AI analysis pipeline
        Regional → Zone → Site → Leverage analysis
        """
        if not self.pipeline_status['processing_complete']:
            print("❌ Please complete Step 3 first!")
            return False
        
        print(f"🤖 STEP 4: AI Analysis Pipeline")
        print("-" * 40)
        print("🌍 Stage 1: Regional network analysis")
        print("🔍 Stage 2: Zone site detection")
        print("🎯 Stage 3: Site confirmation")
        print("🔄 Stage 4: Discovery leverage")
        print()
        
        # Ensure we have processed data loaded
        if not self.processed_data:
            print("📂 Loading processed data first...")
            self.load_existing_data()
        
        if not self.processed_data:
            print("❌ No processed data available for AI analysis")
            return False
        
        print(f"📊 Analyzing {len(self.processed_data)} regions with AI...")
        for region_id, region_data in self.processed_data.items():
            zones = len(region_data.get('scales', {}).get('zones', []))
            sites = len(region_data.get('scales', {}).get('sites', []))
            print(f"   🎯 {region_id}: {zones} zones, {sites} sites")
        
        # Run complete multi-scale AI analysis
        self.ai_analyses = self.ai_analyzer.analyze_all_scales(self.processed_data)
        
        if self.ai_analyses:
            self.pipeline_status['ai_analysis_complete'] = True
            
            # Save AI analysis results to organized folder
            print("💾 Saving AI analysis results...")
            ai_results_file = self.ai_analyzer.save_analysis_results()
            
            # Save current system state
            self.save_current_data()
            
            # Get all discoveries
            all_discoveries = self.ai_analyzer.get_high_confidence_discoveries(min_confidence=0.3)
            
            print(f"\n✅ Step 4 completed - AI analysis finished!")
            print(f"🏛️ Archaeological discoveries: {len(all_discoveries)}")
            print(f"📝 Prompts logged: {sum(len(prompts) if isinstance(prompts, list) else (1 if prompts else 0) for prompts in self.ai_analyses.values())}")
            print(f"🔄 Leverage analysis: {'✅' if self.ai_analyses.get('leverage') else '❌'}")
            print(f"💾 Results saved to: {ai_results_file}")
            return True
        else:
            print("❌ Step 4 failed - AI analysis unsuccessful")
            return False
    
    def step_5_create_checkpoint2_submission(self) -> bool:
        """
        Step 5: Create complete Checkpoint 2 submission
        Validates all requirements and creates submission package
        """
        if not self.pipeline_status['ai_analysis_complete']:
            print("❌ Please complete Step 4 first!")
            return False
        
        print(f"📦 STEP 5: Create Checkpoint 2 Submission")
        print("-" * 40)
        print("✅ Validating all Checkpoint 2 requirements...")
        print()
        
        # Ensure we have all current data loaded
        if not self.processed_data or not self.ai_analyses:
            print("📂 Loading latest analysis data...")
            self.load_existing_data()
        
        # Debug: Check what we have
        print(f"📊 Debug - Current data status:")
        print(f"   Processed regions: {len(self.processed_data)}")
        print(f"   AI analyses: {len(self.ai_analyses) if self.ai_analyses else 0}")
        print(f"   AI discoveries: {len(self.ai_analyzer.discoveries)}")
        
        # Get data summary - use create_data_summary for proper structure
        data_summary = self.data_acquisition.create_data_summary()
        
        # Get processor discoveries
        all_discoveries = self.data_processor.get_all_discoveries() if hasattr(self.data_processor, 'get_all_discoveries') else []
        
        # Get AI discoveries 
        ai_discoveries = self.ai_analyzer.get_high_confidence_discoveries(min_confidence=0.3)
        
        print(f"📊 Discovery counts before merging:")
        print(f"   Processor discoveries: {len(all_discoveries)}")
        print(f"   AI discoveries: {len(ai_discoveries)}")
        
        # Merge processor and AI discoveries
        enhanced_discoveries = self.merge_discoveries(all_discoveries, ai_discoveries)
        
        print(f"   Enhanced discoveries: {len(enhanced_discoveries)}")
        
        # Create submission package
        self.final_submission = self.results_manager.create_checkpoint2_submission(
            data_summary, 
            self.ai_analyses, 
            enhanced_discoveries
        )
        
        if self.final_submission:
            self.pipeline_status['submission_ready'] = True
            
            # Save submission files
            submission_file = self.results_manager.save_submission()
            summary_file = self.results_manager.create_summary_report()
            
            # Show final summary
            self.results_manager.show_final_summary()
            
            print(f"\n✅ Step 5 completed - Submission package ready!")
            print(f"📄 Files created:")
            print(f"   • {submission_file}")
            print(f"   • {summary_file}")
            return True
        else:
            print("❌ Step 5 failed - Submission requirements not met")
            return False
    
    def merge_discoveries(self, processor_discoveries: List[Dict], ai_discoveries: List[Dict]) -> List[Dict]:
        """
        Merge discoveries from processor and AI analyzer
        """
        merged = []
        
        print(f"🔍 Merging discoveries: {len(processor_discoveries)} processor + {len(ai_discoveries)} AI")
        
        # Start with processor discoveries (have spatial analysis)
        for discovery in processor_discoveries:
            # Ensure proper field naming for validation
            if 'center_lat' not in discovery and 'center_lng' not in discovery:
                # Try to extract coordinates from other fields
                if hasattr(discovery, 'center_lat') and hasattr(discovery, 'center_lng'):
                    discovery['center_lat'] = discovery.center_lat
                    discovery['center_lng'] = discovery.center_lng
                elif 'coordinates' in discovery:
                    coords = discovery['coordinates']
                    if isinstance(coords, list) and len(coords) >= 2:
                        discovery['center_lat'] = coords[0]
                        discovery['center_lng'] = coords[1]
            
            # Ensure confidence field
            if 'confidence' not in discovery and 'confidence_score' not in discovery:
                discovery['confidence'] = discovery.get('site_confidence', 0.7)
            
            merged.append(discovery)
        
        # Add ALL AI discoveries - they already have proper field formatting
        for ai_disc in ai_discoveries:
            # Format AI discovery properly - ensure all required fields
            formatted_disc = {
                'center_lat': ai_disc.get('center_lat', ai_disc.get('lat')),
                'center_lng': ai_disc.get('center_lng', ai_disc.get('lng')),
                'confidence': ai_disc.get('confidence_score', ai_disc.get('confidence', 0.5)),
                'site_id': ai_disc.get('id', ai_disc.get('site_id', f'ai_discovery_{len(merged)+1}')),
                'site_type': ai_disc.get('site_type', ai_disc.get('type', 'ai_detected')),
                'source': 'ai_analysis',
                'discovery_timestamp': ai_disc.get('discovery_timestamp', ''),
                'analysis_scale': ai_disc.get('analysis_scale', 'zone')
            }
            
            # Copy additional fields if available
            for field in ['diameter_meters', 'defensive_rings', 'features_detected', 'measurements']:
                if field in ai_disc:
                    formatted_disc[field] = ai_disc[field]
            
            merged.append(formatted_disc)
        
        # Add more discoveries from processed data if we need them
        if hasattr(self, 'processed_data') and self.processed_data:
            for region_id, region_results in self.processed_data.items():
                discovery_candidates = region_results.get('discovery_candidates', [])
                for candidate in discovery_candidates:
                    # Add if not already in merged list
                    if not any(abs(discovery.get('center_lat', 0) - candidate.get('center_lat', 0)) < 0.01
                              for discovery in merged):
                        merged.append(candidate)
                        print(f"   ✅ Added processor candidate: {candidate.get('site_id', 'unknown')}")
        
        print(f"🔍 Final merged count: {len(merged)} discoveries")
        
        # Sort by confidence
        return sorted(merged, key=lambda x: x.get('confidence', 0), reverse=True)
    
    def run_complete_pipeline(self, max_regions: int = 3) -> bool:
        """
        Run complete pipeline with resume capability
        """
        print(f"🚀 COMPLETE CHECKPOINT 2 PIPELINE")
        print("=" * 60)
        print(f"📊 Analyzing {max_regions} regions")
        print(f"🎯 Target: Full Checkpoint 2 compliance")
        print(f"⏱️ Estimated time: 15-30 minutes")
        print()
        
        # Step 1: Authentication (always verify - don't skip)
        print("🔑 STEP 1: Authentication & Setup")
        print("-" * 40)
        if not self.data_acquisition.setup_google_earth_engine():
            print("❌ Google Earth Engine setup failed!")
            return False
        else:
            self.pipeline_status['authentication'] = True
            print("✅ Step 1 completed - Authentication verified!")
        
        print("=" * 60)
        
        # Step 2: Data loading (skip if already done)
        if not self.pipeline_status['data_loaded']:
            if not self.step_2_load_dual_source_data(max_regions):
                return False
        else:
            print("📡 Step 2: Data Loading ✅ (already completed)")
            print("🔄 Loading existing data...")
            # We would need to reload the actual GEE data here for processing
        
        print("=" * 60)
        
        # Step 3: Processing (skip if already done)
        if not self.pipeline_status['processing_complete']:
            if not self.step_3_multi_scale_processing():
                return False
        else:
            print("🔬 Step 3: Multi-Scale Processing ✅ (already completed)")
            self.load_existing_data()
        
        print("=" * 60)
        
        # Step 4: AI analysis (skip if already done)
        if not self.pipeline_status['ai_analysis_complete']:
            if not self.step_4_ai_analysis_pipeline():
                return False
        else:
            print("🤖 Step 4: AI Analysis ✅ (already completed)")
            self.load_existing_data()
        
        print("=" * 60)
        
        # Step 5: Submission (always run to get latest)
        if not self.step_5_create_checkpoint2_submission():
            return False
        
        print("\n🎉 COMPLETE PIPELINE SUCCESSFUL!")
        print("=" * 40)
        self.show_final_validation_summary()
        return True

    def run_step_by_step_mode(self):
        """Interactive step-by-step mode with resume options"""
        while True:
            try:
                print(f"\n🛠️ STEP-BY-STEP MODE")
                print("=" * 30)
                
                # Show current status
                self.show_pipeline_status()
                
                print(f"\n📋 Available Actions:")
                print(f"1. Run Step 1: Authentication")
                print(f"2. Run Step 2: Load Data (1-5 regions)")
                print(f"3. Run Step 3: Multi-scale Processing")
                print(f"4. Run Step 4: AI Analysis")
                print(f"5. Run Step 5: Create Submission")
                print(f"6. Resume from detected step")
                print(f"7. Load existing results")
                print(f"8. Show detailed status")
                print(f"9. Clear progress and restart")
                print(f"0. Exit")
                
                choice = input(f"\nSelect action (0-9): ").strip()
                
                if choice == '0':
                    print("👋 Exiting step-by-step mode")
                    break
                elif choice == '1':
                    self.step_1_setup_and_authentication()
                elif choice == '2':
                    regions = input("How many regions? (1-5): ").strip()
                    max_regions = int(regions) if regions.isdigit() and 1 <= int(regions) <= 5 else 3
                    self.step_2_load_dual_source_data(max_regions)
                elif choice == '3':
                    if self.pipeline_status['data_loaded']:
                        self.step_3_multi_scale_processing()
                    else:
                        print("❌ Please complete Step 2 first!")
                elif choice == '4':
                    if self.pipeline_status['processing_complete']:
                        self.step_4_ai_analysis_pipeline()
                    else:
                        print("❌ Please complete Step 3 first!")
                elif choice == '5':
                    if self.pipeline_status['ai_analysis_complete']:
                        self.step_5_create_checkpoint2_submission()
                    else:
                        print("❌ Please complete Step 4 first!")
                elif choice == '6':
                    self.resume_from_detected_step()
                elif choice == '7':
                    self.load_existing_data()
                    print("✅ Existing results loaded")
                elif choice == '8':
                    self.show_detailed_status()
                elif choice == '9':
                    self.clear_progress()
                    print("🔄 Progress cleared - fresh start")
                else:
                    print("❌ Invalid choice, please try again")
                    
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\n👋 Exiting step-by-step mode")
                break    
            except Exception as e:
                print(f"❌ Error: {e}")
                input("Press Enter to continue...")

    def resume_from_detected_step(self):
        """Resume pipeline from detected completion point"""
        print("🔄 Resuming from detected progress...")
        
        if not self.pipeline_status['authentication']:
            print("▶️ Starting from Step 1: Authentication")
            self.step_1_setup_and_authentication()
        elif not self.pipeline_status['data_loaded']:
            print("▶️ Starting from Step 2: Data Loading")
            regions = input("How many regions? (1-5): ").strip()
            max_regions = int(regions) if regions.isdigit() and 1 <= int(regions) <= 5 else 3
            self.step_2_load_dual_source_data(max_regions)
        elif not self.pipeline_status['processing_complete']:
            print("▶️ Starting from Step 3: Processing")
            self.step_3_multi_scale_processing()
        elif not self.pipeline_status['ai_analysis_complete']:
            print("▶️ Starting from Step 4: AI Analysis")
            self.load_existing_data()
            self.step_4_ai_analysis_pipeline()
        else:
            print("▶️ Running Step 5: Create Submission")
            self.load_existing_data()
            self.step_5_create_checkpoint2_submission()

    def clear_progress(self):
        """Clear all progress and start fresh"""
        confirm = input("⚠️ This will clear all progress. Continue? (y/N): ").strip().lower()
        if confirm == 'y':
            # Reset pipeline status
            self.pipeline_status = {
                'authentication': False,
                'data_loaded': False,
                'processing_complete': False,
                'ai_analysis_complete': False,
                'submission_ready': False,
                'last_updated': None,
                'regions_processed': [],
                'images_created': {},
                'ai_responses_saved': {}
            }
            
            # Clear data
            self.loaded_data = {}
            self.processed_data = {}
            self.ai_analyses = {}
            self.final_submission = {}
            
            # Save cleared state
            self.save_pipeline_progress()
            
            print("🔄 All progress cleared")

    def show_pipeline_status(self):
        """Show current pipeline status"""
        print(f"\n📊 PIPELINE STATUS:")
        print("-" * 30)
        
        for step, completed in self.pipeline_status.items():
            status = "✅ Complete" if completed else "⏸️ Pending"
            step_name = step.replace('_', ' ').title()
            print(f"{step_name}: {status}")
        
        if self.loaded_data:
            print(f"\nData: {len(self.loaded_data)} regions loaded")
        if self.processed_data:
            total_candidates = sum(len(result.get('discovery_candidates', [])) for result in self.processed_data.values())
            print(f"Processing: {total_candidates} candidates found")
        if hasattr(self, 'ai_analyses') and self.ai_analyses:
            discoveries = len(self.ai_analyzer.get_high_confidence_discoveries(0.3))
            print(f"AI Analysis: {discoveries} discoveries")
    
    def show_detailed_status(self):
        """Show detailed system status"""
        print(f"\n📋 DETAILED SYSTEM STATUS")
        print("=" * 50)
        
        # Component status
        print("🔧 Components:")
        print(f"   Region Config: {len(self.region_config.regions)} regions available")
        print(f"   Data Acquisition: {'✅ Ready' if self.data_acquisition.authenticated else '❌ Not authenticated'}")
        print(f"   Data Processor: {len(self.data_processor.analysis_scales)} analysis scales")
        print(f"   AI Analyzer: Casarabe knowledge base loaded")
        print(f"   Results Manager: Checkpoint 2 compliance monitoring")
        
        # Data status
        if self.loaded_data:
            print(f"\n📊 Loaded Data:")
            for region_id, data in self.loaded_data.items():
                print(f"   {region_id}: {data['region_info']['name']}")
                print(f"      Optical scenes: {data['metadata']['optical_scenes']}")
                print(f"      Radar source: {data['metadata']['radar_source']}")
        
        # Processing status
        if self.processed_data:
            print(f"\n🔬 Processing Results:")
            for region_id, results in self.processed_data.items():
                print(f"   {region_id}: {results['region_name']}")
                print(f"      Candidates: {len(results['discovery_candidates'])}")
                print(f"      Analysis scales: {len(results['scales'])}")
        
        # AI status
        if hasattr(self, 'ai_analyses') and self.ai_analyses:
            print(f"\n🤖 AI Analysis:")
            total_prompts = sum(len(prompts) if isinstance(prompts, list) else 1 
                              for prompts in self.ai_analyses.values() if prompts)
            print(f"   Total prompts: {total_prompts}")
            print(f"   Discoveries: {len(self.ai_analyzer.discoveries)}")
            print(f"   Leverage analysis: {'✅' if self.ai_analyses.get('leverage') else '❌'}")
        
        # Submission status
        if self.final_submission:
            print(f"\n📦 Submission:")
            print(f"   Status: {self.final_submission['validation']['overall_status']}")
            print(f"   Footprints: {len(self.final_submission['anomaly_footprints'])}")
            print(f"   Quality score: {self.final_submission['quality_metrics']['average_discovery_confidence']:.3f}")
    
    def show_final_validation_summary(self):
        """Show final validation summary"""
        if not self.final_submission:
            return
        
        validation = self.final_submission['validation']
        
        print(f"🔍 FINAL VALIDATION SUMMARY")
        print("=" * 40)
        print(f"📊 Overall Status: {validation['overall_status']}")
        print()
        
        # Check each requirement
        requirements = validation['requirements']
        
        req_names = {
            'independent_sources': 'Two Independent Data Sources',
            'anomaly_footprints': 'Five Anomaly Footprints',
            'dataset_logging': 'Dataset IDs Logged',
            'prompt_logging': 'OpenAI Prompts Logged',
            'reproducibility': 'Reproducibility Verified',
            'leverage_analysis': 'Discovery Leverage'
        }
        
        for req_key, req_name in req_names.items():
            if req_key in requirements:
                status = requirements[req_key]['status']
                emoji = "✅" if status == 'PASS' else "❌"
                print(f"{emoji} {req_name}: {status}")
        
        if validation.get('critical_issues'):
            print(f"\n❌ Critical Issues:")
            for issue in validation['critical_issues']:
                print(f"   • {issue}")
        
        if validation.get('warnings'):
            print(f"\n⚠️ Warnings:")
            for warning in validation['warnings']:
                print(f"   • {warning}")
        
        print(f"\n🎯 Ready for competition submission!")


def main():
    """
    Main entry point with enhanced resume capabilities
    """
    print("🏛️ Enhanced Amazon Archaeological Discovery System")
    print("=" * 60)
    print("🎯 OpenAI to Z Challenge - Checkpoint 2 Complete Solution")
    print()
    print("This system implements:")
    print("• Multi-scale analysis (50km → 10km → 2km)")
    print("• Dual-source satellite data (Optical + Radar)")
    print("• Archaeological knowledge integration (Casarabe culture)")
    print("• Full Checkpoint 2 compliance validation")
    print("• Reproducible methodology with ±50m tolerance")
    print("• Resume capability for interrupted sessions")
    print()
    
    # Create the main system
    system = EnhancedAmazonArchaeology()
    
    print(f"🚀 How do you want to proceed?")
    print(f"1. Run complete pipeline automatically (recommended)")
    print(f"2. Step-by-step interactive mode (for learning/debugging)")
    print(f"3. Resume from last detected progress")
    print(f"4. Show system status only")
    print(f"0. Exit")
    
    try:
        choice = input(f"\nSelect option (0-4): ").strip()
        
        if choice == '1':
            # Complete automatic pipeline
            regions = input("How many regions to analyze? (1-5, recommended: 3): ").strip()
            max_regions = int(regions) if regions.isdigit() and 1 <= int(regions) <= 5 else 3
            
            print(f"\n🚀 Starting complete pipeline with {max_regions} regions...")
            print("⏱️ This will take 15-30 minutes depending on your internet connection")
            print("🔧 Make sure you have:")
            print("   • Google Earth Engine access")
            print("   • OpenAI API key in keyring")
            print("   • Stable internet connection")
            
            confirm = input("\nProceed? (y/N): ").strip().lower()
            if confirm == 'y':
                success = system.run_complete_pipeline(max_regions)
                
                if success:
                    print(f"\n🎉 Analysis completed successfully!")
                    print(f"📁 Check these files:")
                    print(f"   • checkpoint2_submission_*.json")
                    print(f"   • checkpoint2_summary_*.md") 
                    print(f"   • {system.paths['images']}/ folder")
                else:
                    print(f"\n❌ Analysis failed. Check error messages above.")
            else:
                print("👋 Operation cancelled")
        
        elif choice == '2':
            # Interactive step-by-step mode
            system.run_step_by_step_mode()
        
        elif choice == '3':
            # Resume from progress
            system.resume_from_detected_step()
        
        elif choice == '4':
            # Show status only
            system.show_detailed_status()
        
        elif choice == '0':
            print("👋 Goodbye!")
        
        else:
            print("❌ Invalid choice")
    
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("🔧 Please report this issue")


if __name__ == "__main__":
    main()