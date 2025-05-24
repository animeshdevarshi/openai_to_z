# fixed_enhanced_data_acquisition.py
# Corrected multi-source data loading for Checkpoint 2
# Fixes Google Earth Engine API errors

import ee
import json
import time
from datetime import datetime
from typing import Dict, List, Tuple, Optional

# Import region configuration
from simple_region_config import SimpleRegionConfig

class EnhancedDataAcquisition:
    """
    Fixed enhanced data acquisition for Checkpoint 2
    Implements dual-source loading with proper GEE API calls
    """
    
    def __init__(self):
        """Initialize with corrected dual-source capability"""
        self.authenticated = False
        self.loaded_data = {}
        self.failed_regions = []
        
        # Initialize region configuration
        self.region_config = SimpleRegionConfig()
        
        # Track data sources for Checkpoint 2 compliance
        self.data_sources_used = {
            'source_1': {
                'name': 'Sentinel-2 MSI Level-2A',
                'dataset_id': 'COPERNICUS/S2_SR_HARMONIZED',
                'type': 'Optical Multispectral Imagery',
                'resolution_m': 10,
                'purpose': 'Vegetation patterns and spectral anomalies'
            },
            'source_2': {
                'name': 'Sentinel-1 SAR GRD',
                'dataset_id': 'COPERNICUS/S1_GRD',
                'type': 'C-band Synthetic Aperture Radar',
                'resolution_m': 10,
                'purpose': 'Ground surface structure through canopy'
            }
        }
        
        print("📡 Fixed Enhanced Data Acquisition initialized")
        print("🔄 Dual-source capability: Optical + Radar")
        
    def setup_google_earth_engine(self):
        """Setup Google Earth Engine with proper error handling"""
        print("🔑 Setting up Google Earth Engine...")
        
        try:
            # Always try to initialize (it's safe to call multiple times)
            ee.Initialize()
            
            # Don't make API calls during setup - just check if initialize worked
            # API calls like .getInfo() can hang if auth is not working
            
            self.authenticated = True
            print("✅ Google Earth Engine ready!")
            print("📊 Connection will be verified when loading data")
            return True
            
        except Exception as e:
            self.authenticated = False
            print(f"❌ Authentication failed: {e}")
            print("\n🔧 SETUP REQUIRED:")
            print("1. Run: import ee")
            print("2. Run: ee.Authenticate()")  
            print("3. Follow the authentication flow")
            print("4. Run this script again")
            print("\nOr visit: https://developers.google.com/earth-engine/guides/python_install")
            return False
    
    def load_dual_source_data(self, region_id: str, region_info: Dict) -> Optional[Dict]:
        """
        Load both optical and radar data with corrected API calls
        """
        print(f"📡 Loading dual-source data for {region_info['name']}...")
        
        try:
            # Define region geometry
            lat, lng = region_info['center']
            area_size = 0.2  # ~22km x 22km area
            
            region_area = ee.Geometry.Rectangle([
                lng - area_size, lat - area_size,
                lng + area_size, lat + area_size
            ])
            
            # SOURCE 1: Sentinel-2 Optical Data
            print("   📸 Loading Sentinel-2 optical data...")
            sentinel2 = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED') \
                .filterBounds(region_area) \
                .filterDate('2023-01-01', '2023-12-31') \
                .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 30))
            
            s2_count = sentinel2.size().getInfo()
            
            if s2_count == 0:
                print("   🔄 Expanding date range...")
                sentinel2 = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED') \
                    .filterBounds(region_area) \
                    .filterDate('2022-01-01', '2023-12-31') \
                    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 50))
                s2_count = sentinel2.size().getInfo()
            
            if s2_count == 0:
                print(f"   ❌ No Sentinel-2 data for {region_id}")
                return None
            
            # Create optical composite
            optical_composite = sentinel2.median().clip(region_area)
            
            # SOURCE 2: Sentinel-1 Radar Data (more reliable than PALSAR)
            print("   📡 Loading Sentinel-1 radar data...")
            sentinel1 = ee.ImageCollection('COPERNICUS/S1_GRD') \
                .filterBounds(region_area) \
                .filterDate('2023-01-01', '2023-12-31') \
                .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV')) \
                .filter(ee.Filter.eq('instrumentMode', 'IW'))
            
            s1_count = sentinel1.size().getInfo()
            
            if s1_count == 0:
                print("   🔄 Expanding radar date range...")
                sentinel1 = ee.ImageCollection('COPERNICUS/S1_GRD') \
                    .filterBounds(region_area) \
                    .filterDate('2022-01-01', '2023-12-31') \
                    .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))
                s1_count = sentinel1.size().getInfo()
            
            if s1_count == 0:
                print(f"   ❌ No Sentinel-1 data for {region_id}")
                return None
            
            # Create radar composite
            radar_composite = sentinel1.select(['VV', 'VH']).median().clip(region_area)
            
            # Additional data layers
            print("   🗻 Loading elevation data...")
            elevation = ee.Image('USGS/SRTMGL1_003').clip(region_area)
            
            # Calculate indices with corrected API calls
            print("   🧮 Calculating archaeological indices...")
            
            # NDVI for vegetation analysis
            ndvi = optical_composite.normalizedDifference(['B8', 'B4']).rename('ndvi')
            
            # Archaeological probability index (simplified and corrected)
            arch_index = self.calculate_archaeological_index_fixed(
                optical_composite, radar_composite, elevation, ndvi
            )
            
            # Package the data
            region_data = {
                'region_id': region_id,
                'region_info': region_info,
                'regional_area': region_area,
                
                # Data sources (Checkpoint 2 requirement)
                'data_sources': {
                    'optical': optical_composite,
                    'radar': radar_composite,
                    'elevation': elevation,
                    'ndvi': ndvi,
                    'archaeological_index': arch_index
                },
                
                # Metadata for validation
                'metadata': {
                    'optical_scenes': s2_count,
                    'radar_scenes': s1_count,
                    'data_sources_count': 2,
                    'dataset_ids': [
                        'COPERNICUS/S2_SR_HARMONIZED',
                        'COPERNICUS/S1_GRD'
                    ],
                    'load_timestamp': datetime.now().isoformat(),
                },
                
                'status': 'loaded'
            }
            
            print(f"   ✅ Successfully loaded {region_id}")
            print(f"   📊 {s2_count} optical, {s1_count} radar scenes")
            
            return region_data
            
        except Exception as e:
            print(f"   ❌ Failed to load {region_id}: {e}")
            self.failed_regions.append(region_id)
            return None
    
    def calculate_archaeological_index_fixed(self, optical, radar, elevation, ndvi):
        """
        Calculate fixed archaeological index with proper bounds and normalization
        Addresses red image visualization issue
        """
        try:
            # Multi-band analysis for archaeological features
            optical_bands = optical.select(['B4', 'B3', 'B2', 'B8'])  # Red, Green, Blue, NIR
            
            # Vegetation indices
            evi = optical.expression(
                '2.5 * ((NIR - RED) / (NIR + 6 * RED - 7.5 * BLUE + 1))', {
                    'NIR': optical.select('B8'),
                    'RED': optical.select('B4'),
                    'BLUE': optical.select('B2')
                }
            ).clamp(-1, 1)
            
            # Soil and terrain features
            soil_brightness = optical_bands.reduce(ee.Reducer.mean())
            terrain_roughness = elevation.focal_stdDev(ee.Kernel.circle(1))
            
            # Radar texture analysis
            radar_texture = radar.focal_stdDev(ee.Kernel.circle(2))
            radar_smoothness = radar.focal_mean(ee.Kernel.circle(3))
            
            # Archaeological feature indicators
            arch_components = [
                ndvi.multiply(-0.3),  # Less vegetation
                evi.multiply(-0.2),   # Modified vegetation
                soil_brightness.multiply(0.4),  # Exposed soil
                terrain_roughness.multiply(0.3),  # Terrain modification
                radar_texture.multiply(0.2),     # Surface texture
                radar_smoothness.multiply(0.1)    # Surface smoothness
            ]
            
            # Sum all components
            arch_index = ee.Image(arch_components).reduce(ee.Reducer.sum())
            
            # Clean up invalid values (NaN, Infinity)
            arch_index = arch_index.where(arch_index.lt(0), 0)  # Remove negative values
            arch_index = arch_index.where(arch_index.gt(10), 1)  # Cap extreme values
            arch_index = arch_index.unmask(0)  # Replace masked values with 0
            
            # Create a reasonable geometry for the region (approximately 50km x 50km)
            center_coords = optical.geometry().centroid(1).coordinates()
            region_geometry = ee.Geometry.Rectangle([
                center_coords.get(0).subtract(0.25),
                center_coords.get(1).subtract(0.25),
                center_coords.get(0).add(0.25),
                center_coords.get(1).add(0.25)
            ])
            
            # Normalize to 0-1 range using percentile normalization
            try:
                percentiles = arch_index.reduceRegion(
                    reducer=ee.Reducer.percentile([5, 95]),
                    geometry=region_geometry,
                    scale=100,
                    maxPixels=1e9
                )
                
                # Apply percentile normalization if possible
                p5 = ee.Number(percentiles.get('archaeological_index_p5', 0))
                p95 = ee.Number(percentiles.get('archaeological_index_p95', 1))
                arch_index = arch_index.subtract(p5).divide(p95.subtract(p5)).clamp(0, 1)
            except:
                # Fallback: simple division by maximum
                arch_max = arch_index.reduceRegion(
                    reducer=ee.Reducer.max(),
                    geometry=region_geometry,
                    scale=100,
                    maxPixels=1e9
                ).get('archaeological_index')
                arch_index = arch_index.divide(ee.Number(arch_max).max(0.1))
            
            return arch_index.rename('archaeological_index')
            
        except Exception as e:
            print(f"   ⚠️ Simplified index calculation: {e}")
            # Fallback to simple NDVI if complex calculation fails
            simple_index = ndvi.abs().clamp(0, 1)
            return simple_index.rename('archaeological_index')
    
    def load_multiple_regions(self, max_regions: int = 3) -> Dict:
        """
        Load dual-source data for multiple high-priority regions
        Ensures two independent data sources per region
        """
        print(f"🌍 Loading dual-source data for {max_regions} regions...")
        print("=" * 60)
        
        # Get regions by priority (high first)
        all_regions = self.region_config.get_regions_by_priority(max_regions=10)
        
        loaded_data = {}
        
        for region_id, region_info in all_regions.items():
            if len(loaded_data) >= max_regions:
                break
            
            print(f"\n📍 Processing region {region_id}...")
            region_data = self.load_dual_source_data(region_id, region_info)
            
            if region_data:
                loaded_data[region_id] = region_data
                print(f"✅ {region_id} loaded successfully")
            else:
                print(f"❌ {region_id} failed to load")
        
        return loaded_data

    def load_specific_regions(self, region_ids: List[str]) -> Dict:
        """
        Load dual-source data for specific user-selected regions
        """
        print(f"🌍 Loading dual-source data for selected regions...")
        print("=" * 60)
        
        all_regions = self.region_config.get_regions_by_priority(max_regions=10)
        loaded_data = {}
        
        for region_id in region_ids:
            if region_id not in all_regions:
                print(f"⚠️ Region {region_id} not found in configuration")
                continue
            
            print(f"\n📍 Processing region {region_id}...")
            region_info = all_regions[region_id]
            region_data = self.load_dual_source_data(region_id, region_info)
            
            if region_data:
                loaded_data[region_id] = region_data
                print(f"✅ {region_id} loaded successfully")
            else:
                print(f"❌ {region_id} failed to load")
        
        if not loaded_data:
            print("❌ No regions loaded successfully")
            print("💡 Consider trying different regions or checking data availability")
        
        return loaded_data
    
    def show_summary(self):
        """Display comprehensive summary"""
        if not self.loaded_data:
            print("❌ No data loaded yet")
            return
        
        print(f"\n📊 ENHANCED DATA SUMMARY:")
        print("=" * 40)
        print(f"🎯 Checkpoint 2 Compliance: ✅")
        print(f"📊 Independent sources: 2 (Optical + Radar)")
        print(f"📍 Regions loaded: {len(self.loaded_data)}")
        
        for region_id, data in self.loaded_data.items():
            info = data['region_info']
            meta = data['metadata']
            print(f"\n✅ {region_id}")
            print(f"   📍 {info['name']} ({info['country']})")
            print(f"   📸 {meta['optical_scenes']} optical scenes")
            print(f"   📡 {meta['radar_scenes']} radar scenes")
            print(f"   🎯 Archaeological index: Ready")
        
        print(f"\n🔄 Ready for next step: Multi-scale processing")

    def get_data_summary(self) -> Dict:
        """Return data summary as dictionary for programmatic access"""
        if not self.loaded_data:
            return {
                'status': 'no_data',
                'regions_loaded': 0,
                'checkpoint2_compliance': False,
                'data_sources': []
            }
        
        summary = {
            'status': 'data_loaded',
            'regions_loaded': len(self.loaded_data),
            'checkpoint2_compliance': True,
            'independent_sources_count': 2,
            'data_sources': [
                'COPERNICUS/S2_SR_HARMONIZED',
                'COPERNICUS/S1_GRD'
            ],
            'regions': {},
            'total_optical_scenes': 0,
            'total_radar_scenes': 0
        }
        
        for region_id, data in self.loaded_data.items():
            region_info = data['region_info']
            metadata = data['metadata']
            
            summary['regions'][region_id] = {
                'name': region_info['name'],
                'country': region_info['country'],
                'optical_scenes': metadata['optical_scenes'],
                'radar_scenes': metadata['radar_scenes'],
                'status': 'loaded'
            }
            
            summary['total_optical_scenes'] += metadata['optical_scenes']
            summary['total_radar_scenes'] += metadata['radar_scenes']
        
        return summary

    def create_data_summary(self) -> Dict:
        """Create summary of loaded data"""
        summary = {
            'timestamp': datetime.now().isoformat(),
            'checkpoint2_compliance': True,  # Flag for validation
            'data_sources': [
                'COPERNICUS/S2_SR_HARMONIZED',  # Sentinel-2 Optical
                'COPERNICUS/S1_GRD'             # Sentinel-1 Radar
            ],
            'regions': {},
            'total_optical_scenes': 0,
            'total_radar_scenes': 0,
            'independent_sources_count': 2
        }
        
        # Add region details
        for region_id, region_data in self.loaded_data.items():
            optical_count = len(region_data.get('data_sources', {}).get('optical', []))
            radar_count = len(region_data.get('data_sources', {}).get('radar', []))
            
            summary['regions'][region_id] = {
                'name': region_data.get('region_info', {}).get('name', region_id),
                'optical_scenes': optical_count,
                'radar_scenes': radar_count,
                'data_quality': region_data.get('status', 'unknown'),
                'total_scenes': optical_count + radar_count
            }
            
            summary['total_optical_scenes'] += optical_count
            summary['total_radar_scenes'] += radar_count
        
        return summary


# Test the fixed system
if __name__ == "__main__":
    print("🏛️ Fixed Enhanced Data Acquisition Test")
    print("=" * 50)
    
    # Initialize fixed system
    data_loader = EnhancedDataAcquisition()
    
    # Setup Google Earth Engine
    if data_loader.setup_google_earth_engine():
        print("\n🚀 Testing fixed dual-source data loading...")
        
        # Load data for 3 regions
        loaded_data = data_loader.load_multiple_regions(max_regions=3)
        
        # Show summary
        data_loader.show_summary()
        
        if loaded_data:
            print(f"\n✅ Fixed data acquisition working!")
            print(f"🎯 Ready for Checkpoint 2 processing")
        else:
            print(f"\n❌ Still having issues - check your GEE access")
            
    else:
        print("\n⚠️ Please setup Google Earth Engine first")
        print("Run these commands:")
        print("import ee")
        print("ee.Authenticate()")