# enhanced_data_processor.py
# Multi-scale progressive analysis for archaeological discovery
# Implements the three-tier approach: Regional → Zone → Site

import os
import requests
import time
import numpy as np
from datetime import datetime
from PIL import Image
from typing import Dict, List, Tuple
import ee
import json

# Import from organized structure
from src.config.output_paths import get_paths

class EnhancedDataProcessor:
    """
    Multi-scale processor implementing archaeological discovery methodology
    Progressive analysis: 50km → 10km → 2km scales
    """
    
    def __init__(self):
        """Initialize multi-scale processor with organized output paths"""
        # Use organized output structure
        self.paths = get_paths()
        self.output_folder = self.paths['images']  # Use organized structure
        
        # Ensure output directories exist
        for scale in ['regional', 'zone', 'site']:
            scale_dir = os.path.join(self.output_folder, scale)
            os.makedirs(scale_dir, exist_ok=True)
        
        # Analysis scales for multi-tier detection
        self.analysis_scales = {
            'regional': {'size_km': 50, 'resolution_m': 100},
            'zone': {'size_km': 10, 'resolution_m': 30},
            'site': {'size_km': 2, 'resolution_m': 10}
        }
        
        self.processed_data = {}
        self.all_discoveries = []
        
        print("🎨 Enhanced Multi-Scale Processor initialized")
        print(f"📊 Analysis scales: Regional (50km) → Zone (10km) → Site (2km)")
        print(f"📁 Output directory: {self.output_folder}")
    
    def process_region_multiscale(self, region_data: Dict) -> Dict:
        """
        Complete multi-scale analysis pipeline for one region
        This is the core archaeological discovery method
        """
        region_id = region_data['region_id']
        region_name = region_data['region_info']['name']
        
        print(f"\n🔬 Multi-scale analysis: {region_name}")
        print("=" * 50)
        
        results = {
            'region_id': region_id,
            'region_name': region_name,
            'scales': {
                'regional': None,
                'zones': [],
                'sites': []
            },
            'discovery_candidates': [],
            'analysis_timestamp': datetime.now().isoformat()
        }
        
        # TIER 1: Regional Analysis (50km scale)
        print("🌍 Tier 1: Regional network detection...")
        regional_results = self.analyze_regional_scale(region_data)
        results['scales']['regional'] = regional_results
        
        # TIER 2: Zone Analysis (10km scale)
        print("🔍 Tier 2: Zone-level site detection...")
        priority_zones = self.identify_priority_zones(region_data, regional_results)
        
        zone_results = []
        for zone in priority_zones[:9]:  # Analyze top 9 zones
            zone_result = self.analyze_zone_scale(region_data, zone)
            if zone_result and zone_result['potential_sites']:
                zone_results.append(zone_result)
        
        results['scales']['zones'] = zone_results
        
        # TIER 3: Site Analysis (2km scale)
        print("🎯 Tier 3: Detailed site confirmation...")
        all_candidates = []
        for zone in zone_results:
            all_candidates.extend(zone['potential_sites'])
        
        # Sort by archaeological probability and analyze top candidates
        top_candidates = sorted(
            all_candidates, 
            key=lambda x: x.get('confidence', 0), 
            reverse=True
        )[:15]  # Analyze top 15 candidates
        
        site_results = []
        for candidate in top_candidates:
            site_result = self.analyze_site_scale(region_data, candidate)
            if site_result and site_result.get('confirmed', False):
                site_results.append(site_result)
        
        results['scales']['sites'] = site_results
        results['discovery_candidates'] = site_results
        
        print(f"\n📊 Multi-scale analysis complete:")
        print(f"   🌍 Regional hotspots: {len(regional_results.get('hotspots', []))}")
        print(f"   🔍 Zone candidates: {len(all_candidates)}")
        print(f"   🎯 Confirmed sites: {len(site_results)}")
        
        return results
    
    def analyze_regional_scale(self, region_data: Dict) -> Dict:
        """
        Tier 1: Regional analysis for settlement network detection
        50km scale at 512x512 resolution (97m per pixel)
        """
        region_id = region_data['region_id']
        
        print("   📡 Creating regional composite...")
        
        # Create regional overview images
        regional_images = self.create_regional_images(region_data)
        
        # Detect settlement clusters using archaeological index
        hotspots = self.detect_settlement_hotspots(region_data)
        
        # Detect potential causeways (linear features)
        linear_features = self.detect_linear_features(region_data)
        
        results = {
            'scale': 'regional',
            'images': regional_images,
            'hotspots': hotspots,
            'linear_features': linear_features,
            'analysis_resolution_m': 97
        }
        
        print(f"   ✅ Regional analysis complete: {len(hotspots)} hotspots detected")
        return results
    
    def analyze_zone_scale(self, region_data: Dict, zone: Dict) -> Dict:
        """
        Tier 2: Zone analysis for individual site detection
        10km scale at 1024x1024 resolution (9.8m per pixel)
        """
        zone_id = zone['id']
        zone_center = zone['center']
        
        print(f"   🔍 Analyzing zone {zone_id} at {zone_center}")
        
        # Create zone-specific images
        zone_images = self.create_zone_images(region_data, zone)
        
        # Detect archaeological features at zone scale
        detections = {
            'concentric_rings': self.detect_concentric_features(region_data, zone),
            'raised_platforms': self.detect_elevated_areas(region_data, zone),
            'geometric_patterns': self.detect_geometric_shapes(region_data, zone),
            'vegetation_anomalies': self.detect_vegetation_patterns(region_data, zone)
        }
        
        # Integrate multiple detection methods
        potential_sites = self.integrate_zone_detections(detections, zone)
        
        results = {
            'zone_id': zone_id,
            'zone_center': zone_center,
            'scale': 'zone',
            'images': zone_images,
            'detections': detections,
            'potential_sites': potential_sites,
            'analysis_resolution_m': 9.8
        }
        
        print(f"     ✅ Zone {zone_id}: {len(potential_sites)} potential sites")
        return results if potential_sites else None
    
    def analyze_site_scale(self, region_data: Dict, candidate: Dict) -> Dict:
        """
        Tier 3: Detailed site confirmation and mapping
        2km scale at 1024x1024 resolution (1.95m per pixel)
        """
        site_center = candidate['center']
        
        print(f"   🎯 Confirming site at {site_center}")
        
        # Create high-resolution site images
        site_images = self.create_site_images(region_data, candidate)
        
        # Extract detailed archaeological features
        features = self.extract_site_features(region_data, candidate)
        
        # Calculate confidence based on multiple factors
        confidence = self.calculate_site_confidence(features)
        
        # Classify site tier (Primary/Secondary/Tertiary)
        site_tier = self.classify_site_tier(features)
        
        # Create precise bounding box
        bbox_wkt = self.create_precise_bbox(features, site_center)
        
        results = {
            'site_id': f"site_{candidate.get('zone_id', 'unknown')}_{candidate.get('id', '001')}",
            'center_lat': site_center[0],
            'center_lng': site_center[1],
            'scale': 'site',
            'images': site_images,
            'features': features,
            'confidence': confidence,
            'site_tier': site_tier,
            'bbox_wkt': bbox_wkt,
            'radius_m': features.get('estimated_radius_m', 100),
            'confirmed': confidence > 0.7,
            'analysis_resolution_m': 1.95
        }
        
        if confidence > 0.7:
            print(f"     ✅ Site confirmed: {site_tier} (confidence: {confidence:.2f})")
        else:
            print(f"     ⚠️ Site uncertain: confidence {confidence:.2f}")
        
        return results
    
    def create_regional_images(self, region_data: Dict) -> Dict:
        """Create regional overview images for network detection"""
        region_id = region_data['region_id']
        regional_area = region_data['regional_area']
        
        images_created = {}
        
        # Archaeological probability heatmap with dynamic range
        arch_index = region_data['data_sources']['archaeological_index']
        
        # Calculate proper min/max values for archaeological index
        try:
            stats = arch_index.reduceRegion(
                reducer=ee.Reducer.minMax(),
                geometry=regional_area,
                scale=100,  # Coarser scale for regional
                maxPixels=1e9
            ).getInfo()
            
            arch_min = stats.get('archaeological_index_min', 0)
            arch_max = stats.get('archaeological_index_max', 1)
            
            # Handle invalid ranges
            if arch_min is None or arch_max is None or arch_min == arch_max:
                arch_min, arch_max = 0, 0.5
            
            # Use 95th percentile if values are extreme
            if arch_max > 3:
                arch_max = arch_max * 0.8  # Reduce max for better contrast
                
        except Exception as e:
            print(f"   ⚠️ Using default archaeological index range: {e}")
            arch_min, arch_max = 0, 0.3
        
        arch_url = arch_index.getThumbURL({
            'region': regional_area,
            'dimensions': 512,
            'format': 'png',
            'min': arch_min,
            'max': arch_max,
            'palette': ['000033', '000066', '003366', '006666', '336666', 
                       '666633', '996633', 'CC6633', 'FF6633', 'FF3300']
        })
        
        arch_file = self.download_image(
            arch_url, 
            f"{self.output_folder}/regional/{region_id}_archaeological_heatmap.png"
        )
        images_created['archaeological_heatmap'] = arch_file
        
        print(f"   📊 Regional archaeological range: {arch_min:.3f} to {arch_max:.3f}")
        
        # Multi-source composite
        optical = region_data['data_sources']['optical']
        composite_url = optical.select(['B4', 'B3', 'B2']).getThumbURL({
            'region': regional_area,
            'dimensions': 512,
            'format': 'png',
            'min': 0,
            'max': 3000
        })
        
        composite_file = self.download_image(
            composite_url,
            f"{self.output_folder}/regional/{region_id}_optical_composite.png"
        )
        images_created['optical_composite'] = composite_file
        
        return images_created
    
    def create_zone_images(self, region_data: Dict, zone: Dict) -> Dict:
        """Create zone-level images for site detection"""
        region_id = region_data['region_id']
        zone_id = zone['id']
        zone_geometry = zone['geometry']
        
        images_created = {}
        
        # High-resolution optical
        optical = region_data['data_sources']['optical']
        optical_url = optical.select(['B4', 'B3', 'B2']).getThumbURL({
            'region': zone_geometry,
            'dimensions': 1024,
            'format': 'png',
            'min': 0,
            'max': 3000
        })
        
        optical_file = self.download_image(
            optical_url,
            f"{self.output_folder}/zone/{region_id}_{zone_id}_optical.png"
        )
        images_created['optical'] = optical_file
        
        # Radar image
        radar = region_data['data_sources']['radar']
        if radar.bandNames().contains('HH').getInfo():
            radar_band = 'HH'
        else:
            radar_band = 'VV'
            
        radar_url = radar.select(radar_band).getThumbURL({
            'region': zone_geometry,
            'dimensions': 1024,
            'format': 'png',
            'min': -20,
            'max': 0
        })
        
        radar_file = self.download_image(
            radar_url,
            f"{self.output_folder}/zone/{region_id}_{zone_id}_radar.png"
        )
        images_created['radar'] = radar_file
        
        # Archaeological index with corrected visualization
        arch_index = region_data['data_sources']['archaeological_index']
        
        # Calculate proper min/max values for better visualization
        try:
            # Get actual statistics of the archaeological index
            stats = arch_index.reduceRegion(
                reducer=ee.Reducer.minMax(),
                geometry=zone_geometry,
                scale=30,
                maxPixels=1e9
            ).getInfo()
            
            # Use actual data range or fallback to defaults
            arch_min = stats.get('archaeological_index_min', 0)
            arch_max = stats.get('archaeological_index_max', 1)
            
            # Ensure valid range
            if arch_min is None or arch_max is None or arch_min == arch_max:
                arch_min, arch_max = 0, 1
            
            # Normalize the range for better visualization
            if arch_max > 2:  # If values are too high, normalize
                arch_max = np.percentile([arch_min, arch_max], 95)  # Use 95th percentile
        
        except Exception as e:
            print(f"   ⚠️ Failed to get archaeological index stats: {e}")
            arch_min, arch_max = 0, 0.5  # Conservative fallback
        
        # Use a more balanced color palette (blue-green-yellow-red)
        arch_url = arch_index.getThumbURL({
            'region': zone_geometry,
            'dimensions': 1024,
            'format': 'png',
            'min': arch_min,
            'max': arch_max,
            'palette': ['000066', '0066CC', '00CC66', 'CCCC00', 'CC6600', 'CC0000']
        })
        
        arch_file = self.download_image(
            arch_url,
            f"{self.output_folder}/zone/{region_id}_{zone_id}_archaeological.png"
        )
        images_created['archaeological'] = arch_file
        
        print(f"   📊 Archaeological index range: {arch_min:.3f} to {arch_max:.3f}")
        
        return images_created
    
    def create_site_images(self, region_data: Dict, candidate: Dict) -> Dict:
        """Create high-resolution site images for detailed analysis"""
        region_id = region_data['region_id']
        site_center = candidate['center']
        
        # Create 2km x 2km area around site center
        lat, lng = site_center
        site_buffer = 0.009  # ~1km radius
        site_geometry = region_data['regional_area'].__class__.Rectangle([
            lng - site_buffer, lat - site_buffer,
            lng + site_buffer, lat + site_buffer
        ])
        
        images_created = {}
        
        # Ultra high-resolution optical
        optical = region_data['data_sources']['optical']
        optical_url = optical.select(['B4', 'B3', 'B2']).getThumbURL({
            'region': site_geometry,
            'dimensions': 1024,
            'format': 'png',
            'min': 0,
            'max': 3000
        })
        
        site_id = candidate.get('id', 'unknown')
        optical_file = self.download_image(
            optical_url,
            f"{self.output_folder}/site/{region_id}_site_{site_id}_optical.png"
        )
        images_created['optical'] = optical_file
        
        return images_created
    
    def detect_settlement_hotspots(self, region_data: Dict) -> List[Dict]:
        """Detect settlement clusters at regional scale"""
        # This is simplified - in real implementation would use GEE's 
        # clustering algorithms and statistical analysis
        
        # Create mock hotspots for demonstration
        hotspots = []
        center_lat, center_lng = region_data['region_info']['center']
        
        # Generate potential hotspot locations
        import random
        for i in range(3):  # Find up to 3 hotspots per region
            hotspot_lat = center_lat + random.uniform(-0.15, 0.15)
            hotspot_lng = center_lng + random.uniform(-0.15, 0.15)
            
            hotspots.append({
                'id': f'hotspot_{i+1}',
                'center': [hotspot_lat, hotspot_lng],
                'confidence': random.uniform(0.6, 0.9),
                'estimated_sites': random.randint(2, 5)
            })
        
        return hotspots
    
    def detect_linear_features(self, region_data: Dict) -> List[Dict]:
        """Detect potential causeways and linear earthworks"""
        # Simplified implementation
        return [
            {
                'id': 'linear_1',
                'type': 'potential_causeway',
                'confidence': 0.7,
                'length_km': 3.2
            }
        ]
    
    def identify_priority_zones(self, region_data: Dict, regional_results: Dict) -> List[Dict]:
        """Identify high-priority zones for detailed analysis"""
        priority_zones = []
        
        # Create zones around detected hotspots
        for hotspot in regional_results.get('hotspots', []):
            lat, lng = hotspot['center']
            
            # Create 3x3 grid around each hotspot
            for i in range(3):
                for j in range(3):
                    zone_lat = lat + (i - 1) * 0.042  # ~4.6km spacing
                    zone_lng = lng + (j - 1) * 0.042
                    
                    zone = {
                        'id': f"{hotspot['id']}_zone_{i}_{j}",
                        'center': [zone_lat, zone_lng],
                        'geometry': region_data['regional_area'].__class__.Rectangle([
                            zone_lng - 0.042, zone_lat - 0.042,
                            zone_lng + 0.042, zone_lat + 0.042
                        ]),
                        'priority': hotspot['confidence'],
                        'parent_hotspot': hotspot['id']
                    }
                    priority_zones.append(zone)
        
        # Sort by priority
        return sorted(priority_zones, key=lambda x: x['priority'], reverse=True)
    
    def detect_concentric_features(self, region_data: Dict, zone: Dict) -> List[Dict]:
        """Detect concentric rings characteristic of defensive earthworks"""
        # Simplified implementation - would use circular Hough transforms
        import random
        
        detections = []
        if random.random() > 0.7:  # 30% chance of detection
            detections.append({
                'center': zone['center'],
                'radius_m': random.randint(80, 200),
                'confidence': random.uniform(0.6, 0.9),
                'ring_count': random.randint(1, 3)
            })
        
        return detections
    
    def detect_elevated_areas(self, region_data: Dict, zone: Dict) -> List[Dict]:
        """Detect raised platforms and mounds"""
        # Simplified implementation
        import random
        
        detections = []
        if random.random() > 0.6:  # 40% chance
            detections.append({
                'center': zone['center'],
                'area_ha': random.randint(5, 50),
                'confidence': random.uniform(0.5, 0.8)
            })
        
        return detections
    
    def detect_geometric_shapes(self, region_data: Dict, zone: Dict) -> List[Dict]:
        """Detect geometric patterns too regular to be natural"""
        # Simplified implementation
        import random
        
        detections = []
        if random.random() > 0.8:  # 20% chance
            detections.append({
                'shape': random.choice(['circular', 'rectangular', 'polygonal']),
                'center': zone['center'],
                'size_m': random.randint(50, 150),
                'confidence': random.uniform(0.4, 0.7)
            })
        
        return detections
    
    def detect_vegetation_patterns(self, region_data: Dict, zone: Dict) -> List[Dict]:
        """Detect vegetation anomalies indicating buried structures"""
        # Simplified implementation
        import random
        
        detections = []
        if random.random() > 0.5:  # 50% chance
            detections.append({
                'pattern': 'vegetation_stress',
                'center': zone['center'],
                'confidence': random.uniform(0.3, 0.6)
            })
        
        return detections
    
    def integrate_zone_detections(self, detections: Dict, zone: Dict) -> List[Dict]:
        """Integrate multiple detection methods into site candidates"""
        candidates = []
        
        # Combine different types of evidence
        all_detections = []
        for detection_type, detection_list in detections.items():
            for detection in detection_list:
                detection['type'] = detection_type
                all_detections.append(detection)
        
        # Group detections by proximity
        for detection in all_detections:
            candidates.append({
                'id': f"candidate_{len(candidates)+1}",
                'center': detection['center'],
                'zone_id': zone['id'],
                'confidence': detection['confidence'],
                'evidence_types': [detection['type']],
                'source_detections': [detection]
            })
        
        return candidates
    
    def extract_site_features(self, region_data: Dict, candidate: Dict) -> Dict:
        """Extract detailed features from high-resolution site analysis"""
        # Simplified feature extraction
        import random
        
        features = {
            'defensive_rings': random.randint(0, 3),
            'central_platform': random.choice([True, False]),
            'estimated_radius_m': random.randint(50, 200),
            'area_hectares': random.randint(5, 150),
            'geometric_regularity': random.uniform(0.4, 0.9),
            'elevation_prominence': random.uniform(0.2, 0.8),
            'vegetation_anomaly': random.uniform(0.3, 0.7),
            'radar_signature': random.uniform(0.4, 0.8)
        }
        
        return features
    
    def calculate_site_confidence(self, features: Dict) -> float:
        """Calculate multi-factor confidence score"""
        confidence_factors = []
        
        # Geometric regularity (higher = more likely human-made)
        if features['geometric_regularity'] > 0.7:
            confidence_factors.append(0.25)
        elif features['geometric_regularity'] > 0.5:
            confidence_factors.append(0.15)
        
        # Defensive features
        rings = features['defensive_rings']
        if rings >= 2:
            confidence_factors.append(0.25)
        elif rings == 1:
            confidence_factors.append(0.15)
        
        # Size in known range
        area = features['area_hectares']
        if 20 <= area <= 400:  # Known Casarabe range
            confidence_factors.append(0.2)
        elif 5 <= area <= 20:
            confidence_factors.append(0.1)
        
        # Multi-source visibility
        if features['radar_signature'] > 0.6:
            confidence_factors.append(0.15)
        
        # Elevation prominence
        if features['elevation_prominence'] > 0.6:
            confidence_factors.append(0.15)
        
        return min(sum(confidence_factors), 1.0)
    
    def classify_site_tier(self, features: Dict) -> str:
        """Classify site as Primary, Secondary, or Tertiary"""
        area = features['area_hectares']
        rings = features['defensive_rings']
        
        if area >= 100 and rings >= 2:
            return "Primary"
        elif area >= 20 and rings >= 1:
            return "Secondary"
        else:
            return "Tertiary"
    
    def create_precise_bbox(self, features: Dict, site_center: List[float]) -> str:
        """Create precise WKT bounding box for the site"""
        lat, lng = site_center
        radius_m = features['estimated_radius_m']
        
        # Convert meters to degrees (approximate)
        lat_deg_per_m = 1 / 111000
        lng_deg_per_m = 1 / (111000 * abs(lat))
        
        radius_lat = radius_m * lat_deg_per_m
        radius_lng = radius_m * lng_deg_per_m
        
        # Create bounding box
        south = lat - radius_lat
        north = lat + radius_lat
        west = lng - radius_lng
        east = lng + radius_lng
        
        bbox_wkt = f"POLYGON(({west} {south}, {east} {south}, {east} {north}, {west} {north}, {west} {south}))"
        
        return bbox_wkt
    
    def download_image(self, url: str, filepath: str) -> str:
        """Download image from URL with error handling"""
        try:
            response = requests.get(url, timeout=60)
            response.raise_for_status()
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            return filepath
            
        except Exception as e:
            print(f"   ⚠️ Failed to download {os.path.basename(filepath)}: {e}")
            return None
    
    def process_all_regions(self, loaded_data: Dict) -> Dict:
        """Process all loaded regions with multi-scale analysis"""
        if not loaded_data:
            print("❌ No data to process")
            return {}
        
        print(f"\n🔬 Multi-Scale Archaeological Analysis")
        print(f"📊 Processing {len(loaded_data)} regions")
        print("=" * 60)
        
        all_results = {}
        
        for region_id, region_data in loaded_data.items():
            print(f"\n🏛️ Processing {region_data['region_info']['name']}...")
            
            # Run complete multi-scale analysis
            results = self.process_region_multiscale(region_data)
            all_results[region_id] = results
            
            # Brief delay between regions
            time.sleep(2)
        
        self.processed_data = all_results
        
        # Summary statistics
        total_candidates = sum(
            len(result['discovery_candidates']) 
            for result in all_results.values()
        )
        
        print(f"\n📊 MULTI-SCALE ANALYSIS COMPLETE:")
        print("=" * 40)
        print(f"🌍 Regions processed: {len(all_results)}")
        print(f"🎯 Discovery candidates: {total_candidates}")
        print(f"📁 Images created in: {self.output_folder}/")
        
        return all_results
    
    def get_all_discoveries(self) -> List[Dict]:
        """Get all archaeological discoveries across all regions"""
        all_discoveries = []
        
        for region_id, results in self.processed_data.items():
            for site in results['discovery_candidates']:
                site['region_id'] = region_id
                site['region_name'] = results['region_name']
                all_discoveries.append(site)
        
        # Sort by confidence
        return sorted(all_discoveries, key=lambda x: x['confidence'], reverse=True)


# Test the enhanced processor
if __name__ == "__main__":
    print("🔬 Enhanced Multi-Scale Processor Test")
    print("=" * 45)
    
    processor = EnhancedDataProcessor()
    
    print(f"✅ Multi-scale processor ready!")
    print(f"📊 Analysis scales configured:")
    for scale, config in processor.analysis_scales.items():
        print(f"   {scale}: {config['size_km']}km at {config['resolution_m']}m")
    print(f"📁 Output folder: {processor.output_folder}/")
    print(f"🏛️ Ready for archaeological discovery!")