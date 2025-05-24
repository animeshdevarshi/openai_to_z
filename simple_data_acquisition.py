# simple_data_acquisition.py
# Simple data downloading from Google Earth Engine

import ee
import time
from datetime import datetime
from simple_region_config import SimpleRegionConfig

class SimpleDataAcquisition:
    """
    Simple data downloader for satellite imagery
    Focuses on basic functionality that's easy to understand
    """
    
    def __init__(self):
        """Initialize the data acquisition system"""
        self.authenticated = False
        self.region_config = SimpleRegionConfig()
        self.loaded_data = {}
        self.failed_regions = []
        
        print("🚀 Simple Data Acquisition initialized")
    
    def setup_google_earth_engine(self):
        """Setup Google Earth Engine authentication"""
        print("🔑 Setting up Google Earth Engine...")
        
        try:
            # Try to initialize (if already authenticated)
            ee.Initialize()
            self.authenticated = True
            print("✅ Google Earth Engine ready!")
            return True
            
        except Exception as e:
            print("❌ Need to authenticate Google Earth Engine")
            print("\n🔧 SETUP INSTRUCTIONS:")
            print("1. Go to https://earthengine.google.com/")
            print("2. Sign up with your Google account")
            print("3. Wait for approval (1-2 days)")
            print("4. Run: ee.Authenticate() in Python")
            print("5. Then run this script again")
            return False
    
    def load_region_satellite_data(self, region_id, region_info):
        """
        Load satellite data for one region
        Simple version - just Sentinel-2 optical imagery
        """
        print(f"📡 Loading data for {region_info['name']}...")
        
        try:
            # Get region center coordinates
            lat, lng = region_info['center']
            
            # Create a 50km x 50km area around the center
            area_size = 0.25  # degrees (roughly 25km)
            region_area = ee.Geometry.Rectangle([
                lng - area_size, lat - area_size,  # bottom-left
                lng + area_size, lat + area_size   # top-right
            ])
            
            # Get Sentinel-2 satellite images
            satellite_images = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED') \
                .filterBounds(region_area) \
                .filterDate('2023-01-01', '2023-12-31') \
                .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 30))  # Less than 30% clouds
            
            # Check if we found any images
            image_count = satellite_images.size().getInfo()
            print(f"   Found {image_count} satellite images")
            
            if image_count == 0:
                print(f"   ⚠️ No good images found for {region_id}")
                self.failed_regions.append(region_id)
                return None
            
            # Create a single composite image (median of all images)
            composite_image = satellite_images.median().clip(region_area)
            
            # Try to get elevation data too
            elevation_data = None
            try:
                elevation_data = ee.Image('USGS/SRTMGL1_003').clip(region_area)
                print(f"   ✅ Elevation data loaded")
            except Exception as e:
                print(f"   ⚠️ Could not load elevation data: {e}")
            
            # Package the data
            region_data = {
                'region_id': region_id,
                'region_info': region_info,
                'area_geometry': region_area,
                'satellite_image': composite_image,
                'elevation_data': elevation_data,
                'image_count': image_count,
                'load_time': datetime.now().isoformat(),
                'status': 'success'
            }
            
            print(f"   ✅ Successfully loaded data for {region_id}")
            return region_data
            
        except Exception as e:
            print(f"   ❌ Failed to load {region_id}: {e}")
            self.failed_regions.append(region_id)
            return None
    
    def load_multiple_regions(self, region_list=None, max_regions=3):
        """
        Load data for multiple regions
        Simple version - one at a time to avoid complexity
        """
        if not self.authenticated:
            print("❌ Please setup Google Earth Engine first!")
            return {}
        
        # Use provided regions or get top priority regions
        if region_list is None:
            regions_to_load = self.region_config.get_regions_by_priority(max_regions)
        else:
            regions_to_load = region_list
        
        print(f"\n🌍 Loading data for {len(regions_to_load)} regions...")
        print("=" * 50)
        
        loaded_data = {}
        
        for region_id, region_info in regions_to_load.items():
            print(f"\n📍 Processing region {region_id}...")
            
            # Load data for this region
            region_data = self.load_region_satellite_data(region_id, region_info)
            
            if region_data:
                loaded_data[region_id] = region_data
            
            # Small delay to be nice to Google Earth Engine
            time.sleep(2)
        
        # Save results
        self.loaded_data = loaded_data
        
        # Print summary
        print(f"\n📊 LOADING SUMMARY:")
        print(f"   ✅ Successful: {len(loaded_data)} regions")
        print(f"   ❌ Failed: {len(self.failed_regions)} regions")
        
        if self.failed_regions:
            print(f"   Failed regions: {', '.join(self.failed_regions)}")
        
        return loaded_data
    
    def get_loaded_regions(self):
        """Get list of successfully loaded regions"""
        return list(self.loaded_data.keys())
    
    def get_region_data(self, region_id):
        """Get data for a specific region"""
        return self.loaded_data.get(region_id, None)
    
    def show_summary(self):
        """Show a simple summary of loaded data"""
        if not self.loaded_data:
            print("❌ No data loaded yet")
            return
        
        print(f"\n📊 DATA SUMMARY:")
        print("=" * 30)
        
        for region_id, data in self.loaded_data.items():
            info = data['region_info']
            print(f"✅ {region_id}")
            print(f"   📍 {info['name']}")
            print(f"   🏴 {info['country']}")
            print(f"   📡 {data['image_count']} satellite images")
            print(f"   🗻 Elevation: {'Yes' if data['elevation_data'] else 'No'}")
            print()


# Simple test function
if __name__ == "__main__":
    # Test the data acquisition
    data_loader = SimpleDataAcquisition()
    
    # Setup Google Earth Engine
    if data_loader.setup_google_earth_engine():
        print("\n🚀 Testing data loading...")
        
        # Load data for top 2 regions
        loaded_data = data_loader.load_multiple_regions(max_regions=2)
        
        # Show summary
        data_loader.show_summary()
        
    else:
        print("\n⚠️ Please setup Google Earth Engine first")
        print("Run: ee.Authenticate() in Python")
