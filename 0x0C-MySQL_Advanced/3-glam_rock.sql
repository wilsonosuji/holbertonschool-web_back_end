-- 3. Old school band
-- This SQL script lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, (ifnull(split, 2020)-formed) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
