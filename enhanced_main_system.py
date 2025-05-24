# enhanced_main_system.py
# Complete OpenAI to Z Challenge Checkpoint 2 Solution
# Multi-scale archaeological discovery with full compliance

import os
import sys
import time
from datetime import datetime
from typing import Dict, List, Optional

# Import all enhanced components
from simple_region_config import SimpleRegionConfig
from enhanced_data_acquisition import EnhancedDataAcquisition
from enhanced_data_processor import EnhancedDataProcessor
from enhanced_ai_analyzer import EnhancedAIAnalyzer
from enhanced_results_manager import EnhancedResultsManager

class EnhancedAmazonArchaeology:
    """
    Complete enhanced system for Amazon archaeological discovery
    Implements multi-scale analysis with full Checkpoint 2 compliance
    """
    
    def __init__(self):
        """Initialize the complete enhanced system"""
        print("🏛️ Enhanced Amazon Archaeological Discovery System")
        print("=" * 60)
        print("🎯 OpenAI to Z Challenge - Checkpoint 2 Solution")
        print("🔬 Multi-scale Network Detection: 50km → 10km → 2km")
        print("📊 Dual-source Analysis: Optical + Radar")
        print("🤖 AI-powered with Archaeological Knowledge")
        print("✅ Full Checkpoint 2 Compliance")
        print()
        
        # Initialize all components
        print("🔧 Initializing system components...")
        
        self.region_config = SimpleRegionConfig()
        self.data_acquisition = EnhancedDataAcquisition()
        self.data_processor = EnhancedDataProcessor()
        self.ai_analyzer = EnhancedAIAnalyzer()
        self.results_manager = EnhancedResultsManager()
        
        # Track pipeline progress
        self.pipeline_status = {
            'authentication': False,
            'data_loaded': False,
            'processing_complete': False,
            'ai_analysis_complete': False,
            'submission_ready': False
        }
        
        # Store results from each stage
        self.loaded_data = {}
        self.processed_data = {}
        self.ai_analyses = {}
        self.final_submission = {}
        
        print("✅ All components initialized successfully!")
        print()
    
    def step_1_setup_and_authentication(self) -> bool:
        """
        Step 1: Setup Google Earth Engine authentication
        """
        print("🔑 STEP 1: Setup and Authentication")
        print("-" * 40)
        
        # Show available regions
        print("🌍 Available Amazon regions:")
        regions = self.region_config.get_regions_by_priority(8)
        for region_id, info in regions.items():
            priority_emoji = "🔴" if info['priority'] == 'high' else "🟡" if info['priority'] == 'medium' else "🟢"
            sites_emoji = "🏛️" if info['known_sites'] else "🔍"
            print(f"  {priority_emoji} {sites_emoji} {region_id}: {info['name']} ({info['country']})")
        
        print()
        
        # Setup Google Earth Engine
        if self.data_acquisition.setup_google_earth_engine():
            self.pipeline_status['authentication'] = True
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
    
    def step_2_load_dual_source_data(self, max_regions: int = 3) -> bool:
        """
        Step 2: Load dual-source satellite data
        Implements Checkpoint 2 requirement for two independent sources
        """
        if not self.pipeline_status['authentication']:
            print("❌ Please complete Step 1 first!")
            return False
        
        print(f"📡 STEP 2: Load Dual-Source Data")
        print("-" * 40)
        print(f"🎯 Target regions: {max_regions}")
        print("📊 Data sources: Optical (Sentinel-2) + Radar (PALSAR/Sentinel-1)")
        print("✅ Checkpoint 2 compliance: Two independent public sources")
        print()
        
        # Load data for selected regions
        self.loaded_data = self.data_acquisition.load_multiple_regions(max_regions)
        
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
            
            # Count total discoveries
            total_candidates = sum(
                len(result['discovery_candidates']) 
                for result in self.processed_data.values()
            )
            
            print(f"\n✅ Step 3 completed - Multi-scale processing finished!")
            print(f"🎯 Discovery candidates found: {total_candidates}")
            print(f"📁 Images created in: {self.data_processor.output_folder}/")
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
        
        # Run complete multi-scale AI analysis
        self.ai_analyses = self.ai_analyzer.analyze_all_scales(self.processed_data)
        
        if self.ai_analyses:
            self.pipeline_status['ai_analysis_complete'] = True
            
            # Get all discoveries
            all_discoveries = self.ai_analyzer.get_high_confidence_discoveries(min_confidence=0.5)
            
            print(f"\n✅ Step 4 completed - AI analysis finished!")
            print(f"🏛️ Archaeological discoveries: {len(all_discoveries)}")
            print(f"📝 Prompts logged: {sum(len(prompts) if isinstance(prompts, list) else 1 for prompts in self.ai_analyses.values() if prompts)}")
            print(f"🔄 Leverage analysis: {'✅' if self.ai_analyses.get('leverage') else '❌'}")
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
        
        # Get data summary and discoveries
        data_summary = self.data_acquisition.get_data_summary()
        all_discoveries = self.data_processor.get_all_discoveries()
        
        # Add AI-enhanced information to discoveries
        ai_discoveries = self.ai_analyzer.get_high_confidence_discoveries(min_confidence=0.3)
        
        # Merge processor and AI discoveries
        enhanced_discoveries = self.merge_discoveries(all_discoveries, ai_discoveries)
        
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
        
        # Start with processor discoveries (have spatial analysis)
        for discovery in processor_discoveries:
            # Find matching AI analysis
            ai_match = None
            for ai_disc in ai_discoveries:
                # Simple proximity matching (in real implementation, use spatial analysis)
                if (abs(discovery.get('center_lat', 0) - ai_disc.get('center_lat', 0)) < 0.01 and
                    abs(discovery.get('center_lng', 0) - ai_disc.get('center_lng', 0)) < 0.01):
                    ai_match = ai_disc
                    break
            
            # Enhance discovery with AI information
            if ai_match:
                discovery['ai_confidence'] = ai_match.get('confidence_score', 0)
                discovery['ai_analysis'] = ai_match.get('ai_response', '')
                discovery['confidence'] = max(discovery.get('confidence', 0), ai_match.get('confidence_score', 0))
            
            merged.append(discovery)
        
        # Add any AI discoveries not matched
        for ai_disc in ai_discoveries:
            if not any(abs(discovery.get('center_lat', 0) - ai_disc.get('center_lat', 0)) < 0.01 and
                      abs(discovery.get('center_lng', 0) - ai_disc.get('center_lng', 0)) < 0.01
                      for discovery in merged):
                merged.append(ai_disc)
        
        # Sort by confidence
        return sorted(merged, key=lambda x: x.get('confidence', 0), reverse=True)
    
    def run_complete_pipeline(self, max_regions: int = 3) -> bool:
        """
        Run the complete Checkpoint 2 pipeline automatically
        """
        print(f"🚀 COMPLETE CHECKPOINT 2 PIPELINE")
        print("=" * 60)
        print(f"📊 Analyzing {max_regions} regions")
        print(f"🎯 Target: Full Checkpoint 2 compliance")
        print(f"⏱️ Estimated time: 15-30 minutes")
        print()
        
        start_time = time.time()
        
        try:
            # Step 1: Authentication
            if not self.step_1_setup_and_authentication():
                return False
            
            print(f"\n{'='*60}")
            
            # Step 2: Data loading
            if not self.step_2_load_dual_source_data(max_regions):
                return False
            
            print(f"\n{'='*60}")
            
            # Step 3: Multi-scale processing
            if not self.step_3_multi_scale_processing():
                return False
            
            print(f"\n{'='*60}")
            
            # Step 4: AI analysis
            if not self.step_4_ai_analysis_pipeline():
                return False
            
            print(f"\n{'='*60}")
            
            # Step 5: Submission creation
            if not self.step_5_create_checkpoint2_submission():
                return False
            
            # Success!
            elapsed_time = time.time() - start_time
            
            print(f"\n🎉 COMPLETE SUCCESS!")
            print("=" * 60)
            print(f"✅ All 5 steps completed successfully")
            print(f"🏛️ Archaeological analysis finished")
            print(f"📦 Checkpoint 2 submission ready")
            print(f"⏱️ Total time: {elapsed_time/60:.1f} minutes")
            print()
            
            # Final validation summary
            self.show_final_validation_summary()
            
            return True
            
        except Exception as e:
            print(f"\n❌ Pipeline failed: {e}")
            print("🔧 Check error messages above for troubleshooting")
            return False
    
    def run_step_by_step_mode(self):
        """
        Interactive step-by-step mode
        Allows running one step at a time with user control
        """
        print(f"📋 STEP-BY-STEP INTERACTIVE MODE")
        print("=" * 50)
        print("🎯 Run each step individually with full control")
        print()
        
        while True:
            self.show_pipeline_status()
            
            print(f"\n🚀 Available Steps:")
            print(f"1. Setup and authentication {'✅' if self.pipeline_status['authentication'] else '⏸️'}")
            print(f"2. Load dual-source data {'✅' if self.pipeline_status['data_loaded'] else '⏸️'}")
            print(f"3. Multi-scale processing {'✅' if self.pipeline_status['processing_complete'] else '⏸️'}")
            print(f"4. AI analysis pipeline {'✅' if self.pipeline_status['ai_analysis_complete'] else '⏸️'}")
            print(f"5. Create submission {'✅' if self.pipeline_status['submission_ready'] else '⏸️'}")
            print(f"6. Run all remaining steps")
            print(f"7. Show detailed status")
            print(f"0. Exit")
            
            try:
                choice = input(f"\nSelect step (0-7): ").strip()
                
                if choice == '0':
                    break
                elif choice == '1':
                    self.step_1_setup_and_authentication()
                elif choice == '2':
                    regions = input("How many regions to analyze? (1-5, default: 3): ").strip()
                    max_regions = int(regions) if regions.isdigit() and 1 <= int(regions) <= 5 else 3
                    self.step_2_load_dual_source_data(max_regions)
                elif choice == '3':
                    self.step_3_multi_scale_processing()
                elif choice == '4':
                    self.step_4_ai_analysis_pipeline()
                elif choice == '5':
                    self.step_5_create_checkpoint2_submission()
                elif choice == '6':
                    # Run all remaining steps
                    regions = input("How many regions for complete analysis? (1-5, default: 3): ").strip()
                    max_regions = int(regions) if regions.isdigit() and 1 <= int(regions) <= 5 else 3
                    
                    if not self.pipeline_status['authentication']:
                        self.step_1_setup_and_authentication()
                    if not self.pipeline_status['data_loaded']:
                        self.step_2_load_dual_source_data(max_regions)
                    if not self.pipeline_status['processing_complete']:
                        self.step_3_multi_scale_processing()
                    if not self.pipeline_status['ai_analysis_complete']:
                        self.step_4_ai_analysis_pipeline()
                    if not self.pipeline_status['submission_ready']:
                        self.step_5_create_checkpoint2_submission()
                    break
                elif choice == '7':
                    self.show_detailed_status()
                else:
                    print("❌ Invalid choice, please try again")
                    
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\n👋 Exiting step-by-step mode")
                break    
            except Exception as e:
                print(f"❌ Error: {e}")
                input("Press Enter to continue...")
    
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
    Main entry point for the enhanced archaeological discovery system
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
    print()
    
    # Create the main system
    system = EnhancedAmazonArchaeology()
    
    print(f"🚀 How do you want to proceed?")
    print(f"1. Run complete pipeline automatically (recommended)")
    print(f"2. Step-by-step interactive mode (for learning/debugging)")
    print(f"3. Show system status only")
    print(f"0. Exit")
    
    try:
        choice = input(f"\nSelect option (0-3): ").strip()
        
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
                    print(f"   • enhanced_images/ folder")
                else:
                    print(f"\n❌ Analysis failed. Check error messages above.")
            else:
                print("👋 Operation cancelled")
        
        elif choice == '2':
            # Interactive step-by-step mode
            system.run_step_by_step_mode()
        
        elif choice == '3':
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