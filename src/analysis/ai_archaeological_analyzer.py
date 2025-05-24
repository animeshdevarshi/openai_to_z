# Archaeological AI Analyzer
# AI analysis with archaeologically-informed prompts
# Implements scale-specific analysis and discovery leveraging

import os
import json
import base64
from datetime import datetime
from typing import List, Dict, Optional
from openai import OpenAI
from dotenv import load_dotenv
import keyring
import time
import re

# Import from organized structure
from config.output_paths import get_paths, get_ai_analysis_path
from config.prompt_database import PromptConfig


class EnhancedAIAnalyzer:
    """
    Enhanced AI analyzer with archaeological knowledge integration
    Uses scale-specific prompts and discovery leveraging from prompt database
    """
    
    def __init__(self):
        """Initialize with archaeological knowledge base and prompt database"""
        # Load environment variables
        load_dotenv()
        
        # Get organized output paths
        self.paths = get_paths()
        
        # Initialize prompt database
        self.prompt_config = PromptConfig()
        
        self.ai_responses = []
        self.discoveries = []
        self.prompts_used = {
            'regional': [],
            'zone': [],
            'site': [],
            'leverage': []
        }
        
        # Use knowledge base from prompt config
        self.casarabe_knowledge = self.prompt_config.casarabe_knowledge
        
        print("🤖 Enhanced Archaeological AI Analyzer initialized")
        print("🏛️ Loaded Casarabe culture knowledge base from prompt database")
        print("📝 Prompt database ready")
        print("📊 Scale-specific prompting ready")
        print(f"💾 Output directory: {self.paths['analysis_results']}")
    
    def create_regional_prompt(self, region_info: Dict, images: Dict) -> str:
        """Create prompt using prompt database"""
        return self.prompt_config.get_regional_prompt(region_info, images)
    
    def create_zone_prompt(self, zone_info: Dict, images: Dict) -> str:
        """Create prompt using prompt database"""
        return self.prompt_config.get_zone_prompt(zone_info, images)
    
    def create_site_prompt(self, site_info: Dict, images: Dict) -> str:
        """Create prompt using prompt database"""
        return self.prompt_config.get_site_prompt(site_info, images)
    
    def create_leverage_prompt(self, initial_discoveries: List[Dict], search_region: Dict) -> str:
        """Create prompt using prompt database"""
        return self.prompt_config.get_leverage_prompt(initial_discoveries, search_region)
    
    def analyze_discovery_patterns(self, discoveries: List[Dict]) -> Dict:
        """Analyze patterns in discovered sites for leverage prompting"""
        if not discoveries:
            return {}
        
        # Calculate statistics
        sizes = [d.get('features', {}).get('area_hectares', 50) for d in discoveries]
        rings = [d.get('features', {}).get('defensive_rings', 1) for d in discoveries]
        tiers = [d.get('site_tier', 'Secondary') for d in discoveries]
        
        patterns = {
            'avg_size_ha': sum(sizes) / len(sizes) if sizes else 50,
            'avg_rings': sum(rings) / len(rings) if rings else 1,
            'common_features': ['defensive_rings', 'raised_platforms', 'geometric_regularity'],
            'tier_distribution': f"{tiers.count('Primary')} Primary, {tiers.count('Secondary')} Secondary",
            'primary_count': tiers.count('Primary'),
            'secondary_count': tiers.count('Secondary'),
            'elevation_range': '100-300',
            'causeway_directions': 'NNW, NE',
            'typical_spacing_km': 3.5,
            'vegetation_signature': 'disturbed_canopy_patterns',
            'preferred_setting': 'slightly_elevated_near_water',
            'avoided_settings': 'steep_slopes_and_wetlands',
            'signature_indicators': 'geometric_vegetation_patterns'
        }
        
        return patterns
    
    def call_ai_model(self, prompt: str, image_path: str, analysis_scale: str = 'zone') -> Optional[str]:
        """
        Call AI model with image and prompt
        Uses OpenAI GPT-4 Vision API
        """
        
        # MOCK MODE for testing (remove when ready for real AI calls)
        print(f"🤖 MOCK AI analysis for {analysis_scale} scale...")
        print(f"📸 Would analyze: {os.path.basename(image_path)}")
        
        # Return mock JSON responses for testing
        if analysis_scale == 'regional':
            return """{
  "analysis_type": "regional_network",
  "region_name": "Colombian Amazon",
  "coordinates": "0.0, -70.0",
  "settlement_clusters": [
    {
      "cluster_id": 1,
      "center_coordinates": "-1.0667, -70.1459",
      "cluster_size_km": 5.0,
      "site_count_estimate": 3,
      "primary_centers": 1,
      "secondary_centers": 2,
      "confidence": 0.8
    }
  ],
  "causeway_networks": [],
  "priority_zones": [
    {
      "zone_id": 1,
      "center_coordinates": "-1.0667, -70.1459",
      "priority_level": "high",
      "expected_site_type": "primary",
      "reasoning": "Large geometric features detected"
    }
  ],
  "overall_assessment": {
    "network_hierarchy_detected": true,
    "total_clusters_found": 1,
    "total_causeways_found": 0,
    "confidence_score": 0.8,
    "recommended_detailed_analysis": true
  }
}"""
        
        elif analysis_scale == 'zone':
            return """{
  "analysis_type": "zone_site_detection",
  "zone_id": "test_zone",
  "zone_center": "-1.0667, -70.1459",
  "sites_detected": [
    {
      "site_id": "site_001",
      "center_coordinates": "-1.0667, -70.1459",
      "site_type": "secondary",
      "diameter_meters": 400,
      "defensive_rings": 1,
      "features_detected": ["concentric_rings", "raised_platform"],
      "data_sources_visible": ["optical", "radar"],
      "measurements": {
        "outer_ring_diameter_m": 400,
        "inner_platform_size_m": 200,
        "estimated_area_hectares": 20
      },
      "context": {
        "elevation": "elevated",
        "water_proximity": true,
        "forest_disturbance": false
      },
      "confidence_score": 0.7,
      "geometric_regularity": 0.8,
      "archaeological_probability": 0.7
    },
    {
      "site_id": "site_002",
      "center_coordinates": "-1.0700, -70.1500",
      "site_type": "tertiary",
      "diameter_meters": 150,
      "defensive_rings": 0,
      "features_detected": ["raised_platform"],
      "data_sources_visible": ["optical"],
      "measurements": {
        "outer_ring_diameter_m": 150,
        "inner_platform_size_m": 100,
        "estimated_area_hectares": 5
      },
      "context": {
        "elevation": "elevated",
        "water_proximity": false,
        "forest_disturbance": false
      },
      "confidence_score": 0.6,
      "geometric_regularity": 0.6,
      "archaeological_probability": 0.6
    }
  ],
  "linear_features": [],
  "zone_summary": {
    "total_sites_detected": 2,
    "primary_sites": 0,
    "secondary_sites": 1,
    "geometric_features_count": 2,
    "zone_confidence": 0.65,
    "recommend_site_analysis": true
  }
}"""
        
        elif analysis_scale == 'site':
            return """{
  "analysis_type": "site_detailed_mapping",
  "site_id": "detailed_site_001",
  "site_center": "-1.0667, -70.1459",
  "defensive_structures": {
    "concentric_rings": [
      {
        "ring_number": 1,
        "diameter_meters": 400,
        "type": "rampart",
        "completeness": 0.9,
        "preservation": "good"
      }
    ],
    "entrance_gaps": [
      {
        "gap_id": 1,
        "location": "north",
        "width_meters": 30,
        "causeway_connection": false
      }
    ]
  },
  "central_architecture": {
    "raised_platforms": [
      {
        "platform_id": 1,
        "dimensions": "200m x 150m",
        "height_estimate_m": 3,
        "shape": "rectangular",
        "function": "ceremonial"
      }
    ],
    "pyramid_mounds": [],
    "plaza_areas": [
      {
        "plaza_id": 1,
        "dimensions": "100m x 100m",
        "surface_type": "prepared"
      }
    ]
  },
  "site_connections": [],
  "site_measurements": {
    "overall_diameter_m": 400,
    "total_area_hectares": 20,
    "defensive_area_hectares": 12,
    "central_area_hectares": 3
  },
  "site_classification": {
    "tier": "secondary",
    "confidence": 0.8,
    "classification_criteria": ["single_ring", "large_platform"]
  },
  "preservation_assessment": {
    "overall_preservation": "good",
    "modern_disturbances": false,
    "disturbance_types": [],
    "archaeological_integrity": 0.8
  },
  "final_assessment": {
    "archaeological_confidence": 0.8,
    "site_significance": "high",
    "recommended_for_submission": true,
    "additional_analysis_needed": false
  }
}"""
        
        elif analysis_scale == 'leverage':
            return """{
  "analysis_type": "leverage_discovery",
  "leveraging_patterns": {
    "site_size_distribution": {
      "primary_sites_diameter_m": [800, 1200],
      "secondary_sites_diameter_m": [300, 500],
      "tertiary_sites_diameter_m": [100, 200]
    },
    "defensive_features": {
      "concentric_rings_common": true,
      "average_rings_per_site": 1.2,
      "entrance_gap_orientation": "north_south_preferred"
    },
    "spatial_relationships": {
      "inter_site_distance_primary_km": [2.5, 4.0],
      "inter_site_distance_secondary_km": [1.0, 2.0],
      "network_hierarchy_confirmed": true
    }
  },
  "pattern_based_discoveries": [
    {
      "discovery_id": "leverage_001",
      "center_coordinates": "-8.025, -74.350",
      "predicted_type": "secondary",
      "confidence_based_on_pattern": 0.85,
      "matching_patterns": ["size_range", "defensive_rings", "spatial_position"]
    },
    {
      "discovery_id": "leverage_002", 
      "center_coordinates": "-8.080, -74.420",
      "predicted_type": "tertiary",
      "confidence_based_on_pattern": 0.75,
      "matching_patterns": ["size_range", "spatial_position"]
    }
  ],
  "leverage_recommendations": {
    "search_priority_areas": [
      {
        "area_id": "priority_001",
        "center_coordinates": "-8.060, -74.380",
        "search_radius_km": 1.5,
        "expected_site_type": "secondary",
        "reasoning": "Optimal spacing from known primary center"
      }
    ],
    "refined_detection_criteria": {
      "size_thresholds_updated": true,
      "geometric_regularity_threshold": 0.7,
      "defensive_feature_weight_increased": true
    }
  },
  "leverage_success": {
    "initial_discoveries_analyzed": 19,
    "pattern_learning_confidence": 0.85,
    "new_discoveries_predicted": 2,
    "search_efficiency_improvement": 0.40,
    "recommended_next_analysis": "continue_leverage"
  }
}"""
        
        # For real AI calls, uncomment this code:
        """
        try:
            # Get API key from environment variable
            api_key = os.getenv('OPENAI_API_KEY')
            if not api_key:
                print("❌ OpenAI API key not found in environment variables")
                return None
            
            client = OpenAI(api_key=api_key)
            
            # Encode image
            with open(image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            
            print(f"🤖 Calling AI model for {analysis_scale} analysis...")
            print(f"📸 Image: {os.path.basename(image_path)}")
            print(f"📝 Prompt length: {len(prompt)} characters")
            
            # Call OpenAI API
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {
                                "type": "image_url",
                                "image_url": {"url": f"data:image/png;base64,{encoded_image}"}
                            }
                        ]
                    }
                ],
                max_tokens=1000,
                response_format={"type": "json_object"}
            )
            
            ai_response = response.choices[0].message.content
            print(f"✅ AI analysis completed ({len(ai_response)} characters)")
            
            return ai_response
            
        except Exception as e:
            print(f"❌ AI model call failed: {e}")
            return None
        """
    
    def analyze_regional_scale(self, region_results: Dict) -> Optional[Dict]:
        """Analyze at regional scale for network detection"""
        region_name = region_results['region_name']
        images = region_results['scales']['regional']['images']
        
        print(f"🌍 Regional AI analysis: {region_name}")
        
        # Use archaeological heatmap for analysis
        if 'archaeological_heatmap' in images and images['archaeological_heatmap']:
            prompt = self.create_regional_prompt(region_results, images)
            
            ai_response = self.call_ai_model(
                prompt, 
                images['archaeological_heatmap'], 
                'regional'
            )
            
            if ai_response:
                analysis = {
                    'scale': 'regional',
                    'region_name': region_name,
                    'image_analyzed': images['archaeological_heatmap'],
                    'prompt': prompt,
                    'ai_response': ai_response,
                    'analysis_timestamp': datetime.now().isoformat()
                }
                
                self.ai_responses.append(analysis)
                return analysis
        
        return None
    
    def analyze_zone_scale(self, zone_results: List[Dict]) -> List[Dict]:
        """Analyze at zone scale for site detection"""
        zone_analyses = []
        
        print(f"🔍 Zone AI analysis: {len(zone_results)} zones")
        
        for zone in zone_results:
            zone_id = zone['zone_id']
            images = zone['images']
            
            print(f"   Analyzing zone {zone_id}...")
            
            # Use optical image for detailed analysis
            if 'optical' in images and images['optical']:
                prompt = self.create_zone_prompt(zone, images)
                
                ai_response = self.call_ai_model(
                    prompt,
                    images['optical'],
                    'zone'
                )
                
                if ai_response:
                    analysis = {
                        'scale': 'zone',
                        'zone_id': zone_id,
                        'zone_center': zone['zone_center'],
                        'image_analyzed': images['optical'],
                        'prompt': prompt,
                        'ai_response': ai_response,
                        'analysis_timestamp': datetime.now().isoformat()
                    }
                    
                    self.ai_responses.append(analysis)
                    zone_analyses.append(analysis)
                    
                    # Extract discoveries from response
                    discoveries = self.extract_discoveries_from_response(analysis, 'zone')
                    self.discoveries.extend(discoveries)
        
        return zone_analyses
    
    def analyze_site_scale(self, site_results: List[Dict]) -> List[Dict]:
        """Analyze at site scale for detailed confirmation"""
        site_analyses = []
        
        print(f"🎯 Site AI analysis: {len(site_results)} sites")
        
        for site in site_results:
            site_id = site['site_id']
            images = site['images']
            
            print(f"   Analyzing site {site_id}...")
            
            if 'optical' in images and images['optical']:
                prompt = self.create_site_prompt(site, images)
                
                ai_response = self.call_ai_model(
                    prompt,
                    images['optical'],
                    'site'
                )
                
                if ai_response:
                    analysis = {
                        'scale': 'site',
                        'site_id': site_id,
                        'site_center': [site['center_lat'], site['center_lng']],
                        'image_analyzed': images['optical'],
                        'prompt': prompt,
                        'ai_response': ai_response,
                        'analysis_timestamp': datetime.now().isoformat()
                    }
                    
                    self.ai_responses.append(analysis)
                    site_analyses.append(analysis)
                    
                    # Update site confidence based on AI analysis
                    ai_confidence = self.extract_confidence_from_response(ai_response)
                    if ai_confidence:
                        site['ai_confidence'] = ai_confidence
                        site['confidence'] = max(site.get('confidence', 0), ai_confidence)
        
        return site_analyses
    
    def perform_leverage_analysis(self, all_discoveries: List[Dict], region_data: Dict) -> Optional[Dict]:
        """
        Perform leverage analysis using discovered patterns
        This satisfies Checkpoint 2's re-prompting requirement
        """
        if not all_discoveries:
            print("⚠️ No discoveries to leverage")
            return None
        
        print(f"🔄 Leverage analysis: Using {len(all_discoveries)} discoveries")
        
        # Create leverage prompt
        prompt = self.create_leverage_prompt(all_discoveries, region_data)
        
        # Use regional archaeological heatmap for leverage analysis
        heatmap_path = None
        for region_id, results in region_data.items():
            if 'scales' in results and 'regional' in results['scales']:
                images = results['scales']['regional']['images']
                if 'archaeological_heatmap' in images:
                    heatmap_path = images['archaeological_heatmap']
                    break
        
        if heatmap_path:
            ai_response = self.call_ai_model(prompt, heatmap_path, 'leverage')
            
            if ai_response:
                leverage_analysis = {
                    'type': 'leverage_analysis',
                    'initial_discoveries': len(all_discoveries),
                    'prompt': prompt,
                    'ai_response': ai_response,
                    'analysis_timestamp': datetime.now().isoformat()
                }
                
                self.ai_responses.append(leverage_analysis)
                print("✅ Leverage analysis completed")
                return leverage_analysis
        
        return None
    
    def extract_discoveries_from_response(self, analysis: Dict, scale: str) -> List[Dict]:
        """Extract archaeological discoveries from AI JSON response"""
        discoveries = []
        ai_response = analysis['ai_response']
        
        try:
            # Parse JSON response
            response_data = json.loads(ai_response)
            
            if scale == 'regional':
                # Extract from regional analysis
                if 'settlement_clusters' in response_data:
                    for i, cluster in enumerate(response_data['settlement_clusters']):
                        if cluster.get('confidence', 0) >= 0.3:  # Lowered threshold
                            # Parse coordinates
                            coords_str = cluster.get('center_coordinates', '0, 0')
                            try:
                                if ',' in coords_str:
                                    lat_str, lng_str = coords_str.split(',')
                                    center_lat = float(lat_str.strip())
                                    center_lng = float(lng_str.strip())
                                else:
                                    center_lat, center_lng = 0, 0
                            except:
                                center_lat, center_lng = 0, 0
                            
                            discovery = {
                                'id': f"regional_cluster_{i+1:03d}",
                                'analysis_scale': 'regional',
                                'type': 'settlement_cluster',
                                'center_lat': center_lat,
                                'center_lng': center_lng,
                                'center_coordinates': [center_lat, center_lng],
                                'cluster_size_km': cluster.get('cluster_size_km', 0),
                                'site_count_estimate': cluster.get('site_count_estimate', 0),
                                'confidence_score': cluster.get('confidence', 0),
                                'confidence': cluster.get('confidence', 0),  # Duplicate for compatibility
                                'discovery_timestamp': datetime.now().isoformat(),
                                'source_analysis': analysis
                            }
                            discoveries.append(discovery)
                
                if 'priority_zones' in response_data:
                    for i, zone in enumerate(response_data['priority_zones']):
                        if zone.get('priority_level') in ['high', 'medium']:
                            # Parse coordinates 
                            coords_str = zone.get('center_coordinates', '0, 0')
                            try:
                                if ',' in coords_str:
                                    lat_str, lng_str = coords_str.split(',')
                                    center_lat = float(lat_str.strip())
                                    center_lng = float(lng_str.strip())
                                else:
                                    center_lat, center_lng = 0, 0
                            except:
                                center_lat, center_lng = 0, 0
                            
                            discovery = {
                                'id': f"priority_zone_{i+1:03d}",
                                'analysis_scale': 'regional',
                                'type': 'priority_zone',
                                'center_lat': center_lat,
                                'center_lng': center_lng,
                                'center_coordinates': [center_lat, center_lng],
                                'expected_site_type': zone.get('expected_site_type'),
                                'priority_level': zone.get('priority_level'),
                                'confidence_score': 0.7 if zone.get('priority_level') == 'high' else 0.5,
                                'confidence': 0.7 if zone.get('priority_level') == 'high' else 0.5,
                                'discovery_timestamp': datetime.now().isoformat(),
                                'source_analysis': analysis
                            }
                            discoveries.append(discovery)
            
            elif scale == 'zone':
                # Extract from zone analysis
                if 'sites_detected' in response_data:
                    for site in response_data['sites_detected']:
                        if site.get('confidence_score', 0) >= 0.3:  # Lowered threshold
                            # Parse coordinates
                            coords_str = site.get('center_coordinates', '0, 0')
                            try:
                                if ',' in coords_str:
                                    lat_str, lng_str = coords_str.split(',')
                                    center_lat = float(lat_str.strip())
                                    center_lng = float(lng_str.strip())
                                else:
                                    center_lat, center_lng = 0, 0
                            except:
                                center_lat, center_lng = 0, 0
                            
                            discovery = {
                                'id': site.get('site_id', f"zone_site_{len(discoveries)+1:03d}"),
                                'analysis_scale': 'zone',
                                'type': 'archaeological_site',
                                'center_lat': center_lat,
                                'center_lng': center_lng,
                                'center_coordinates': [center_lat, center_lng],
                                'site_type': site.get('site_type'),
                                'diameter_meters': site.get('diameter_meters', 0),
                                'defensive_rings': site.get('defensive_rings', 0),
                                'features_detected': site.get('features_detected', []),
                                'measurements': site.get('measurements', {}),
                                'context': site.get('context', {}),
                                'confidence_score': site.get('confidence_score', 0),
                                'confidence': site.get('confidence_score', 0),
                                'geometric_regularity': site.get('geometric_regularity', 0),
                                'archaeological_probability': site.get('archaeological_probability', 0),
                                'discovery_timestamp': datetime.now().isoformat(),
                                'source_analysis': analysis
                            }
                            discoveries.append(discovery)
                
                if 'linear_features' in response_data:
                    for feature in response_data['linear_features']:
                        if feature.get('confidence', 0) >= 0.3:  # Lowered threshold
                            discovery = {
                                'id': feature.get('feature_id', f"causeway_{len(discoveries)+1:03d}"),
                                'analysis_scale': 'zone',
                                'type': 'linear_feature',
                                'start_coordinates': feature.get('start_coordinates'),
                                'end_coordinates': feature.get('end_coordinates'),
                                'center_lat': 0,  # Will be calculated from start/end
                                'center_lng': 0,
                                'width_meters': feature.get('width_meters', 0),
                                'length_meters': feature.get('length_meters', 0),
                                'orientation': feature.get('orientation'),
                                'connects_sites': feature.get('connects_sites', []),
                                'confidence_score': feature.get('confidence', 0),
                                'confidence': feature.get('confidence', 0),
                                'discovery_timestamp': datetime.now().isoformat(),
                                'source_analysis': analysis
                            }
                            discoveries.append(discovery)
            
            elif scale == 'site':
                # Extract from detailed site analysis
                if response_data.get('final_assessment', {}).get('archaeological_confidence', 0) >= 0.3:
                    # Parse coordinates from site_center
                    site_center = response_data.get('site_center', '0, 0')
                    try:
                        if isinstance(site_center, list) and len(site_center) >= 2:
                            center_lat, center_lng = float(site_center[0]), float(site_center[1])
                        elif ',' in str(site_center):
                            lat_str, lng_str = str(site_center).split(',')
                            center_lat = float(lat_str.strip())
                            center_lng = float(lng_str.strip())
                        else:
                            center_lat, center_lng = 0, 0
                    except:
                        center_lat, center_lng = 0, 0
                    
                    discovery = {
                        'id': response_data.get('site_id', f"detailed_site_{len(discoveries)+1:03d}"),
                        'analysis_scale': 'site',
                        'type': 'detailed_archaeological_site',
                        'center_lat': center_lat,
                        'center_lng': center_lng,
                        'site_center': response_data.get('site_center'),
                        'defensive_structures': response_data.get('defensive_structures', {}),
                        'central_architecture': response_data.get('central_architecture', {}),
                        'site_connections': response_data.get('site_connections', []),
                        'site_measurements': response_data.get('site_measurements', {}),
                        'site_classification': response_data.get('site_classification', {}),
                        'preservation_assessment': response_data.get('preservation_assessment', {}),
                        'confidence_score': response_data.get('final_assessment', {}).get('archaeological_confidence', 0),
                        'confidence': response_data.get('final_assessment', {}).get('archaeological_confidence', 0),
                        'site_significance': response_data.get('final_assessment', {}).get('site_significance'),
                        'recommended_for_submission': response_data.get('final_assessment', {}).get('recommended_for_submission', False),
                        'discovery_timestamp': datetime.now().isoformat(),
                        'source_analysis': analysis
                    }
                    discoveries.append(discovery)
        
        except json.JSONDecodeError as e:
            print(f"⚠️ Failed to parse JSON response: {e}")
            # Fallback to keyword-based extraction
            discoveries = self._fallback_extraction(analysis, scale)
        
        except Exception as e:
            print(f"⚠️ Error processing response: {e}")
            discoveries = self._fallback_extraction(analysis, scale)
        
        return discoveries
    
    def _fallback_extraction(self, analysis: Dict, scale: str) -> List[Dict]:
        """Fallback extraction when JSON parsing fails - extract from text"""
        discoveries = []
        
        try:
            text = analysis.get('ai_response', '').lower()
            
            # Look for coordinate patterns in text
            coord_pattern = r'(-?\d+\.?\d*)\s*,\s*(-?\d+\.?\d*)'
            coordinates = re.findall(coord_pattern, text)
            
            # Look for confidence scores
            confidence_pattern = r'confidence[:\s]*(\d*\.?\d+)'
            confidences = re.findall(confidence_pattern, text)
            
            for i, (lat_str, lng_str) in enumerate(coordinates[:5]):  # Max 5 discoveries
                try:
                    center_lat = float(lat_str)
                    center_lng = float(lng_str)
                    confidence = float(confidences[i]) if i < len(confidences) else 0.5
                    
                    # Normalize confidence to 0-1 range
                    if confidence > 1.0:
                        confidence = confidence / 100.0
                    
                    discovery = {
                        'id': f"fallback_{scale}_{i+1:03d}",
                        'analysis_scale': scale,
                        'type': f'{scale}_fallback_discovery',
                        'center_lat': center_lat,
                        'center_lng': center_lng,
                        'confidence_score': confidence,
                        'confidence': confidence,
                        'source': 'fallback_extraction',
                        'discovery_timestamp': datetime.now().isoformat(),
                        'source_analysis': analysis
                    }
                    discoveries.append(discovery)
                except (ValueError, IndexError):
                    continue
                    
        except Exception as e:
            print(f"⚠️ Fallback extraction failed: {e}")
        
        return discoveries
    
    def extract_confidence_from_response(self, ai_response: str) -> Optional[float]:
        """Extract confidence score from AI response (JSON or text)"""
        try:
            # Try to parse as JSON first
            response_data = json.loads(ai_response)
            
            # Look for confidence in different JSON structures
            if 'overall_assessment' in response_data:
                return response_data['overall_assessment'].get('confidence_score')
            elif 'zone_summary' in response_data:
                return response_data['zone_summary'].get('zone_confidence')
            elif 'final_assessment' in response_data:
                return response_data['final_assessment'].get('archaeological_confidence')
            elif 'leverage_success' in response_data:
                return response_data['leverage_success'].get('pattern_learning_confidence')
            
            # Look for any confidence field in the JSON
            def find_confidence_recursive(obj):
                if isinstance(obj, dict):
                    for key, value in obj.items():
                        if 'confidence' in key.lower():
                            return value
                        elif isinstance(value, (dict, list)):
                            result = find_confidence_recursive(value)
                            if result is not None:
                                return result
                elif isinstance(obj, list):
                    for item in obj:
                        result = find_confidence_recursive(item)
                        if result is not None:
                            return result
                return None
            
            confidence = find_confidence_recursive(response_data)
            if confidence is not None:
                return float(confidence)
        
        except (json.JSONDecodeError, ValueError):
            # Fallback to text-based extraction
            pass
        
        # Text-based extraction as fallback
        response_lower = ai_response.lower()
        
        # Look for confidence indicators
        for line in response_lower.split('\n'):
            if 'confidence' in line:
                words = line.split()
                for word in words:
                    try:
                        if '/' in word:
                            return float(word.split('/')[0]) / 10.0
                        elif word.replace('.', '').isdigit():
                            conf = float(word)
                            return conf / 10.0 if conf > 1 else conf
                    except:
                        continue
        
        # Default confidence based on keywords
        if any(keyword in response_lower for keyword in ['certain', 'definitely', 'clear']):
            return 0.9
        elif any(keyword in response_lower for keyword in ['likely', 'probable']):
            return 0.7
        elif any(keyword in response_lower for keyword in ['possible', 'maybe']):
            return 0.5
        
        return None
    
    def analyze_all_scales(self, processed_data: Dict) -> Dict:
        """
        Perform complete multi-scale AI analysis
        Regional → Zone → Site → Leverage
        """
        print(f"\n🤖 Multi-Scale AI Analysis Pipeline")
        print("=" * 50)
        
        all_analyses = {
            'regional': [],
            'zone': [],
            'site': [],
            'leverage': None
        }
        
        # Stage 1: Regional Analysis
        print("\n🌍 Stage 1: Regional Network Analysis")
        for region_id, results in processed_data.items():
            regional_analysis = self.analyze_regional_scale(results)
            if regional_analysis:
                all_analyses['regional'].append(regional_analysis)
        
        # Stage 2: Zone Analysis
        print("\n🔍 Stage 2: Zone Site Detection")
        for region_id, results in processed_data.items():
            zone_results = results['scales'].get('zones', [])
            if zone_results:
                zone_analyses = self.analyze_zone_scale(zone_results)
                all_analyses['zone'].extend(zone_analyses)
        
        # Stage 3: Site Analysis
        print("\n🎯 Stage 3: Site Confirmation")
        for region_id, results in processed_data.items():
            site_results = results['scales'].get('sites', [])
            if site_results:
                site_analyses = self.analyze_site_scale(site_results)
                all_analyses['site'].extend(site_analyses)
        
        # Stage 4: Leverage Analysis
        print("\n🔄 Stage 4: Discovery Leverage Analysis")
        if self.discoveries:
            leverage_analysis = self.perform_leverage_analysis(self.discoveries, processed_data)
            all_analyses['leverage'] = leverage_analysis
        
        # Summary
        print(f"\n📊 AI ANALYSIS SUMMARY:")
        print("=" * 30)
        print(f"🌍 Regional analyses: {len(all_analyses['regional'])}")
        print(f"🔍 Zone analyses: {len(all_analyses['zone'])}")
        print(f"🎯 Site analyses: {len(all_analyses['site'])}")
        print(f"🔄 Leverage analysis: {'✅' if all_analyses['leverage'] else '❌'}")
        print(f"🏛️ Total discoveries: {len(self.discoveries)}")
        
        return all_analyses
    
    def get_all_prompts_used(self) -> Dict:
        """Get all prompts used for Checkpoint 2 compliance"""
        return self.prompts_used
    
    def get_high_confidence_discoveries(self, min_confidence: float = 0.7) -> List[Dict]:
        """Get discoveries above confidence threshold"""
        return [
            d for d in self.discoveries 
            if d.get('confidence_score', 0) >= min_confidence
        ]
    
    def save_analysis_results(self, filename: str = None) -> str:
        """Save all analysis results to organized output folder"""
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            # Use organized path for AI analysis files
            output_file = get_ai_analysis_path(timestamp)
        else:
            # Use organized ai_responses subdirectory
            paths = get_paths()
            output_file = os.path.join(paths['ai_responses'], filename)
        
        results = {
            'analysis_timestamp': datetime.now().isoformat(),
            'total_analyses': len(self.ai_responses),
            'total_discoveries': len(self.discoveries),
            'prompts_used': self.prompts_used,
            'ai_responses': self.ai_responses,
            'discoveries': self.discoveries,
            'casarabe_knowledge_base': self.casarabe_knowledge
        }
        
        try:
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"💾 Analysis results saved to {output_file}")
            return output_file
        except Exception as e:
            print(f"❌ Could not save results: {e}")
            return None


# Test the enhanced AI analyzer
if __name__ == "__main__":
    print("🏛️ Enhanced Archaeological AI Analyzer Test")
    print("=" * 50)
    
    analyzer = EnhancedAIAnalyzer()
    
    print(f"\n✅ AI analyzer ready!")
    print(f"🏛️ Casarabe knowledge base loaded from prompt database")
    print(f"📊 Scale-specific prompts: Regional, Zone, Site, Leverage")
    print(f"🔧 Replace os.getenv('OPENAI_API_KEY') with your OpenAI API key")
    print(f"🤖 Ready for archaeological discovery!")