-- Script that ranks country origins of band
-- Should display the origin and nb-fans
  SELECT origin, sum(fans) as nb_fans
    FROM metal_bands
GROUP BY origin
ORDER by nb_fans DESC;
