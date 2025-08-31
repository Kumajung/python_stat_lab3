from osgeo import gdal

def raster_to_ascii(input_raster, output_ascii, nodata_value=-9999):
    """
    Converts a raster file to ASCII format, replacing NoData values with a specified value.
    
    :param input_raster: Path to the input raster file.
    :param output_ascii: Path to the output ASCII file.
    :param nodata_value: The value to replace NoData values with (default is -9999).
    """
    # Open the raster file
    raster = gdal.Open(input_raster)
    if not raster:
        raise FileNotFoundError(f"Cannot open file: {input_raster}")
    
    # Get the current NoData value, if it exists
    band = raster.GetRasterBand(1)  # Assumes single band raster
    current_nodata = band.GetNoDataValue()
    
    # Set the NoData value for the output (if the raster has NoData values)
    if current_nodata is not None:
        print(f"Replacing NoData values ({current_nodata}) with {nodata_value}")
        band.SetNoDataValue(nodata_value)

    # Define the output format
    driver = gdal.GetDriverByName('AAIGrid')
    if not driver:
        raise RuntimeError("AAIGrid driver not found!")

    # Convert to ASCII
    driver.CreateCopy(output_ascii, raster)
    print(f"Raster successfully converted to ASCII: {output_ascii}")

# Example usage
input_raster_path = "bio1.tif"
output_ascii_path = "bio1.asc"

raster_to_ascii(input_raster_path, output_ascii_path)
